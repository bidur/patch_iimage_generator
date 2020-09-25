import os, gdal,random

def save_patch_image(input_image_path,out_small_image, srcwin_option):

	gdal_command = "gdal_translate "
	#gdal_command += " -of GTIFF "  # if not given -> guessed from extention

	gdal_command += "  -co COMPRESS=DEFLATE  "
	gdal_command += srcwin_option
	gdal_command += " " + input_image_path + " " + out_small_image
	print (gdal_command)
	os.system(gdal_command)
	
	return



#def get_patches( input_img_path, output_dir, img_type = 'images', n_images=3 ): #img_type = 'masks'  #'masks' # 'images'
def get_patches(input_image_path,input_mask_path, patch_img , patch_mask, patch_tile_size = 128, n_images=3):

	os.makedirs(patch_img, exist_ok=True)
	os.makedirs(patch_mask, exist_ok=True)

	tile_size_x =  patch_tile_size
	tile_size_y =   patch_tile_size
	ds = gdal.Open(input_image_path)

	band = ds.GetRasterBand(1)
	xsize = band.XSize
	ysize = band.YSize
	
	_, mask_ext = os.path.splitext(input_mask_path)
	_, img_ext  = os.path.splitext(input_image_path)

	
	for i in range(n_images):
		
		i_offset = random.randint(0, xsize)
		j_offset = random.randint(0, ysize)
		
		#out_small_image = str(patch_img)  + str(i) +  ".tif"
		
		srcwin_option =		"   -srcwin "  + str( i_offset)+ ", " + str( j_offset) + ", " + str(tile_size_x) + ", " + str(tile_size_y)
		save_patch_image(input_image_path , str(patch_img)  + str(i) +  "."+ img_ext  , srcwin_option)
		save_patch_image(input_mask_path   , str(patch_mask)  + str(i) +  "."+ mask_ext  , srcwin_option)

	return i

###################################################


def main():
	
	# Input image and mask dir
	input_image_path ='./input/cat001_img.png' # https://github.com/HZCTony/U-net-with-multiple-classification/blob/master/data/catndog/train/image/cat/cat001.png
	input_mask_path ='./input/cat001_mask.png' # https://github.com/HZCTony/U-net-with-multiple-classification/blob/master/data/catndog/train/label/cat/cat001.png
	
	# output patch image and mask dir
	out_path = './patches/'
	patch_img =  out_path +'img/'
	patch_mask = out_path +'mask/' 
	
	patch_tile_size = 128 # size of patch image 
	n_images=3 # Number of patch to generate
	
	
	# invoke the patch generator
	get_patches(input_image_path,input_mask_path, patch_img , patch_mask, patch_tile_size, n_images)
	
	return

if __name__ == "__main__":
    main()
