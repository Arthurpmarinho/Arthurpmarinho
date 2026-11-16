# Hi, I'm Arthur Pinheiro Marinho

Electronics engineering student at the University of Brasília, currently on exchange at ENSEA in Cergy, France.
I build embedded systems end to end, from the schematic and the PCB to the firmware and the test bench.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arthur-pinheiro-marinho-610887343)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:arthurpinheiromarinho@gmail.com)

## Featured project · Capital Rocket Team avionics

<a href="https://github.com/Arthurpmarinho/capital-rocket-team-avionics"><img src="https://raw.githubusercontent.com/Arthurpmarinho/capital-rocket-team-avionics/main/docs/images/crm_3d_top.png" height="200" alt="Control and Recovery Module"></a>
<a href="https://github.com/Arthurpmarinho/capital-rocket-team-avionics"><img src="https://raw.githubusercontent.com/Arthurpmarinho/capital-rocket-team-avionics/main/docs/images/gnm_3d_top.png" height="200" alt="Guidance and Navigation Module"></a>

Flight avionics for Boscov, the hybrid rocket of the Capital Rocket Team. **1st place in the hybrid rocket category at the Latin American Space Challenge (LASC) 2025.**
I helped design the onboard boards in EasyEDA Pro. The Control and Recovery Module drives the tank valves and fires the parachute charges, with current sensing on every channel to confirm each actuation. The Guidance and Navigation Module tracks the flight with GPS and an IMU and streams telemetry over LoRa.

[Repository](https://github.com/Arthurpmarinho/capital-rocket-team-avionics) · [Schematics](https://github.com/Arthurpmarinho/capital-rocket-team-avionics/tree/main/hardware)

## Featured project · Micromouse

<a href="https://github.com/Arthurpmarinho/2026_1_PI1_Grupo02_Hilmer"><img src="https://raw.githubusercontent.com/Arthurpmarinho/2026_1_PI1_Grupo02_Hilmer/main/hw/PCB/Logic%20%26%20Control%20Board/3D_PCB2_2026-06-05.png" height="200" alt="Logic and control board"></a>
<a href="https://github.com/Arthurpmarinho/2026_1_PI1_Grupo02_Hilmer"><img src="https://raw.githubusercontent.com/Arthurpmarinho/2026_1_PI1_Grupo02_Hilmer/main/hw/PCB/Motor%20%26%20Drive%20Board/3D_PCB1_2026-06-30.png" height="200" alt="Motor and drive board"></a>

Autonomous robot that maps an unknown maze and then runs the shortest path. **1st place in the UnB internal competition.**
I led the electronics team, designed the board schematics in KiCad and wrote the motor and sensor firmware on an ESP32 with ESP-IDF. Live telemetry goes over Wi-Fi to a web dashboard.

[Repository](https://github.com/Arthurpmarinho/2026_1_PI1_Grupo02_Hilmer) · [8x8 maze run](https://youtu.be/1a2v_xoSXcU) · [How it works](https://youtu.be/TcLgV6eDGfE)

## Projects

<!-- PORTFOLIO:START -->
| Project | What it is | Stack |
| --- | --- | --- |
| [Capital Rocket Team avionics](https://github.com/Arthurpmarinho/capital-rocket-team-avionics) | Flight avionics boards for the Boscov hybrid rocket: valve control and parachute deployment (CRM) and GPS/IMU LoRa telemetry (GNM). 1st place in the hybrid category at LASC 2025 | EasyEDA Pro, ESP32, LoRa, I2C, SPI |
| [Micromouse](https://github.com/Arthurpmarinho/2026_1_PI1_Grupo02_Hilmer) | Autonomous maze-solving robot. I led the electronics, designed the KiCad board schematics and wrote the motor and sensor firmware on ESP32. 1st place in the UnB internal competition | ESP32, ESP-IDF, C++, KiCad, FastAPI, React |
| [Bluetooth elevator controller](https://github.com/Arthurpmarinho/Trabalho-final-Eletronica-Embarcada) | 4-floor elevator on PIC16F1827 with SCAN scheduling, PWM motor control and Bluetooth UART telemetry | PIC, C, UART, PWM |
| [Magic Screen (telecran, FPGA)](https://github.com/anauehara/FPGA_TP_2026.02) | Magic Screen: Etch-A-Sketch style drawing toy on a DE10-Nano. Debounced quadrature encoders move a cursor, a dual-port RAM framebuffer stores the drawing, and it is streamed out over HDMI. ENSEA FPGA lab, with Ana Carolina | VHDL, ModelSim, Quartus, HDMI, DE10-Nano |
| [VHDL labs (ENSEA)](https://github.com/Arthurpmarinho/FPGA_ENSEA) | VHDL modules with testbenches: ALU, HDMI timing controller, counter, shift register. GHDL CI | VHDL, ModelSim, Quartus, GHDL |
<!-- PORTFOLIO:END -->

## Experience

- **BMS for an electric bus**, UnB research with Mercedes-Benz. Voltage and current acquisition circuit with LTC6811 and INA260, validated on a Li-ion pack, data processed in MATLAB and Simulink.
- **Constant current regulator firmware**, internship at LEDS. C on ESP32 with ESP-IDF and FreeRTOS, RS-485 Modbus RTU link, validated on the bench.
- **Capital Rocket Team**. [Avionics boards](https://github.com/Arthurpmarinho/capital-rocket-team-avionics) for a hybrid rocket and its ground station. The team won the hybrid rocket category at LASC 2025.
- **Motor vibration monitoring**, UnB with Eldorado and Rossi. Python acquisition software over Modbus RTU with FFT and ISO 10816 diagnostics, deployed on 20 motors.
- **SLAM with LiDAR** at ENSEA, in progress.

## Tools

| Area | Tools |
| --- | --- |
| Embedded | ESP32, ESP-IDF, FreeRTOS, PIC, FPGA |
| Languages | C, C++, Python, VHDL |
| Interfaces | I2C, SPI, UART, RS-485 Modbus RTU |
| Hardware and simulation | KiCad, EasyEDA, LTspice, MATLAB/Simulink, ModelSim, Quartus |

Portuguese native · English C1 · Spanish B1 · French A2

## Recently updated

<!-- RECENT:START -->
- [Capital Rocket Team avionics](https://github.com/Arthurpmarinho/capital-rocket-team-avionics), updated 2026-11-16
- [VHDL labs (ENSEA)](https://github.com/Arthurpmarinho/FPGA_ENSEA), updated 2026-11-15
- [Bluetooth elevator controller](https://github.com/Arthurpmarinho/Trabalho-final-Eletronica-Embarcada), updated 2026-10-31
<!-- RECENT:END -->

## Coursework

<!-- COURSEWORK:START -->
| Project | What it is | Stack |
| --- | --- | --- |
| [Café loyalty system (OOP final project)](https://github.com/Arthurpmarinho/Trabalho_final_OO_2026-1) | Sales and loyalty program for a themed café, object-oriented design in Java. UnB 2026/1 | Java |
| [Embedded Electronics labs (PIC)](https://github.com/Arthurpmarinho/Embarcado_2025_02) | Lab exercises on PIC microcontrollers in MPLAB X. UnB Embedded Electronics 2025/2 | PIC, C, MPLAB X |
| [Digital systems labs (VHDL, Vivado)](https://github.com/Arthurpmarinho/ted_ped_2_2024_02) | FPGA labs in Vivado: state machines, counters, 7-segment display, PicoBlaze. UnB 2024/2 | VHDL, Vivado |
<!-- COURSEWORK:END -->
