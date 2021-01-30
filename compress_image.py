
""" A very basic image compression program using python's pillow module."""
 
import os 
import sys 
from PIL import Image 

# Place .m file within the directory where image compression is desired. 

sav_dir = #somedir

def compress_all(file, verbose = False): 
	"""
    This function carries out the image compression using Image from PIL.
    Altering the quality changes compression and image quality.
    """
	
    filepath = os.path.join(os.getcwd(), file) 
	
	# Open  and save the image. 
	text_img = Image.open(filepath) 
	text_img.save(
                sav_dir + file, 
				"JPEG", 
				optimize = True, 
				quality = 75,
                ) 
	return


def main(): 
	""" Run compress_all for each file in the current directory."""
	
    verbose = False
	if (len(sys.argv) > 1): 
		
		if (sys.argv[1].lower() == "-v"): 
			verbose = True
					
	# Retrieve the working directory 
	cwd = os.getcwd() 
	allowed_formats = ('.png', '.jpg') 
	
	# looping through all the files in the current directory 
	for file in os.listdir(cwd): 
		if os.path.splitext(file)[1].lower() in allowed_formats: 
			print('compressing', file) 
			compress_all(file, verbose) 

	print("All allowed files completed!") 

# Driver code 
if __name__ == "__main__": 
	main() 
