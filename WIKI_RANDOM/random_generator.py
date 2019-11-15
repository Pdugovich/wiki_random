"""contains function to print a random wikipedia article paragraph"""

import requests
from bs4 import BeautifulSoup
from numpy.random import random


def RandomWiki():
    source = requests.get("http://en.wikipedia.org/wiki/Special:Random").text
    soup = BeautifulSoup(source,'html.parser')
    title = soup.find('title')
    paragraphs = soup.find_all('p', text=True)

    plist=[]
    for i in paragraphs:
        if len(list(i.text)) > 0 and i.text != '\n':
            print(f'next item is: {i}')
            plist.append(i.text)

    print(plist)
    if len(plist) <1:
        return RandomWiki()

    #Title with the last characters " - Wikipedia" removed
    title_isolated = title.text[:-12]

    return title_isolated, plist[0]
