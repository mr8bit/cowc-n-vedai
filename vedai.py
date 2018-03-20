# 1: car, 2:trucks, 4: tractors, 5: camping cars, 7: motorcycles, 8:buses, 9: vans, 10: others, 11: pickup, 23: boats , 201: Small Land Vehicles, 31: Large land Vehicles

import os
import pandas as pd
import xml.etree.cElementTree as ET

COUNT_OBJECT = 0
COUNT_CAR = 0
COUNT_PLANE = 0
COUNT_TRUCK = 0
COUNT_PICKUP = 0
def update_annotations(filename):
	data = pd.read_csv('annotations/vedai/' + filename, sep=' ', index_col=None, header=None, names=['x_center', 'y_center', 'orientation', 'class', 'is_contained', 'is_occluded', 'corner1_x', 'corner2_x', 'corner3_x', 'corner4_x', 'corner1_y', 'corner2_y', 'corner3_y', 'corner4_y'])
	imagename = filename.split('.')[0]
	full_path_to_image = os.path.abspath('images/{0}.png'.format(imagename))
	print('Work on: {0}'.format(imagename))
	annotation = ET.Element("annotation", verified="yes")
	folder = ET.SubElement(annotation, "folder").text = 'images'
	filename = ET.SubElement(annotation, "filename").text = '{0}.{1}'.format(imagename,'jpg')
	path = ET.SubElement(annotation, "path").text = '{0}'.format(full_path_to_image)
	source = ET.SubElement(annotation, "source")
	database = ET.SubElement(source, "database").text = 'Unknown'
	size = ET.SubElement(annotation, 'size')
	width = ET.SubElement(size, 'width').text = '1024'
	height = ET.SubElement(size, 'height').text = '1024'
	depth = ET.SubElement(size, 'depth').text = '3'
	segmented = ET.SubElement(annotation, 'segmented').text = '0'
	x = []
	y = []
	global COUNT_OBJECT
	global COUNT_CAR
	global COUNT_PLANE
	global COUNT_TRUCK
	global COUNT_PICKUP
	for row in range(len(data)):
		object = ET.SubElement(annotation, 'object')
		if data.iloc[row]['class'] == 1:
			name = ET.SubElement(object, 'name').text = 'car'
			COUNT_CAR += 1
		elif data.iloc[row]['class'] == 2:
			name = ET.SubElement(object, 'name').text = 'truck'
			COUNT_TRUCK += 1
		elif data.iloc[row]['class'] == 11:
			name = ET.SubElement(object, 'name').text = 'pickup'
			COUNT_PICKUP += 1
		elif data.iloc[row]['class'] == 4:
			name = ET.SubElement(object, 'name').text = 'tractor'
		elif data.iloc[row]['class'] == 5:
			name = ET.SubElement(object, 'name').text = 'camping car'
		elif data.iloc[row]['class'] == 6:
			name = ET.SubElement(object, 'name').text = 'boat'
		elif data.iloc[row]['class'] == 7:
			name = ET.SubElement(object, 'name').text = 'motorcycle'
		elif data.iloc[row]['class'] == 8:
			name = ET.SubElement(object, 'name').text = 'bus'
		elif data.iloc[row]['class'] == 9:
			name = ET.SubElement(object, 'name').text = 'van'
		elif data.iloc[row]['class'] == 10:
			name = ET.SubElement(object, 'name').text = 'other'
		elif data.iloc[row]['class'] == 11:
			name = ET.SubElement(object, 'name').text = 'car'
			COUNT_CAR += 1
		elif data.iloc[row]['class'] == 12:
			name = ET.SubElement(object, 'name').text = 'large'
			COUNT_CAR += 1
		elif data.iloc[row]['class'] == 31:
			name = ET.SubElement(object, 'name').text = 'plane'
			COUNT_PLANE += 1
		elif data.iloc[row]['class'] == 23:
			name = ET.SubElement(object, 'name').text = 'boat'
		pose = ET.SubElement(object, 'pose').text = 'Unspecified'
		truncated = ET.SubElement(object, 'truncated').text = '0'
		difficult = ET.SubElement(object, 'difficult').text = '0'
		bndbox = ET.SubElement(object, 'bndbox')
		try:
			COUNT_OBJECT += 1
			x.append(int(data.iloc[row]['corner1_x']))
			x.append(int(data.iloc[row]['corner2_x']))
			x.append(int(data.iloc[row]['corner3_x']))
			x.append(int(data.iloc[row]['corner4_x']))
			x.sort()
			y.append(int(data.iloc[row]['corner1_y']))
			y.append(int(data.iloc[row]['corner2_y']))
			y.append(int(data.iloc[row]['corner3_y']))
			y.append(int(data.iloc[row]['corner4_y']))
			y.sort()
			xmin = ET.SubElement(bndbox, 'xmin').text = '{0}'.format(x[0])
			ymin = ET.SubElement(bndbox, 'ymin').text = '{0}'.format(y[0])
			xmax = ET.SubElement(bndbox, 'xmax').text = '{0}'.format(x[-1])
			ymax = ET.SubElement(bndbox, 'ymax').text = '{0}'.format(y[-1])
			x = []
			y = []
		except ValueError as e:
			pass
	tree = ET.ElementTree(annotation)
	tree.write("images/{0}.xml".format(imagename))


if __name__ == '__main__':
	list = os.listdir('annotations/vedai/')
	for filename in list:
		# print(filename)
		update_annotations(filename)
	print("Dataset generate XML DONE!")
	print("Count Car:{0}".format(COUNT_CAR))
	print("Count Plane:{0}".format(COUNT_PLANE))
	print("Count Truck:{0}".format(COUNT_TRUCK))
	print("Count Pickup:{0}".format(COUNT_PICKUP))
	print("All count object: {0}".format(COUNT_OBJECT))
