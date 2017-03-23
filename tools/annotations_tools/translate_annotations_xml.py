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
    xmin = data[6]
    ymin = data[7]
    xmax = str(int(xmin)+int(data[8]))
    ymax = str(int(ymin)+int(data[9]))
    return data, complete_name, img_name, im_t, bb_t, bb_cx, bb_cy, bbpxN, xmin, ymin, xmax, ymax

def convert_annotations_xml(filename):

    dataset_dir, images_dir, camera, day, pose, name, category = info_from_path(filename)
    folder_from_category = os.path.join(category, name, pose, day, camera)
    path_to_annotations_dir = os.path.join('Annotations_xml', folder_from_category)

    if not os.path.exists(path_to_annotations_dir):
        os.makedirs(path_to_annotations_dir)

    source = open(filename,'r')
    for line in source:

        data, complete_name, img_name, im_t, bb_t, bb_cx, bb_cy, bbpxN, xmin, ymin, xmax, ymax = info_from_line(line)

        target_file = img_name + '.xml'
        target_path = os.path.join(path_to_annotations_dir, target_file)
        target = open(target_path, 'w')

        target.write('<annotation>')

        target.write('\n\t<folder>')
        target.write(folder_from_category)
        target.write('</folder>')

        target.write('\n\t<filename>')
        target.write(img_name)
        target.write('</filename>')

        target.write('\n\t<source>')

        target.write('\n\t\t<database>iCubWorld-Transformation</database>')

        target.write('\n\t</source>')

        target.write('\n\t<size>')

        target.write('\n\t\t<width>640</width>')

        target.write('\n\t\t<height>480</height>')

        target.write('\n\t\t<depth>3</depth>')

        target.write('\n\t</size>')

        target.write('\n\t<segmented>0</segmented>')

        target.write('\n\t<imgtstamp>')
        target.write(im_t)
        target.write('</imgtstamp>')

        target.write('\n\t<day>')
        target.write(day)
        target.write('</day>')

        target.write('\n\t<camera>')
        target.write(camera)
        target.write('</camera>')

        target.write('\n\t<object>')

        target.write('\n\t\t<category>')
        target.write(category)
        target.write('</category>')

        target.write('\n\t\t<name>')
        target.write(name)
        target.write('</name>')

        target.write('\n\t\t<pose>')
        target.write(pose)
        target.write('</pose>')

        target.write('\n\t\t<truncated>0</truncated>')

        target.write('\n\t\t<difficult>0</difficult>')

        target.write('\n\t\t<bndbox>')

        target.write('\n\t\t\t<xmin>')
        target.write(xmin)
        target.write('</xmin>')

        target.write('\n\t\t\t<ymin>')
        target.write(ymin)
        target.write('</ymin>')

        target.write('\n\t\t\t<xmax>')
        target.write(xmax)
        target.write('</xmax>')

        target.write('\n\t\t\t<ymax>')
        target.write(ymax)
        target.write('</ymax>')

        target.write('\n\t\t</bndbox>')

        target.write('\n\t\t<bbtstamp>')
        target.write(bb_t)
        target.write('</bbtstamp>')

        target.write('\n\t\t<xcentroid>')
        target.write(bb_cx)
        target.write('</xcentroid>')

        target.write('\n\t\t<ycentroid>')
        target.write(bb_cy)
        target.write('</ycentroid>')

        target.write('\n\t\t<blobpixels>')
        target.write(bbpxN)
        target.write('</blobpixels>')

        target.write('\n\t</object>')

        target.write('\n</annotation>')
