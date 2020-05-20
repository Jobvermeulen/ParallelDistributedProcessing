# Computer Vision Assessment 2
In this folder you will find assessment 2

## Table of contents

* [Assignment 1](#assignment-1)
* [Dataset](#dataset)

## Assignment 1
The task for this assignment is to write code in Python with the the Keras Library that can classify `healthy RBC cells` and `Sick cells`. <br />
For this assignment there is given a dataset with `Healthy RBC cells` and `Sick cells`. <br />

The dataset is added in the `Original_Dataset` folder. <br />
For this assignment the dataset is expanded to `5000+ images` by using the created python script `Expanding_Dataset`. Follow the steps below to expand the dataset.

### Result
After changing alot of parameters and trying to get a good accuracy. I ended up with a 82,50% accuracy with a model. <br />
This doesn't regocnize all sick images yet, but I don't get it higher at the moment. <br />
This model is saved in the `Models` folder as file `model-81,25.h5`

## Dataset
Coming with the original dataset you don't get alot of images and that needs to be extended. <br /> 
You start with a total of `175 images`:
- 91 Healthy RBC cell images
- 84 Sick cell images

### Expanding the dataset
Follow these stept to upgrade the dataset from `175 images` to `5000+ images`
- Create tho new folders called `Images` and `Images_Augmentated` in the root folder or this assesment `Assessment_2`
- Copy the images from the folders `RBCs` and `Sickles` in the folder `Original Dataset`
- Paste the image together in the folder `Images` without the sub-folders `RBCs` and `Sickles`.
- Start the `Expanding_Dataset` script in jupyter notebook and execute it.
- Check the folder `Images_Augmentated` if there are now `5000+ images` available.
