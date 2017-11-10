import os
import glob
import re
os.chdir('.')

for img_file in glob.glob("*.png") :
	print(img_file)
	#img_file_components = img_file.split('_')
	img_file_components = re.findall(r'\d+',img_file)
	print(type(img_file))
	print(img_file_components)
	final_components = img_file_components[3:]
	if len(final_components) == 0:
		continue
		pass
	print(" final components selected are ")
	print(final_components)
	print(type(final_components))
	y_values = list(map(int,final_components))
	print(" The y_values are ")
	print(y_values)




