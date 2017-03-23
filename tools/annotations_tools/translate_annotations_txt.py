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
import numpy as np
import cv2

#hierarchy = [
#   ....
#   (hlength-8) dataset_dir
#   (hlength-7) images_dir
#   (hlength-6) categoty
#   (hlength-5) instance
#   (hlength-4) transformation
#   (hlength-3) day
#   (hlength-2) camera
#   (hlength-1) filename
#]
#data = [
#   (0) name.png
#   (1) img_t = image  timestamp
#   (2) bb_t = bndbox timestamp
#   (3) bb_cx = x of bb centroid
#   (4) bb_cy = y of bb centroid
#   (5) bbpxN = num pixels of seg blob
#   (6) bb_tlx = x top-left corner
#   (7) bb_tly = y top-left corner
#   (8) bb_w = bb width
#   (9) bb_h = bb height
#]

def info_from_path(filename):
    ## info extraction from path
    hierarchy = filename.split('/')
    hlength = len(hierarchy)
    camera = hierarchy[hlength-2]
    day  = hierarchy[hlength-3]
    pose = hierarchy[hlength-4]
    name = hierarchy[hlength-5]
    category = hierarchy[hlength-6]
    images_dir = hierarchy[hlength-7]
    dataset_dir = hierarchy[hlength-8]
    return dataset_dir, images_dir, camera, day, pose, name, category

def info_from_line(line):
    data = line.split()
    complete_name = data[0]
    img_name = (complete_name.split('.'))[0]
    im_t = data[1]
    bb_t = data[2]
    bb_cx = data[3]
    bb_cy = data[4]
    bbpxN = data[5]
    bb_tlx = data[6]
    bb_tly = data[7]
    bb_brx = str(int(bb_tlx)+int(data[8]))
    bb_bry = str(int(bb_tly)+int(data[9]))
    return data, complete_name, img_name, im_t, bb_t, bb_cx, bb_cy, bbpxN, bb_tlx, bb_tly, bb_brx, bb_bry

def convert_annotations_txt(filename):

    dataset_dir, images_dir, camera, day, pose, name, category = info_from_path(filename)
    folder_from_category = os.path.join(category, name, pose, day, camera)
    path_to_annotations_dir = os.path.join('Annotations_txt', folder_from_category)

    if not os.path.exists(path_to_annotations_dir):
        os.makedirs(path_to_annotations_dir)

    source = open(filename,'r')
    for line in source:

        data, complete_name, img_name, im_t, bb_t, bb_cx, bb_cy, bbpxN, bb_tlx, bb_tly, bb_brx, bb_bry = info_from_line(line)

        target_file = img_name + '.txt'
        target_path = os.path.join(path_to_annotations_dir, target_file)
        target = open(target_path, 'w')

        #instance
        target.write(name)
        target.write(' ')

        #truncated
        target.write('-1 ')

        #occluded
        target.write('-1 ')

        #alpha: Observation angle of object, ranging [-pi..pi]
        target.write('-10 ')

        #bbox
        target.write(bb_tlx)
        target.write(' ')
        target.write(bb_tly)
        target.write(' ')
        target.write(bb_brx)
        target.write(' ')
        target.write(bb_bry)
        target.write(' ')

        #3D object dimensions: height, width, length (in meters)
        target.write('-1 ')
        target.write('-1 ')
        target.write('-1 ')

        #3D object location x,y,z in camera coordinates (in meters)
        target.write('-1000 ')
        target.write('-1000 ')
        target.write('-1000 ')

        #Rotation ry around Y-axis in camera coordinates [-pi..pi]
        target.write('-10 ')

        #optional score Only for results: Float, indicating confidence
        #in detection, needed for p/r curves, higher is better.
