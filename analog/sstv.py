from PIL import Image
import pysstv.grayscale
import pysstv.color

#you can run .write_wav("file location") on what these functions return
#you need to pass these functions a PIL image.

def Robot36(image):
	image.thumbnail((320, 256)) #downsizes the image
	newbg = Image.new('RGB', (320, 256)) #make a new image
	print(f"Image is {image.width} by {image.height}")
	imgwidth = image.width
	imgheight = image.height
	newbg.paste(image, (160-(imgwidth//2), (128-(imgheight//2)))) #paste image ontop of the new one
	audio = pysstv.color.Robot36(newbg, 44100, 16)
	return audio

def PD120(image):
	image.thumbnail((640, 496)) #downsizes the image
	newbg = Image.new('RGB', (640, 496)) #make a new image
	print(f"Image is {image.width} by {image.height}")
	imgwidth = image.width
	imgheight = image.height
	newbg.paste(image, (320-(imgwidth//2), (248-(imgheight//2)))) #paste image ontop of the new one
	audio = pysstv.color.PD120(newbg, 44100, 16) #note: it doesn't respect the sample rate for some reason. If decoding doesn't work, try 48000
	return audio

def gray8(image):
	image.thumbnail((160, 120)) #downsizes the image
	newbg = Image.new('RGB', (160, 120)) #make a new image
	print(f"Image is {image.width} by {image.height}")
	imgwidth = image.width
	imgheight = image.height
	newbg.paste(image, (80-(imgwidth//2), (60-(imgheight//2)))) #paste image ontop of the new one
	audio = pysstv.grayscale.Robot8BW(newbg, 44100, 16) #note: it doesn't respect the sample rate for some reason. If decoding doesn't work, try 48000
	return audio
