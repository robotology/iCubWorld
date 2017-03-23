#!/usr/bin/python
#
# The script has been used to translate the annotations files given by the robot to more
# standard formats like the [Imagenet](http://www.image-net.org/)'s or the
# [KITTI](http://www.cvlibs.net/datasets/kitti/)'s.
#
# author: Elisa Maiettini
# date: 06/03/2017
#

import os
import translate_annotations_xml as ta_xml
import translate_annotations_txt as ta_txt


curr_path = os.getcwd()
images_dir = 'Images' #cartella che contiene le sotto cartelle con le categories
images_path = os.path.join(curr_path, images_dir)
#loop on the categories
for category_dir in os.listdir(images_path):
    category_path = os.path.join(images_path, category_dir)
    if os.path.isdir(category_path):
        #loop on the instances
        for instance_dir in os.listdir(category_path):
            instance_path = os.path.join(category_path, instance_dir)
            if os.path.isdir(instance_path):
                #loop on the transformations
                for trans_dir in os.listdir(instance_path):
                    trans_path = os.path.join(instance_path, trans_dir)
                    if os.path.isdir(trans_path):
                        #loop on the days
                        for day_dir in os.listdir(trans_path):
                            day_path = os.path.join(trans_path, day_dir)
                            if os.path.isdir(day_path):
                                    #left and right directories
                                    for view_dir in os.listdir(day_path):
                                        #comment the following line if you want to consider also the images from the right camera
                                        if(view_dir == 'left'):
                                            view_path = os.path.join(day_path, view_dir)
                                            if os.path.isdir(view_path):
                                                #info_filename is the name of the file with the informations from the robot
                                                info_filename = os.path.join(view_path, 'img_info.txt')
                                                print info_filename
                                                ta_xml.convert_annotations_xml(info_filename) #comment this line if you don't want the xml annotations
                                                ta_txt.convert_annotations_txt(info_filename) #comment this line if you don't want the txt annotations




# for filename in os.listdir(directory):
#     if filename.endswith(".jpg"):
#         print(os.path.join(directory, filename))
#         continue
#     else:
#         continue
