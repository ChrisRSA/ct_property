import requests
from bs4 import BeautifulSoup
import logging
import subprocess
import time
from random import randint
import sys
import pandas as pd
from collections import defaultdict

PAUSE = 7

RETRY_COUNT = 3

def pause():
    pause = randint(PAUSE - 2, PAUSE + 2)
    logging.info(f'* Pausing for {pause} seconds.')
    time.sleep(pause)

def refreshIP():
    logging.info('Refreshing IP')
    logging.info('Turning IPv6 off')
    subprocess.run(["networksetup",  "-setv6off", "Wi-Fi"])
    pause()
    logging.info('Turning IPv6 on again')
    subprocess.run(["networksetup",  "-setv6automatic", "Wi-Fi"])
    pause()

refreshIP()

url = 'https://www.privateproperty.co.za//for-sale/western-cape/cape-town/atlantic-seaboard/waterfront/653'

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('a', class_='listingResult row')

data_dict = defaultdict(list)

fo
    for x in results:
        #data_dict['title'].append(x.find("div", class_='title').text)
        #data_dict['price'].append(x.find("div", class_='priceDescription').text)
        #data_dict['type'].append(x.find("div", class_='propertyType').text)
        #data_dict['suburb'].append(x.find("div", class_='suburb').text)
        #data_dict['address'].append(x.find("div", class_='address').text)
        #data_dict['feat_1'] = x.find("div", class_='icon bedroom')['class'][1]
        #data_dict['feats'] = 
        #data_dict['feat_2'] = x.find("div", class_='icon bathroom')['class'][1]
        #data_dict['feat_3'] = x.find("div", class_='icon parking')['class'][1]
        #print(x.find_all("div", class_='number')[0].text)
        print(x["href"])

#print(data_dict)