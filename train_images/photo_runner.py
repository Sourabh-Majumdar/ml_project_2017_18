import os
import glob
os.chdir('.')

for img_file in glob.glob("*.png") :
	print(img_file)
	img_file_components = img_file.split('_')
	print(type(img_file))
	print(img_file_components)
	final_components = img_file_components[3:]
	if len(final_components) == 0:
		continue
		pass
	print(" final components selected are ")
	print(final_components)
	print(type(final_components))
	last_component = final_components[-1]



