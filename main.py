import cv2
import numpy as np
import pytesseract
from PIL import Image
from metric import final
import os


set_int = int(input("Enter the set number to extract text from (eg. 5) : "))
set = "set" + str(set_int)
path = "/DIQ_Part1/" + set + "/"
initial_cwd = os.getcwd()
os.chdir(initial_cwd + path)
temp1 = os.getcwd()
temp = os.listdir()
file_name = max(temp, key=len)
final_path = os.getcwd()+"/"+file_name
output = temp1

# Read image with opencv
img = cv2.imread(final_path)

# Convert to gray
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Remove noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

# Write image after removed noise
cv2.imwrite(output + "/processed.jpg", img)

# Recognize text with tesseract for python
result = pytesseract.image_to_string(Image.open(output + "/processed.jpg"), config = ('-l eng --oem 1 --psm 3'))


print("The extracted text from the image is : \n" + result)
text_file = open("result.txt", "w")
text_file.write(result)
text_file.close()

pred_result_file_path = os.getcwd() + "/" + "result.txt"
os.chdir(os.getcwd()+"/GTOCR/")
true_result_file_path = os.getcwd() + "/" + max(os.listdir(), key=len)

print("\n......................................")
print("......................................")
print("......................................\n")
print("The cosine similarity for " + set + " is " + str(final(true_result_file_path, pred_result_file_path)))