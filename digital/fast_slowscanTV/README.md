# Very fast slow scan digital TV

## (a dumb idea that probably will never work)

In this directory is my progress on very fast slow scan digital tv (vfssdtv). The goal for this is maybe a few fps of a low (very low) resolution image. The main issue is that I can't get the images through fast enough using FSK. 1200 baud can get an image through in maybe 15 seconds but that doesn't include error correction. FSK will not work for this. A better encoding would be QAM or MFSK. Maybe I will work on that for vfssdtv.

## Don't do the following

Attempt to send an image with low resolution and hardly and color depth over a 1200 baud connection in hopes of having something faster than robot36.

Expect an image with only red, orange, yellow, green, blue, white, and black that is 20 pixels by 20 pixels to not look like static.

Try to make any of the stuff in this folder actually work as intended.
