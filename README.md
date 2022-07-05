# Device for Cleaning a Stand-Alone PV Panel
![contributors](https://img.shields.io/badge/Contributors-MOTAHHIR%20Saad%2C%20KERBOUT%20Jihad%2C%20JOUBITI%20Achraf-blue)


This project is the implementation of the following [patent](https://patentimages.storage.googleapis.com/93/82/17/ef07e9b79573fc/WO2022019735A1.pdf), it presents the inital prototype of an automated device for the cleaning of a photovoltaic panel.

## Overview
The device consists of a roll of flexible transparent film paper that is driven between two cylinders with a motor, a round microfiber brush will be used to ensure effective cleaning. The system uses a small electronic board to automatically turn on the motor.
![image](https://user-images.githubusercontent.com/104909670/175542044-dbcd54f2-5720-4575-9115-442805606951.png)

Some of the advantages of using this particular method of cleaning instead of traditional methods such as the cleaning robot that glides along the surface are:
- Reducing water consumption and overall cost
- Faster execution speed
- Power can be provided directly from the panel
- Eliminates unnecessary shadows caused by the robot arm as well as unnecessary strain on the surface, thus extending the longevity of the PV panel

## Initial prototype

![image](https://user-images.githubusercontent.com/104909670/175544868-d23b3f3c-443c-4f05-ac86-9ce1562b4c27.png)

- The coupler and the housings of pillow bearings have been 3D printed, and their purpose is to transmit the rotating movement from the stepper motor to the cylinder as well as to eliminate unnecessary friction, thus allowing the PFA transparent film paper (which is yet to be added to this prototype), to smoothly glide over the two cylinders.
- This prototype also includes a Pi Camera to detect dust on the surface of the panel, with the parts being 3D printed. However, it should be noted that a dust sensor would be a much better alternative and would make the system more reliable.
![image](https://user-images.githubusercontent.com/104909670/175546167-e0917bbd-41c6-43fb-9b59-4ad036a4ec5e.png)
- For this prototype, a Raspberry Pi 3 will be used for the control of this system. Nevertheless, smaller boards like ESP32 or Pyboard are more suitable as well as cheaper alternatives, we'll thus include code in Python for the Raspberry and MicroPython for the ESP32/Pyboard in this repository.
- The major electronic components used are:
![image](https://user-images.githubusercontent.com/104909670/175548463-8444f5e3-caf1-4cca-8b74-e9e2c51aa216.png)
- The Raspberry Pi carries out the following tasks in this specific order:
  - Checking current weather conditions
  - Taking image of the surface of the PV panel, using image processing techniques for dust detection.
    - If panel is "clean", turn Green LED.
    - Else, turn on Stepper Motor and Pump simultaneously for a pre-determined number of steps.

- The libraries used and initial setup on the Raspberry Pi:
![image](https://user-images.githubusercontent.com/104909670/175552228-cc0edcfc-2238-478d-8edf-395a6db231b0.png)

## Requirements
- To install Micropython on ESP32: https://pythonforundergradengineers.com/how-to-install-micropython-on-an-esp32.html
- Library used to access the file system on ESP32: https://github.com/wendlers/mpfshell


## Contributing
Pull requests are welcome.
