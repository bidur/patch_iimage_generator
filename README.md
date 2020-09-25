# Patch Image Generator 

A basic program to generate random patches ( images and masks) for deep learning applications like semantic segmentation.

Provide the following information in the main program:

## Input image and mask dir
* input_image_path ='./input/cat001_img.png' # https://github.com/HZCTony/U-net-with-multiple-classification/blob/master/data/catndog/train/image/cat/cat001.png
* input_mask_path ='./input/cat001_mask.png' # https://github.com/HZCTony/U-net-with-multiple-classification/blob/master/data/catndog/train/label/cat/cat001.png
	
## Output patch image and mask dir
* out_path = './patches/'
* patch_img =  out_path +'img/'
* patch_mask = out_path +'mask/' 

## Patch image size:
* patch_tile_size = 128 # size of patch image 
	
## Number of patches to generate:
* n_images=3 # Number of patch to generat
