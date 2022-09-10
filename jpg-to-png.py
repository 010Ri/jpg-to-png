import os
import glob
from PIL import Image

images = glob.glob('/Users/user/Desktop/img/*.jpg')
for image in images:
    file_name = os.path.splitext(os.path.basename(image))[0]
    target = Image.open(image)
    target.save('/Users/user/Desktop/pngs/' + file_name + '.png')
