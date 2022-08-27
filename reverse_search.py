from bs4 import BeautifulSoup
import requests
import os
testURL = "https://cdn.discordapp.com/attachments/339681674944315392/1012522250051788871/unknown.png"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
}

def imageTagsLookup(url):
    googlepath = 'https://images.google.com/searchbyimage?image_url=' + url
    print(googlepath)
    req = requests.get(googlepath, headers=headers)
    doc = BeautifulSoup(req.text, 'html.parser')
    #with open("output1.html", "w") as file:
    #    file.write(str(doc))
    items = doc.find_all("h3")
    print("Finding Tags:\n\n")
    for header in items:
        print (str(header) + "\n")

def imageFinder(url):
    googlepath = 'https://images.google.com/searchbyimage?image_url=' + url
    print(googlepath)
    req = requests.get(googlepath, headers=headers)
    doc = BeautifulSoup(req.text, 'html.parser')
    headings = doc.find("h3", text="Visually similar images")
    print("\nLink\n")
    print(headings)
    
usrIn = input("URL: ")
#usrIn = testURL
imageTagsLookup(usrIn)
imageFinder(usrIn)