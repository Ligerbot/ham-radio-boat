import fsk
import PIL.Image as Image
import numpy as np

#the following code was made with help by claude

COLORS = [
    (128, 128, 128),  # gray
    (139, 69, 19),    # brown
    (255, 0, 0),    # red
    (255, 165, 0),  # orange
    (255, 255, 0),  # yellow
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (255, 255, 255),# white
    (0, 0, 0),      # black
]

colornames = [
    ("gray", "a"),
    ("brown", "b"),
    ("red", "c"),
    ("orange", "d"),
    ("yellow", "e"),
    ("green", "f"),
    ("blue", "g"),
    ("white", "h"),
    ("black", "i")

]

def nearest_color(pixel):
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
#    r, g, b = pixel
    # weighted distance — human eyes are more sensitive to green
    return min(COLORS, key=lambda c: (
        2 * (c[0]-r)**2 +
        4 * (c[1]-g)**2 +
        3 * (c[2]-b)**2
    ))

img = Image.open("input.png").convert("RGB")

w, h = img.size
size = min(w, h)
left = (w - size) // 2
top = (h - size) // 2
img = img.crop((left, top, left + size, top + size))


img = img.resize((45, 45), Image.LANCZOS)

pixels = np.array(img)
result = np.array([[nearest_color(pixel) for pixel in row] for row in pixels], dtype=np.uint8)

out = Image.fromarray(result)
out = out.resize((640, 640), Image.NEAREST)
out.show()
i = 0
codes = []
for x in range(out.width):
	for y in range(out.height):
		pixel = out.getpixel((x, y))
		i = COLORS.index(pixel)
		name, code = colornames[i]
#		print(name)
		codes.append(code)
#print(codes)
newcodes = ""
for newcode in codes:
	newcodes = newcodes + newcode
print(newcodes)
fsk.send_text(newcodes, 2400)
