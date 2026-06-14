# boat hardware stuff

The c++ code for the arduino and any code that manages hardware belongs here.

To get the latitude, longitude, time, bearing, or something else run the following example:

```python3

import locator.py as locator #(or boat_hardware.locator) if in top level directory. the "as locator" part is not necescary if in the boat_hardware directory
list = locator.update()
print("Latitude: " + list['lat'])
print("Longitude: " + list['lon'])
print("Time: " + list['time'])
print("Bearing: " + list['bearing'])
print("Height: " + list['height'])

```

Note: I moved the arduino projects to `/boat_hardware/arduino/`
