# iCubWorld scripts
These scripts have been created to let the dataset's usage be easier and more efficient.
- The [first part](../icubworld-t_scritps/annotations_tools/README.md) of the scripts has been used to translate the annotations files given by the robot to more standard formats like the [Imagenet](http://www.image-net.org/)'s or the [KITTI](http://www.cvlibs.net/datasets/kitti/)'s.
- The [second part](../icubworld-t_scritps/symlinks_annotations_tools/README.md) of the scripts has been used to create symbolic links and files containing imagesets in order to use them for training and testing our systems, avoiding an annoying duplication of the dataset.

We think they can be usefull for anyone who wants to annotate personally the dataset adding some fields or use only a subset of the images for personal purposes.

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
