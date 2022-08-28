from bs4 import BeautifulSoup
import requests
import os
import re
import nltk
import numpy
from rake_nltk import Rake
from keybert import KeyBERT

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
}

def imageHeadings(url):
    googlepath = "https://images.google.com/searchbyimage?image_url=" + url
    req = requests.get(googlepath, headers=headers)
    doc = BeautifulSoup(req.text, "html.parser")
    items = doc.find_all("h3")
    results = []
    for header in items:
        heading = header.text
        if (heading != "Visually similar images"):
            results.append(heading)
        
    return results

def headingsToTags(headings):
    rake = Rake()
    filteredHeadings = []
    for heading in headings:
        heading = ''.join([i for i in heading if not i.isdigit()])
        heading = re.sub(r'[^\w]', ' ', heading)
        heading = " ".join(heading.split())
        filteredHeadings.append(heading)
    rake.extract_keywords_from_sentences(filteredHeadings)
    draftKeyList = []
    for rating, keyword in rake.get_ranked_phrases_with_scores():
        if rating > 5:
            draftKeyList.append(keyword)
    refinedText = ""
    for key in draftKeyList:
        refinedText = refinedText +  " " + key
    refinedText  = re.sub(r'[^\w]', ' ', refinedText)
    refinedText = " ".join(refinedText.split())
    kw_model = KeyBERT()
    results = kw_model.extract_keywords(refinedText)
    keywords =[]
    for word, score in results:
        keywords.append(word)
    return keywords

    

def imageFinder(url, numImages):
    googlepath = 'https://images.google.com/searchbyimage?image_url=' + url
    req = requests.get(googlepath, headers=headers)
    doc = BeautifulSoup(req.text, "html.parser")
    linkDiv = doc.find("g-section-with-header").find("a")
    link = linkDiv["href"]
    req = requests.get(googlepath + link)
    doc  = BeautifulSoup(req.text, "html.parser")
    imgDivs = doc.findAll("a")
    links = []
    num = 0
    for img in imgDivs:
        info = img.find("img")
        if num == 0:
            num += 1
            continue
        if (info and num < numImages + 1):
            links.append(info["src"])
            num += 1
    return links

#def sentiment():
#    print ("")

defaultURL = "https://cdn.discordapp.com/attachments/339681674944315392/1012522250051788871/unknown.png"
usrIn = input("URL: ")
if usrIn == "":
    usrIn = defaultURL

print(headingsToTags(imageHeadings(usrIn)))