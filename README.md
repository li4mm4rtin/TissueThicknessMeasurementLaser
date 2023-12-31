# Tissue Laser Thickness Measurement

**Author:** Liam Martin

**Last Edit:** September 11, 2023

## Purpose

This Python script is designed to communicate with an Arduino and a laser device (Acuity Laser System) to measure the thickness of a tissue sample. The script provides a straightforward way to collect data on tissue thickness. Before using this script, ensure that the Arduino has been flashed with the LaserThicknessArduino code (typically not needed unless you've made changes to the code). Additionally, specify the serial ports where the Arduino and laser are connected. When the script is run, it will measure the tissue thickness and save the data to a CSV file with a timestamp. This code was written for MacOS. The code will likely work for Windows and Linux but no testing has been conducted to confirm.

## Instructions

1. **Setup:** Plug both the laser and the motor contoller into the wall. Laser will immediately turn on, red light on top of the motor controller will turn on. Plug both USB cords into usb ports on the computer.
2. **Arduino Flashing:** Ensure that your Arduino is flashed with the LaserThicknessArduino code. This is usually done only once unless you make changes to the Arduino code, Translational Research Laboratories in Urogynecology can likely skip this step.
3. **Serial Port Identification:** Identify what ports the USB cords are plugged into. Boxed are the two items that need to be copied into the code in the next step.\
   *MacOS*
   ```terminal
   open terminal
   type "ls /dev/tty.*"
   ```
   *Example MacOS Output*
   ![Alt text](MACOS_output.png?raw=true "Example Terminal Output")
5. **Serial Port Configuration:** Specify the correct serial ports for the Arduino and laser in the script (From step 3):
   ```python
   arduino = serial.Serial('/dev/tty.usbmodem######', 115200)  # Arduino serial port
   laser = serial.Serial('/dev/tty.usbserial-#####', 9600)  # Laser serial port
6. **Travel Distance:** Set the travelDistance_mm variable to the desired travel distance in millimeters. Note that it should by default be negative if using it in the configuration that it was left in (e.g., -12 for a 12mm travel).
7. **Run the Script:** Execute the script in your Python environment. It will communicate with the Arduino and laser to measure tissue thickness. Example usage:
   ```python
   python laserThickness.py
8. **Data Output:** The script will save the measurement data to a CSV file with a timestamp in the filename, such as data_[month-day-year_hour-minute-second].csv.

## License
This script is provided under the MIT License. You are free to modify and distribute it as needed. Please refer to the LICENSE file for details.
