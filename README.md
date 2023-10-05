# HW2-Socket-Programming-and-Data-Visualization

Group : 9  
Member : B09901043 陳昱樺 B09901134 林容丞

Function
---
Here are what this project does:
1. Read some sensor values of a STM32 development board, including temperature, humidity, pressure, gyroscope, accelerometer, and magnetometer.
2. Send the data to a Linux/Windows/Mac host.
3. Visualize data with GUI tool (Python).

Prerequisites
---
There are three things a user should prepare to run this project:
* Mbed Studio
* STM32 development board
* Python

Usage
---
Here are some steps to run this project properly:
1. Connect STM32 development board to Mbed Studio.
2. Set SSID and password of the user's Internet connection in the file mbed_app.json.
3. Connect the host to the same Internet.
4. Run main.cpp.
5. Now, sensor values of STM32 are being shown in the console of Mbed Studio, and all the data is sent to the host.
6. The host prints the received data in the console.
7. The figure will update once a second.

License
---
None.

Acknowledgements
---
Here are some resources we refer to to finish this project:
* Mbed OS example: DISCO_L475VG_IOT01-Sensors-BSP  
[https://os.mbed.com/teams/ST/code/DISCO_L475VG_IOT01-Sensors-BSP/]
* Mbed OS example: mbed-os-example-sockets  
[https://github.com/ARMmbed/mbed-os-example-sockets]
* Course slides: STM32 IoT node wifi Lab.pdf
