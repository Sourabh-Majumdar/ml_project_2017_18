#dovahkhiin
import numpy as np
from skimage.io import imread, imsave
import os

height = []
width = []
directory = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(directory):
	"""if filename.startswith("mono"):
		continue
	else:"""
	if filename.endswith(".png"):
		#print(os.path.join(directory, filename))
		image = imread(filename,as_grey=True)
		#imsave('mono-'+filename,image)
		a, b = image.shape
		height.append(a)
		width.append(b) 
		continue
	else:
		continue

print(max(height),max(width))
#print(height)