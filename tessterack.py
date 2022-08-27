import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Michael\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

import os

path = "./imgs"
dir_list = os.listdir(path)

from rake_nltk import Rake
r = Rake()
import re

kws_list = []
for dir in dir_list:
    if dir == "Temp disabled":
        break

    img = Image.open(path + "/" + dir)
    text = tess.image_to_string(img)

    print("--------------------------------------------\n" + dir + ":")

    res = re.findall(r'\w+', text.lower())
    words = " ".join(res)
    print(words)
    #kws_list.append(words)

    r.extract_keywords_from_text(words)
    kws = ""
    for rating, keyword in r.get_ranked_phrases_with_scores():
        if rating > 5:
            kws = "{} {}".format(kws, keyword)
    print(kws)
    kws_list.append(kws[:5])

print(kws_list)
from tren import *
#trends(kws_list)

#all_keywords = ['kid named finger', 'market fryer', 'fortnite battle pass']
#trends(all_keywords)