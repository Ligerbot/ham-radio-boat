# When compassandgps.ino is running on the arduino, and the arduno is connected to the rPi via USB cable, this program has the rPi print what the arduino outputs through serial.print

import serial, time

ser = serial.Serial('COM0', 115200, timeout=5)

start = time.time()
while time.time() - start < 60:
    print(ser.readline().decode(errors='ignore').strip())
ser.close()
