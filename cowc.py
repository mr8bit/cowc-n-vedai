import os
from PIL import Image
import numpy as np
import xml.etree.cElementTree as ET
Image.MAX_IMAGE_PIXELS = 1000000000

def get_original_name(file):
    name = file.split('.')[0].split('_')[0]
    extention = file.split('.')[1]
    return name, extention

def create_xml_file(file_original,file_annotation):
    count= 0
    full_path_to_image = os.path.abspath('images/{0}.png'.format(file_original))
    annotadet = np.array(Image.open('annotations/cowc/{0}'.format(file_annotation)))
    annotation = ET.Element("annotation", verified="yes")
    folder = ET.SubElement(annotation, "folder").text = 'images'
    filename = ET.SubElement(annotation, "filename").text = '{0}.{1}'.format(file_original,'png')
    path = ET.SubElement(annotation, "path").text = '{0}'.format(full_path_to_image)
    source = ET.SubElement(annotation, "source")
    database = ET.SubElement(source, "database").text = 'Unknown'
    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width').text = '2220'
    height = ET.SubElement(size, 'height').text = '2220'
    depth = ET.SubElement(size, 'depth').text = '3'
    segmented = ET.SubElement(annotation, 'segmented').text = '0'
    for y in range(len(annotadet)):
        for x in range(len(annotadet)):
            if 255 in  annotadet[y][x]:
                object = ET.SubElement(annotation, 'object')
                name = ET.SubElement(object, 'name').text = 'car'
                pose = ET.SubElement(object, 'pose').text = 'Unspecified'
                truncated = ET.SubElement(object, 'truncated').text = '0'
                difficult = ET.SubElement(object, 'difficult').text = '0'
                bndbox = ET.SubElement(object, 'bndbox')
                count +=1
                xmin = ET.SubElement(bndbox, 'xmin').text = '{0}'.format(int(x)-17)
                ymin = ET.SubElement(bndbox, 'ymin').text = '{0}'.format(int(y)-17)
                xmax = ET.SubElement(bndbox, 'xmax').text = '{0}'.format(int(x)+17)
                ymax = ET.SubElement(bndbox, 'ymax').text = '{0}'.format(int(y)+17)
    tree = ET.ElementTree(annotation)
    tree.write("images/{0}.xml".format(file_original))
    print("Count Car: {0}".format(count))

if __name__ == '__main__':
    list = os.listdir('annotations/cowc/')
    for file in list:
        name_orgiginal, extention = get_original_name(file)
        print("Work on: {0}".format(name_orgiginal))
        create_xml_file(name_orgiginal,file)
