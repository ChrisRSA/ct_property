import requests
from bs4 import BeautifulSoup
import logging
import subprocess
import time
from random import randint
import sys
import pandas as pd
from collections import defaultdict

url = 'https://www.privateproperty.co.za/for-sale/western-cape/cape-town/55'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mainSuburbs")

suburbs = results.find_all("a")

suburb = []
page_links = []

for sub in suburbs:
    suburb.append(sub.text)
    page_links.append(sub['href'])

#print(page_links)

ad_links = []

test_links = page_links[0:1]

for link in test_links:
    for i in range(1,2):
        url = 'https://www.privateproperty.co.za'
        html_string = requests.get(url + link + '?=page' + str(i)).content
        soup = BeautifulSoup(html_string, 'html.parser')

        results = soup.find_all('a', class_='listingResult row')
        
        for result in results:
            ad_links.append(result['href'])
            #print(result['href'])

#print(ad_links[0:1])

name = []
price = []
address = []

for link in ad_links:
    url = 'https://www.privateproperty.co.za'
    html_string = requests.get(url + link).content
    soup = BeautifulSoup(html_string, 'html.parser')

    results = soup.find_all('div', class_='marginedIn')
    for result in results:
        name.append(result.find("h1").text)
        price.append(result.find('span', class_='detailsPrice').text)
        #print(result.find("h1").text)
        #print(result.find('span', class_='detailsPrice').text)
        try:
            add = result.find('div', class_='address').text
            add = add.split(':')[1].lstrip()
        except:
            add = 'None'
        address.append(add)

print(name)

    
    

