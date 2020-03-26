#Step 1: Import the essential libraries
from PIL import Image,ImageEnhance
import pytesseract
from scipy.misc import imsave
import numpy
import json

def binarize_image(image_name, target_image_name, threshold):
	try:
		#Step 2: Open the image
		image_file = Image.open(image_name)
		#Step 3: Enhance the color of image
		enh_bri = ImageEnhance.Color(image_file)
		brightness=1.6
		image_brightened = enh_bri.enhance(brightness)
		#Step 4: Convert the Enhanced image to gray scale
		image = image_brightened.convert('L')  
		image = numpy.array(image)
		#Step 5: Apply the threshold of 128 to the gray scale image and convert it to black and white
		#Call function binarize_array() which does thresholding and returns black & white image
		image = binarize_array(image, threshold)
		imsave(target_image_name, image)
	except Exception as e:
		print("Exception occured::",e)			

def binarize_array(numpy_array, threshold):
	for i in range(len(numpy_array)):
		for j in range(len(numpy_array[0])):
			if numpy_array[i][j] > threshold:
				numpy_array[i][j] = 255
			else:
				numpy_array[i][j] = 0
	return numpy_array    

def img_to_text():
	text=pytesseract.image_to_string(Image.open('output/res.png'))
	print(text)
	
def main():
	binarize_image('images/receipt.png', 'output/res.png', 128)
	#Step 6: Extract the text from image using tesseract
	#Call function img_to_text() which extracts text from the image
	img_to_text()

if __name__=='__main__':
	#Call main()
	main()	