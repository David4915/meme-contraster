
# Third party modules
import numpy
from PIL import Image


def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values


image = get_image("data1.jpg")

blackandwhite = []

for x in range(image.shape[0]):
    blackandwhite.append([])
    for y in range(image.shape[1]):
        a = 0
        for i in range(3):
            a+=(image[x][y][i])
        a = int(a/3)
        b = [a,a,a]
        blackandwhite[x].append(b)
print(blackandwhite)        




























