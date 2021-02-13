from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('flower1.png')) 
hash1 = imagehash.average_hash(Image.open('flower2.png')) 
cutoff = 5

if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')
