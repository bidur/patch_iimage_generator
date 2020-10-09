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

def save_patch_ann(input_image_path,out_small_image, srcwin_option):

	gdal_command = "gdal_translate "
	#gdal_command += " -of GTIFF "  # if not given -> guessed from extention

	gdal_command += " -of ENVI -co COMPRESS=DEFLATE" # for 1 band format mask/annotation image
	gdal_command += srcwin_option
	gdal_command += " " + input_image_path + " tmp"
	gdal_command += "&& gdal_translate tmp " + out_small_image
	
	print (gdal_command)
	os.system(gdal_command)
	
	return


#def get_patches( input_img_path, output_dir, img_type = 'images', n_images=3 ): #img_type = 'masks'  #'masks' # 'images'
def get_random_patches(input_image_path,input_mask_path, patch_img , patch_mask, patch_tile_size, n_images):

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
		save_patch_image(input_image_path , str(patch_img)  + str(i) + img_ext  , srcwin_option)
		save_patch_ann(input_mask_path   , str(patch_mask)  + str(i) + mask_ext  , srcwin_option)

	return i




#def get_patches( input_img_path, output_dir, img_type = 'images', n_images=3 ): #img_type = 'masks'  #'masks' # 'images'
def get_tiled_patches(input_image_path,input_mask_path, patch_img , patch_mask, patch_tile_size):

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

	image_sn = 1
	#for i in range(n_images):
	for i in range(0, xsize, tile_size_x):
		for j in range(0, ysize, tile_size_y):
			print ('$$$$$$$$$$ ', i,j)		
			srcwin_option =		"   -srcwin "  + str( i)+ ", " + str( j) + ", " + str(tile_size_x) + ", " + str(tile_size_y)
			save_patch_image(input_image_path , str(patch_img)  + str(image_sn)+ "_" +str(i) + "-" + str(j) + img_ext  , srcwin_option)
			save_patch_ann(input_mask_path   , str(patch_mask)  + str(image_sn)+ "_" +str(i)+ "-" +str(j) + mask_ext  , srcwin_option)

	return i
###################################################


def main():
	
	input_img_dir = './input/img/'
	input_mask_dir = './input/mask/'
	input_images = os.listdir(input_img_dir)

	
	patch_tile_size = 128 # size of patch image 
	n_images=3 # Number of patch to generate
	
	for img in input_images:
		
		img_name = os.path.splitext(img)[0]
		input_image_path = input_img_dir + img
		input_mask_path = input_mask_dir + img
		
		out_path = './patches/' + img_name + '/'
		patch_img =  out_path +'img/'
		patch_mask = out_path +'mask/' 
		
		get_tiled_patches(input_image_path,input_mask_path, patch_img , patch_mask, patch_tile_size)
		#get_random_patches(input_image_path,input_mask_path, patch_img , patch_mask, patch_tile_size, n_images)
		
	return

if __name__ == "__main__":
    main()
