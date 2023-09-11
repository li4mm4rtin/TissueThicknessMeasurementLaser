# Tissue Laser Thickness Measurement

**Author:** Liam Martin

**Last Edit:** September 11, 2023

## Purpose

This Python script is designed to communicate with an Arduino and a laser device to measure the thickness of a tissue sample. The script provides a straightforward way to collect data on tissue thickness. Before using this script, ensure that the Arduino has been flashed with the LaserThicknessArduino code (typically not needed unless you've made changes to the code). Additionally, specify the serial ports where the Arduino and laser are connected. When the script is run, it will measure the tissue thickness and save the data to a CSV file with a timestamp.

## Instructions

1. **Arduino Flashing:** Ensure that your Arduino is flashed with the LaserThicknessArduino code. This is usually done only once unless you make changes to the Arduino code. Translational Research Laboratories in Urogynecology can likely skip this step
2. **Serial Port Configuration:** Specify the correct serial ports for the Arduino and laser in the script (Guide.pdf explains how to find this):
   ```python
   arduino = serial.Serial('/dev/tty.usbmodem147401', 115200)  # Arduino serial port
   laser = serial.Serial('/dev/tty.usbserial-14730', 9600)  # Laser serial port
3. **Travel Distance:** Set the travelDistance_mm variable to the desired travel distance in millimeters. Note that it should be negative if the bed moves down (e.g., -12 for a 12mm downward travel).
4. **Run the Script:** Execute the script in your Python environment. It will communicate with the Arduino and laser to measure tissue thickness. Example usage:
   ```python
   python laser_thickness_measurement.py
6. **Data Output:** The script will save the measurement data to a CSV file with a timestamp in the filename, such as data_[month-day-year_hour-minute-second].csv.
