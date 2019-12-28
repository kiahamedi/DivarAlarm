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

maxEj = 500000
maxVa = 20000000
url = "https://divar.ir/s/urmia/rent-residential"



while True:
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html5lib')
    firstElement = soup.find('a',{"class":"col-xs-12 col-sm-6 col-xl-4 p-tb-large p-lr-gutter post-card"})
    vadie = firstElement.find('div',{"class":"body-12 post-card__description"})
    itemsArray = vadie.text.split('\n')
    
    vadie = int(itemsArray[0].replace("تومان","").replace("ودیعه:","").strip().replace(",",""))
    ejare = int(itemsArray[1].replace("تومان","").replace("اجاره ماهیانه:","").strip().replace(",",""))
    titleAD = firstElement.find('div',{"class":"subtitle-16 post-card__title"}).text
    urlAD = "https://divar.ir"+firstElement['href']

    rfile =  open("lastItem.txt","r")
    lastItem = rfile.read()
    
    if lastItem == titleAD:
        print("sleep for 10 second")
        time.sleep(10)
        continue
    else:
        file = open("lastItem.txt","w+")
        file.write(titleAD)
        file.close()
        print("ALAAAAARM")
        system("notify-send 'Divar Alarm'")
        system('cvlc /home/kia/Music/coindrop.wav& sleep 2 && killall vlc')
        system('firefox '+urlAD)
        break
    
    
    
    







