import requests
from bs4 import BeautifulSoup
import logging
import subprocess
import time
from random import randint
import sys

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

url = 'https://www.privateproperty.co.za/for-sale/western-cape/cape-town/55'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mainSuburbs")

#print(results.prettify())

#suburbs = results.find_all("ul", class_="linksHolder row")
suburbs = results.find_all("a")

suburb = []
links = []

for sub in suburbs:
    suburb.append(sub.text)
    links.append(sub['href'])


for link in links[0]:
    
    try:
        url = f'https://www.privateproperty.co.za{link}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        soup.find_all('div', class_='infoHolder')
        print(soup.find("div", class_='title'))
    
    except requests.exceptions.ConnectionError:
        if RETRY_COUNT > 0:
                RETRY_COUNT -= 1
                refreshIP()
                url = f'https://www.privateproperty.co.za{link}'
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "html.parser")
                soup.find_all('div', class_='infoHolder')
                print(soup.find("div", class_='title'))
        else:
            # Exit - failed to get around their IP blocker
            logging.info("We've been caught out!")
            sys.exit()





