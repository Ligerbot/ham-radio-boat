import numpy
import cv2
import PIL.Image as Image
cam = cv2.VideoCapture(0) #index may need to be changed depending on hardware setup
ret, frame = cam.read()
colorconverted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
pilImageType = Image.fromarray(colorconverted)

def get_chunk(tlx, tly): #tlx = top left x, tly = top left y
	x = 0
	y = 0
	red = []
	green = []
	blue = []
	for x in range(20):
		for y in range(20):
			r, g, b = pilImageType.getpixel((x,y))
			red.append(r)
			green.append(g)
			blue.append(b)
	avgred = numpy.average(r)
	avggreen = numpy.average(g)
	avgblue = numpy.average(b)
	return (avgred, avggreen, avgblue)

x = 0
y = 0
px = 0
py = 0

pixelated = Image.new("RGB", (20, 20))
while x <= (pilImageType.width // 20) - (pilImageType.width % 20):
	while y <= (pilImageType.height // 20) - (pilImageType.height % 20):
		getchunk(x, y)
		y = y + 20

for x in range(pilImageType.width):
	for y in range(pilImageType.height):
		get_chunk(x, y)
		
#		pixel = pilImageType.getpixel((x, y))
#		print(str(pixel))
