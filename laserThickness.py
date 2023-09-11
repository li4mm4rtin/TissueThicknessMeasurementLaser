# Name: Tissue Laser Thickness Measurement
# Author: Liam Martin
# Last Edit: 9/11/23

# Purpose: This script communicates with an Arduino and laser device to measure the thickness of a tissue sample.
# Ensure the Arduino is flashed with LaserThicknessArduino (should not have to do unless have made edits to the code).
# Specify the ports where the arduino and laser and plugged in to the serial ports. Run this script to measure tissue
# thickness and which saves the data to 'data_[month-day-year_hour-minute-second].csv'.

# Import necessary libraries
import serial
import time
import csv

# EDIT THESE VALUES ONLY. Define the serial ports for Arduino and laser, as well as the travel distance in millimeters
arduino = serial.Serial('/dev/tty.usbmodem147401', 115200)  # Arduino serial port
laser = serial.Serial('/dev/tty.usbserial-14730', 9600)  # Laser serial port
travelDistance_mm = -12  # Travel distance for laser measurement in millimeters, should be negative (bed is 12mm)


# Function to respond with 'pong' when 'ping' is received
def pingPong(data, loc):
    if data == 'ping':
        print('pong', loc)


# Delay to ensure all devices are properly connected
time.sleep(2)

# Constants for converting steps to millimeters and vice versa
CONST_mmPR = 1.0
steps = str(travelDistance_mm / CONST_mmPR * 25000)
rawData = []
elapsed_time = []

# Send the calculated steps to Arduino (Arduino must be flashed with LaserThicknessArduino)
arduino.write(steps.encode())
start_time = time.time()

# Clear any existing data from the serial inputs (may not be necessary)
arduino.flushInput()
laser.flushInput()

pingPong(arduino.readline().decode().strip(), 'connected-beginning measure')

# Loop to measure the thickness of the tissue sample
while not arduino.inWaiting():
    laserHeight = laser.readline().decode().strip()
    rawData.append(float(laserHeight))
    elapsed_time.append(time.time() - start_time)

pingPong(arduino.readline().decode().strip(), 'connected-measure complete')

# Create a CSV file to save the laser data
csv_file = open('data_'+str(time.strftime("%m-%d-%y_%H-%M-%S", time.localtime(time.time()))) + '.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Time (s)', 'Distance Traversed (mm)', 'Raw Data (mm)', 'Thickness (mm)'])
csv_writer.writerow([0.0, 0.0, rawData[0], 0.0])
for i, timePoint in enumerate(elapsed_time[1:]):
    percentTime = timePoint / elapsed_time[-1]
    thickness = max(rawData) - rawData[i]
    csv_writer.writerow([float(elapsed_time[i]), float(-percentTime * travelDistance_mm), rawData[i], thickness])
csv_file.close()

# Calculate and send steps to return the laser to its original position
steps = str(-travelDistance_mm / CONST_mmPR * 25000)
arduino.write(steps.encode())

# Close the serial connections
arduino.close()
laser.close()
