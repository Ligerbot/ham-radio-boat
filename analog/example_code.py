import sstv
import PIL.Image

file = input("Path to file: ")
callsign = input("Callsign: ")
image = PIL.Image.open(file)
out = sstv.Robot36(image, callsign)
out.write_wav("output.wav")
print("Stored to output.wav")
