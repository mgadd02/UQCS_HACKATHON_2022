import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Michael\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

import os

path = "./imgs"
dir_list = os.listdir(path)

from rake_nltk import Rake
r = Rake()
import re
import enchant
d = enchant.Dict("en-US")

topic_list = []
for dir in dir_list:
    if dir == "Temp disabled":
        break

    img = Image.open(path + "/" + dir)
    text = tess.image_to_string(img)

    res = re.findall(r'\w+', text.lower())
    words = " ".join(res)

    r.extract_keywords_from_text(words)
    count = 0
    kws = []
    for rating, keywords in r.get_ranked_phrases_with_scores():
        keywords = keywords.split(" ")
        for keyword in keywords:
            if (keyword.isalpha() or (rating > 5 and keyword.isalpha())) and len(keyword) > 3:
                kws.append(keyword)
                count += 1

            if count > 3:
                break
        if count > 3:
            break
    if len(kws) != 0:
        topic_list.append(kws)

print(topic_list)

from tren import *
trends(topic_list)

#trends([['kid named finger']])