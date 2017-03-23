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

## Annotations
#### write_annotationts
The script `write_annotationts.py` convert the annotations files given by the robot to more standard formats. For each image `Images/hierarchy/to/the/image/image_name.jpg` it will create an XML file `Annotations_xml/hierarchy/to/the/image/image_name.xml` and a txt file `Annotations_txt/hierarchy/to/the/image/image_name.txt`. Please go to **link** to look at the format of the annotations.
The script:
- expects the `Images` folder containing the categories folders (look at the [hierarchy](## Prerequisites) above);
- fills the two folders `Annotations_txt` and `Annotations_xml`;
- creates in them the same hierarchy found in `Images`;
- if you want to create only one of the two annotations comment line 34 or 35 in the script following the instructions in the comments.

Type `python write_annotationts.py` in the `iCubWorld-Transformation` directory to use it.
