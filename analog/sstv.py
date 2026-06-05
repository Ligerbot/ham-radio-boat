from PIL import Image
from PIL import ImageDraw, ImageFont
import pysstv.grayscale
import pysstv.color

#you can run .write_wav("file location") on what these functions return
#you need to pass these functions a PIL image.

def image_monkey_buisness(image, callsign, w, h):
	image.thumbnail((w, h)) #downsizes the image
	newbg = Image.new('RGB', (w, h)) #make a new image
	print(f"Image is {image.width} by {image.height}")
	imgwidth = image.width
	imgheight = image.height
	newbg.paste(image, ((w//2)-(imgwidth//2), ((h//2)-(imgheight//2)))) #paste image ontop of the new one
	txtoverlay = ImageDraw.Draw(newbg)
	txtoverlay.text((5, -7), str(callsign), fill=(255, 255, 255), font=ImageFont.load_default(size=30), stroke_width=1, stroke_fill=(0, 0, 0))
	return newbg

def Robot36(image, callsign):
	newbg = image_monkey_buisness(image, callsign, 320, 256)
	audio = pysstv.color.Robot36(newbg, 44100, 16)
	return audio

def PD120(image, callsign):
	newbg = image_monkey_buisness(image, callsign, 640, 496)
	audio = pysstv.color.PD120(newbg, 44100, 16) #note: it doesn't respect the sample rate for some reason. If decoding doesn't work, try 48000
	return audio

def gray8(image, callsign):
	newbg = image_monkey_buisness(image, callsign, 160, 120)
	audio = pysstv.grayscale.Robot8BW(newbg, 44100, 16) #note: it doesn't respect the sample rate for some reason. If decoding doesn't work, try 48000
	return audio
