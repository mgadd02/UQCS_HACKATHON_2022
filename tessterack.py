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

    #print("--------------------------------------------\n" + dir + ":")

    res = re.findall(r'\w+', text.lower())
    words = " ".join(res)
    #print(words)
    #kws_list.append(words)

    r.extract_keywords_from_text(words)
    count = 0
    kws = ""
    for rating, keywords in r.get_ranked_phrases_with_scores():
        #print(keyword)
        keywords = keywords.split(" ")
        for keyword in keywords:
            if keyword.isalpha():
                kws += keyword + " "
                count += 1

            if count > 5:
                break
        if count > 5:
            break
    topic_list.append(kws[:len(kws)-1])

    

print(topic_list)
from tren import *
#trends(topic_list)

all_keywords = ['joe mama']
#trends(all_keywords)