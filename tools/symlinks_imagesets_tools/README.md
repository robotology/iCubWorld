## Prerequisites
The scripts expect the dataset to be organized in the following structure:

    |-- iCubWorld-Transformation/
            |-- Images/
                 |-- book/
                 |-- flower/
                 |-- bodylotion/
                 |-- ...
            |-- Imagesets/
            |-- Annotations_txt/
            |-- Annotations_xml/

where `iCubWorld-Transformation` is the main directory, `Images` contains all the categories folders, or a subset (after downloading the different parts of the dataset you should have `cut`+`paste` the different categories folders in `Images`).  
You should `copy`+`paste` the scripts in the `iCubWorld-Transformation` directory to use them.

## ImageSets and symlinks
If you use both the following scripts, you will end up with the following hierarchy:

        |-- path/to/the/dir/to/put/links
            |-- name_of_link_dir/
                |-- test/
                     |-- images/
                     |-- labels/
                |-- train/
                     |-- images/
                     |-- labels/
                |-- val/
                     |-- images/
                     |-- labels/

and/or 3 imagesets files: `iCubWorld-Transformation/ImageSets/validation_imagesets_filename.txt`,  `iCubWorld-Transformation/ImageSets/train_imagesets_filename.txt` and `iCubWorld-Transformation/ImageSets/test_imagesets_filename.txt`, that will point to the subset of the dataset you choose.

#### symlink_imagesets_creation
The script `symlink_imagesets_creation.py` creates symbolic links and/or imagesets files of a subset of the dataset for training and validation. This script:
- will fill two imageset files `iCubWorld-Transformation/ImageSets/validation_imagesets_filename.txt` and `iCubWorld-Transformation/ImageSets/train_imagesets_filename.txt` and/or fill the following hierarchy:

        |-- path/to/the/dir/to/put/links
            |-- name_of_link_dir/
                |-- train/
                     |-- images/
                     |-- labels/
                |-- val/
                     |-- images/
                     |-- labels/

with the subset of the dataset you choose;
- expects the existance of the hierarchy of directories above;
- if you want to create only one of the two you can comment line 159 or 160 in the script following the instructions in the comments;
- [for both] To change the policy of choosing the images for train and val sets you should comment lines from 75 to 82 and from 103 to 118, and replace them with the code for your policy;
- [for both] You can choose the classes and the transformations from which to pick the images. You should specify them at lines 42 and 43;
- [for the imagesets] expects the existance of the files  `iCubWorld-Transformation/ImageSets/validation_imagesets_filename.txt` and `iCubWorld-Transformation/ImageSets/train_imagesets_filename.txt` to write on them the imagesets;
- [for the imagesets] You should choose the name of the files and assign them to the `target_train_file` and `target_val_file` at lines 17 and 18;
- [for the symlinks] you can choose where to put the symbolic links to the dataset, setting the variables `path_to_dir` and `ldir` at lines 28 and 29, respectively to the path to the directory that will contain the links and the directory itself.

#### symlink_imagesets_test
Similarly to the previous script, the script `symlink_imagesets_test.py` creates symbolic links and/or imagesets files of a subset of the dataset for testing. This script:
- will fill an imageset file `iCubWorld-Transformation/ImageSets/test_imagesets_filename.txt` and/or fill the following hierarchy:

        |-- path/to/the/dir/link
            |-- name_of_link_dir/
                    |-- test/
                         |-- images/
                         |-- labels/

with the subset of the dataset you choose;
- expects the existance of the hierarchy of directories above;
- if you want to create only one of the two you can comment line 135 or 136 in the script following the instructions in the comments;
- [for both] To change the policy of choosing the images for test sets you should comment lines 65 and 66 and from 88 to 91, and replace them with the code for your policy;
- [for both] You can choose the classes and the transformations from which to pick the images. You should specify them at lines 35 and 36;
- [for imagesets] expects the existance of the files `iCubWorld-Transformation/ImageSets/test_imagesets_filename.txt`
- [for imagesets] You should choose the name of the file and assign it to the `target_test_file` variable at line 16;
- [for the symlinks] you can choose where to put the symbolic links to the dataset, setting the variables `path_to_dir` and `ldir` at lines 21 and 22, respectively to the path to the directory that will contain the links and the directory itself.
