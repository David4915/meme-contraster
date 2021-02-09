from PIL import Image

im = Image.open('redandgreen.png')
pix = im.load()
print(im.size)
print(pix[1,1])
print(pix[260,260])
