# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:44:46 2019

@author: pi

czytanie danych ze strony - aktualna pogoda

"""

import requests
from bs4 import BeautifulSoup
import statistics


def windangle(w):
    res=[]
    di=0

    for i in w:
        if (i=="N"):
            res.append(0)
        elif (i=="E"):
            res.append(90)
        elif (i=="S"):
            res.append(2*90)
        elif (i=="W"):
            res.append(90)
            di=1    
    r= statistics.mean(res)
    if (di==1):
        r=360-r
    return r

def toint(txt):
    return int(''.join(filter(str.isdigit, txt)))

def pogteraz():

    #wynik: lista elementów 
    #[godzina,temperatura, wilgotnosc,zachmurzenie,deszcz(1=tak,0=nie),kierunek wiatru, prędkoć wiatru]
    adr="https://pogoda.interia.pl/prognoza-szczegolowa-krakow,cId,4970"
    page = requests.get(adr)
    soup=BeautifulSoup(page.text,'html.parser')
    temp = soup.find_all('span',attrs={'class': 'forecast-temp'})
    hour=soup.find_all('span',attrs={'class': 'hour'})
    humidity=soup.find_all('div',attrs={'class': 'entry-humidity-wrap'})
    clouds=soup.find_all('span',attrs={'class': 'entry-precipitation-value cloud-cover'})
    weather=soup.find_all('span',attrs={'class': 'forecast-phrase'})
    windsp=soup.find_all('span',attrs={'class': 'speed-value'})
    winddir=soup.find_all('span',attrs={'class': 'wind-direction'})
    
    w, h = 7,len(temp);
    res = [[0 for x in range(w)] for y in range(h)] 
    
    i=0
    for b in hour:
        res[i][0]=int(b.text)
        i=i+1
        
    
    i=0
    for b in temp:
        res[i][1]=toint(b.text)
        if (b.text[0]=="-"):
            res[i][1]=-res[i][1]
        i=i+1
        
    i=0
    
    for b in humidity:
        res[i][2]=10*(toint(b.text)//10)
        if (res[i][2]==100):
            res[i][2]=90
        i=i+1
        
    i=0
    
    for b in clouds:
        res[i][3]=20*(toint(b.text)//20)
        i=i+1
        
    i=0
    
    for b in weather:
        if "Deszcz" in b.text or "deszcz" in b.text or "opad" in b.text or "Opad" in b.text:
            res[i][4]=1
        i=i+1
    i=0
    
    for b in winddir:
        res[i][5]=windangle(b.text)
        i=i+1
        
    i=0
    
    for b in windsp:
        res[i][6]=5*(toint(b.text)//5)
        i=i+1
        
    i=0
    
    
    
    return res


