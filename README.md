# Patch Image Generator 

A basic program to generate random patches (images and masks) for deep learning applications like semantic segmentation.

## Usage
* get_tiled_patches()
* get_random_patches()

## Explaination
Provide the following information in the main program:

## Input image and mask dir
* input/img/
* input/mask/
	
## Output patch image and mask dir
* out_path = './patches/'
* patch_img =  out_path + img_name +'/img/'
* patch_mask = out_path + img_name +'/mask/' 

## Patch image size:
* patch_tile_size = 128 # size of patch image 
	
## Number of patches to generate:
* n_images=3 # Number of patch to generate ( get_random_patches() )
