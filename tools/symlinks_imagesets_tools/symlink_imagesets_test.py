#!/usr/bin/python
#
# This scripts has been used to create symbolic links and files containing imagesets
# in order to use them for testing our systems, avoiding an annoying
# duplication of the dataset.
#
# author: Elisa Maiettini
# date: 06/03/2017
#
import os

#hierarchy = [
#   ....
#   (hlength-7) dataset_dir
#   (hlength-6) images_dir
#   (hlength-5) categoty
#   (hlength-4) instance
#   (hlength-3) transformation
#   (hlength-2) day
#   (hlength-1) camera
#]

#imagesets file declaration (the empty file should already exist)
target_test_file = '5classes_4transf_80-20_test.txt'
target_test_path = os.path.join(os.getcwd(),'ImageSets', target_test_file)

#path for symbolic link creation. The scripts will create the symlinks
#in a folder called iCubWorld-Transformation_tvt placed in the same directory of the original dataset
#If you want to change the creation path overwrite link_path definition
path_to_dir = os.getcwd(),os.pardir
ldir = 'iCubWorld-Transformation_tvt'
link_path = os.path.join(path_to_dir,ldir)

train_images_path = os.path.join(link_path,'train/images')
val_images_path = os.path.join(link_path,'val/images')
test_images_path = os.path.join(link_path,'test/images')

train_labels_path = os.path.join(link_path,'train/labels')
val_labels_path = os.path.join(link_path,'val/labels')
test_labels_path = os.path.join(link_path,'test/labels')

#Images and txt annotations (kitti like) directories from the main folder of the dataset
images_dir = 'Images'
annotations_dir = 'Annotations_txt'

#classes and transformations selection
classes = ['book','flower','glass','hairclip','hairbrush']
transformations = ['MIX']


def info_from_path(filename):
    ## info extraction from path
    hierarchy = filename.split('/')
    hlength = len(hierarchy)
    camera = hierarchy[hlength-1]
    day  = hierarchy[hlength-2]
    pose = hierarchy[hlength-3]
    name = hierarchy[hlength-4]
    category = hierarchy[hlength-5]

    return camera, day, pose, name, category


def write_imageset(view_path):
    camera, day, pose, name, category = info_from_path(view_path)
    folder_from_category = os.path.join(category, name, pose, day, camera)

    target_test = open(target_test_path, 'a')

    counter = 0
    for filename in os.listdir(view_path):
        if filename.endswith('.jpg'):
            imagename = os.path.splitext(os.path.basename(filename))[0]
            img_path_noext = os.path.join(folder_from_category, imagename)
            print img_path_noext

            target_test.write(img_path_noext)
            target_test.write('\n')

            counter = counter+1

def create_link(view_path, view_path_an):
    counter = 0
    camera, day, pose, name, category = info_from_path(view_path)

    for filename in os.listdir(view_path):
        if filename.endswith('.jpg'):
            imagename = os.path.splitext(os.path.basename(filename))[0]
            annotation_file = imagename + '.txt'

            real_file_path = os.path.join(view_path, filename)
            real_file_path_an = os.path.join(view_path_an, annotation_file)

            new_name = name + '_' + pose + '_' + day + '_' + camera + '_' + imagename
            new_image_name = new_name + '.jpg'
            new_annot_name = new_name + '.txt'

            linked_file_path = os.path.join(test_images_path, new_image_name)
            linked_file_path_an = os.path.join(test_labels_path, new_annot_name)
            if not os.path.isfile(linked_file_path):
                os.symlink(real_file_path, linked_file_path)
                os.symlink(real_file_path_an, linked_file_path_an)

            counter = counter+1



if __name__ == '__main__':

    curr_path = os.getcwd()
    images_path = os.path.join(curr_path, images_dir)
    annotations_path = os.path.join(curr_path, annotations_dir)

    #loop on the categories
    for category_dir in os.listdir(images_path):
        if category_dir in classes:
            category_path = os.path.join(images_path, category_dir)
            category_path_an = os.path.join(annotations_path, category_dir)
            if os.path.isdir(category_path):
                #loop on the instances
                for instance_dir in os.listdir(category_path):
                    instance_path = os.path.join(category_path, instance_dir)
                    instance_path_an = os.path.join(category_path_an, instance_dir)
                    if os.path.isdir(instance_path):
                        #loop on the transformations
                        for trans_dir in os.listdir(instance_path):
                            if trans_dir in transformations:
                                trans_path = os.path.join(instance_path, trans_dir)
                                trans_path_an = os.path.join(instance_path_an, trans_dir)
                                if os.path.isdir(trans_path):
                                    #loop on the days
                                    for day_dir in os.listdir(trans_path):
                                        day = day_dir[-1:]
                                        if(int(day)%2==1):
                                            day_path = os.path.join(trans_path, day_dir)
                                            day_path_an = os.path.join(trans_path_an, day_dir)
                                            if os.path.isdir(day_path):
                                                #left and right directories
                                                for view_dir in os.listdir(day_path):
                                                    if(view_dir == 'left'):
                                                        view_path = os.path.join(day_path, view_dir)
                                                        view_path_an = os.path.join(day_path_an, view_dir)
                                                        if os.path.isdir(view_path):
                                                            print view_path
                                                            create_link(view_path,view_path_an) #comment this line to avoid symlinks creation
                                                            write_imageset(view_path)  #comment this line to avoid imagesets files creation
