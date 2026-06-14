import cv2
import PIL.Image as Image
cam = cv2.VideoCapture(0) #index may need to be changed depending on hardware setup
ret, frame = cam.read()
colorconverted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
pilImageType = Image.fromarray(colorconverted)

def get_chunk(tlx, tly): #tlx = top left x, tly = top left y
	x = 0
	y = 0
	for x in range(20):
		for y in range(20):
			

for x in range(pilImageType.width):
	for y in range(pilImageType.height):
		pixel = pilImageType.getpixel((x, y))
#		print(str(pixel))
