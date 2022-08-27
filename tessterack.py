import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Michael\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

import os

path = "./imgs"
dir_list = os.listdir(path)

for dir in dir_list:
    img = Image.open(path + "/" + dir)
    text = tess.image_to_string(img)

    print(dir + "--------------------------------------------\n" + text)