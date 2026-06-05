from PIL import Image
import sstv
#import pysstv.color

image = Image.open("input.png") #temporary until we get a camera
#pd90 is 320 by 256
#i would do robot36 but it doesn't work welll with pysstv
#the following code handles adding black bars to the side

#image.thumbnail((640, 496)) #downsizes the image

#newbg = Image.new('RGB', (640, 496)) #make a new image
#print(f"Image is {image.width} by {image.height}")
#imgwidth = image.width
#imgheight = image.height
#newbg.paste(image, (320-(imgwidth//2), (248-(imgheight//2)))) #paste image ontop of the new one

#newbg.show()

#audio = pysstv.color.PD120(newbg, 44100, 16) #note: it doesn't respect the sample rate for some reason. If decoding doesn't work, try 48000
#print(dir(audio))

#audio = sstv.Robot36(image, "KO6MUM")
#audio = sstv.gray8(image, "KO6MUM")
audio = sstv.PD120(image, "KO6MUM")
audio.write_wav("temporary_output.wav")
