import cv2
import numpy as np
import pytesseract
from PIL import Image

path = "test_data/"
output = "result/"
# Read image with opencv
img = cv2.imread(path + 'image.jpg')

# Convert to gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Remove noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

# Write image after removed noise
cv2.imwrite(output + "removed_noise.png", img)

# Recognize text with tesseract for python
result = pytesseract.image_to_string(Image.open(output + "removed_noise.png"))


print(result)
