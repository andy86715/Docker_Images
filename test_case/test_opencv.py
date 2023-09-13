import cv2
import fitz
import filetype
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pyzbar.pyzbar import decode

# read image
image = cv2.imread('../data/test.jpg')
print(image.shape)
print('Finish of test image read')
print('-------------------------')

# convert pdf
with open('../data/matplotlib.pdf', 'rb') as f:
	binary = f.read()

input_type = filetype.guess(binary)
if input_type.extension == 'pdf':
	print('start convert pdf')
	doc = fitz.open('pdf', binary)
	pix = doc[0].get_pixmap(dpi=200).tobytes('PNG')
	doc.close()

	# to image
	image = np.frombuffer(pix, np.uint8)
	image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
	print(image.shape)

print('Finish of test convert pdf')
print('-------------------------')

# SIFT
img1 = cv2.imread('../data/test.jpg',cv2.IMREAD_GRAYSCALE) # queryImage
img2 = cv2.imread('../data/test.jpg',cv2.IMREAD_GRAYSCALE) # trainImage
# Initiate SIFT detector
sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
print(len(matches))
print('Finish of test SIFT')
print('-------------------------')

# barcode
print(decode(Image.open('../data/code128.png')))
print('Finish of test barcode')
