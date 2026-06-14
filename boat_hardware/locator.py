#credit to Nathan KO6MUM for the serial reader program. I moved around the code to put it into a library that is importable to other scripts

# When compassandgps.ino is running on the arduino, and the arduno is connected to the rPi via USB cable, this program has the rPi print what the arduino outputs through serial.print

import json
import serial, time
start = time.time() #whats this for?

#time might not be necescary here

def update():
	ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5) #ttyACM0 and baud 115200 should be default on the RPI, adjust to whatever is necescary
	serialin = ser.readline().decode()
	print("Got: " + serialin)
	listed = json.loads(serialin) #now you can do listed['lat'] or listed['lon']. 
	print(str(listed))
	#Supported keys are lat, lon, bearing, time, height.
	return listed #return the array


if __name__ == "main":
	exit(0) #so the code below won't run
	while time.time() - start < 60:
		output = ser.readline().decode(errors='ignore').strip() #TODO: simplify this maybe..?
		print(ser.readline().decode(errors='ignore').strip())
	ser.close()
