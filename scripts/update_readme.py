"""Atualiza as seções automáticas do README de perfil.

- PORTFOLIO: todo repositório público com o tópico "portfolio" (mais os
  extra_repos do config.json), ordenado pelo último push.
- RECENT: os repositórios públicos com push mais recente.

Uso: GITHUB_TOKEN=... python scripts/update_readme.py
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
README = ROOT / "README.md"
API = "https://api.github.com"


def get(path):
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-readme-updater",
    })
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def user_repos(user):
    repos, page = [], 1
    while True:
        batch = get(f"/users/{user}/repos?per_page=100&page={page}&type=owner")
        repos += batch
        if len(batch) < 100:
            return repos
        page += 1


def name_of(repo):
    return CONFIG.get("display_names", {}).get(repo["full_name"], repo["name"].replace("_", " ").replace("-", " "))


def stack_of(repo):
    if repo["full_name"] in CONFIG.get("stacks", {}):
        return CONFIG["stacks"][repo["full_name"]]
    topics = [t for t in repo.get("topics", []) if t != CONFIG["topic"]]
    if topics:
        return ", ".join(topics[:5])
    return repo.get("language") or ""


def portfolio_table(repos):
    rows = ["| Project | What it is | Stack |", "| --- | --- | --- |"]
    for r in repos:
        desc = CONFIG.get("descriptions", {}).get(r["full_name"]) or r.get("description") or ""
        desc = desc.replace("|", "/")
        rows.append(f"| [{name_of(r)}]({r['html_url']}) | {desc} | {stack_of(r)} |")
    return "\n".join(rows)


def recent_list(repos):
    lines = []
    for r in repos:
        lines.append(f"- [{name_of(r)}]({r['html_url']}), updated {r['pushed_at'][:10]}")
    return "\n".join(lines)


def replace_block(text, tag, body):
    pattern = re.compile(rf"(<!-- {tag}:START -->)(.*?)(<!-- {tag}:END -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"Marcadores {tag} não encontrados no README")
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    user = CONFIG["user"]
    own = [r for r in user_repos(user)
           if not r["fork"] and not r["private"] and r["name"].lower() != user.lower()
           and r["name"] not in CONFIG.get("exclude", [])]
    extra = []
    for full in CONFIG.get("extra_repos", []):
        try:
            extra.append(get(f"/repos/{full}"))
        except Exception as exc:  # repo apagado ou privado
            print(f"Ignorando {full}: {exc}")

    portfolio = [r for r in own if CONFIG["topic"] in r.get("topics", [])]
    seen = {r["full_name"].lower() for r in portfolio}
    portfolio += [r for r in extra if r["full_name"].lower() not in seen]
    portfolio.sort(key=lambda r: r["pushed_at"], reverse=True)
    recent = sorted(own, key=lambda r: r["pushed_at"], reverse=True)[: CONFIG["max_recent"]]

    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "PORTFOLIO", portfolio_table(portfolio))
    text = replace_block(text, "RECENT", recent_list(recent))
    README.write_text(text, encoding="utf-8")
    print(f"{len(portfolio)} projetos no portfólio, {len(recent)} recentes")


if __name__ == "__main__":
    main()
