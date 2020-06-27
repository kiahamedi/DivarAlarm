#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 00:47:36 2019
@author: kia
"""

from bs4 import BeautifulSoup
import requests
import time
from os import system

maxEj = input(str("Enter your Maximum Rent:"))
maxVa = input(str("Enter your Maximum Deposit:"))
url = "https://divar.ir/s/tehran/rent-residential"

while True:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    firstElement = soup.find('a', {"class": "col-xs-12 col-sm-6 col-xl-4 p-tb-large p-lr-gutter post-card"})
    vadie = firstElement.find('div', {"class": "body-12 post-card__description"})
    itemsArray = vadie.text.split('\n')

    vadie = itemsArray[0].replace("تومان", "").replace("ودیعه:", "").strip().replace(",", "")
    ejare = itemsArray[1].replace("تومان", "").replace("اجاره ماهیانه:", "").strip().replace(",", "")
    titleAD = firstElement.find('div', {"class": "subtitle-16 post-card__title"}).text
    urlAD = "https://divar.ir" + firstElement['href']


    if ejare == "مجانی" or ejare == "توافقی":
        ejare = "0"

    if vadie == "مجانی" or vadie == "توافقی":
        vadie = "0"

    rfile = open("lastItem.txt", "r")
    lastItem = rfile.readline().strip()

    if lastItem == titleAD:
        print("sleep for 10 second")
        time.sleep(10)


    elif (vadie) <= maxVa and (ejare) <= maxEj:
        file = open("lastItem.txt", "w+")
        file.write(titleAD)
        file.writelines("\n"+vadie)
        file.writelines("\n"+ejare)
        file.close()
        print("ALAAAAARM")
        system("notify-send 'Divar Alarm'")
        system('cvlc /home/kia/Music/coindrop.wav& sleep 2 && killall vlc')
        system('firefox ' + urlAD)
        time.sleep(10)

    else:
        print("Max")
        time.sleep(10)

