1# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:59:43 2019

prognoza PM10 na 70 godzin

@author: pi
"""

import pickle
import pogodateraz
import stacje as st
import requests
import json
import matplotlib.pyplot as plt


#wczytywanie danych archiwalnych z plików

with open ('dane/analiza/godz2017.txt', 'rb') as fp:
    godz = pickle.load(fp)
    
with open ('dane/analiza/chmury2017.txt', 'rb') as fp: #chmury - segmenty po 20 punktów procentowych
    chmury = pickle.load(fp)
    
with open ('dane/analiza/opady2017.txt', 'rb') as fp: #1-tak, 0-nie
    opady = pickle.load(fp)
    
with open ('dane/analiza/temp2017.txt', 'rb') as fp:
    temp = pickle.load(fp)
    
with open ('dane/analiza/wiatrkier2017.txt', 'rb') as fp:
    wiatrkier = pickle.load(fp)
    
with open ('dane/analiza/wiatrpr2017.txt', 'rb') as fp: #wiatrpr - segmenty po 5
    wiatrpr = pickle.load(fp)
    
with open ('dane/analiza/wilg2017.txt', 'rb') as fp: #wilgoć - segmenty po 10 pkt %
    wilg = pickle.load(fp)
    
def znajdzwart(lista,x,stacja=0): #wynik: odchylenie stand., srednia]
    j=0
    for l in lista[2][0]:
        if (l==x):
            i=j
            break
        j=j+1
    
    
    return lista[0][stacja][i], lista[1][stacja][i] 

    #[godzina,temperatura, wilgotnosc,zachmurzenie,deszcz(1=tak,0=nie),kierunek wiatru, prędkoć wiatru]

def znajdzwartosci(g,t,w,c,o,k,p,st=0):
    x=[]
    x.append( znajdzwart(godz,g,st) )
    x.append( znajdzwart(temp,t,st) )
    x.append( znajdzwart(wilg,w,st) )
    x.append( znajdzwart(chmury,c,st) )
    x.append( znajdzwart(opady,o,st) )
    x.append( znajdzwart(wiatrkier,k,st) )
    x.append( znajdzwart(wiatrpr,p,st) )
    
    sumasd=0
    
    for i in x:
        sumasd=sumasd+i[0]

    
    r=0

    for i in x:
        r=r+i[1]*((sumasd-i[0])/((sumasd*len(x))-1))
    
    return r
    
    
def znajdzteraz(i):
    pog=pogodateraz.pogteraz()
    res=[]
    for q in pog:
        res.append([q[0],znajdzwartosci(q[0],q[1],q[2],q[3],q[4],q[5],q[6],i)])
    return res

def zmiany(i): #funkcja zwraca zmianę poziomu zanieczyszczeń co godzinę dla 8 stacji przez najbliższe 70 godzin
    res=[]
    p=znajdzteraz(i)
    
    for i in range(1,len(p)):
        res.append( [p[i][0], p[i][1]-p[i-1][1]] )
            
    return res


#Odbierz dane z sensora o okreslonym id z airly
def getSensorData(id,n):
    id=str(id)
    url="https://airapi.airly.eu/v2/measurements/installation?installationId="+id
    payload = {}
    headers = {'Accept': 'application/json', 'apikey': 'DJoSUEFJJlO8HlofLCBynfBqDBcFgxKk'}

    r = requests.get(url, data=json.dumps(payload), headers=headers)

    if (r.status_code==200):#Sukcess?
        #print(r.json().get("current").get("values")[1]) #wypisz aktualne dane
        if (len(r.json().get("current").get("values"))>1):
            return (r.json().get("current").get("values")[n])['value']
            
        else:

            x = '{ "name": "PM25", "value": 0}'
            y = json.loads(x)

            return(y)
    else:
        print("error")
        
        
pm10_2017,pm25_2017,a=st.load()

stacjeId=[[17,1],[18,1],[19,1],[7394,2],[238,2],[7830,2],[2545,2],[2185,2]]
#id stacji oraz pozycja, na której w jej wynikach są dane o PM10


def main():
    #główne menu
    print (30 * '-')
    print ("PM10 - stan na najbliższe 70 godzin")
    print ("Wybierz stację pomiarową")
    print (30 * '-')
    print ("1. Aleja Krasińskiego")
    print ("2. Bujaka")
    print ("3. Bulwarowa")
    print ("4. Dietla")
    print ("5. Osiedle Piastów")
    print ("6. Telimeny")
    print ("7. Wadowicka")
    print ("8. Złoty Róg")
    print (30 * '-')
     
    choice = input('Wpisz numer [1-8] : ')
    choice = int(choice)
    start=getSensorData(stacjeId[choice-1][0],stacjeId[choice-1][1])
    zm=zmiany(choice-1)
    print("Teraz ",start)
    s=[]
    j=[]
    
    #wyniki prognozy
    for z in zm:
        start=start+z[1]
        if(start<0):
            start=0
            
        s.append(start)
            
        print (z[0],start)
        
    g = [i for i in range(0,len(s))]
    
    #wykres
    plt.plot(g,s)
    plt.xlabel("ilosć godzin od teraz")
    plt.ylabel("szacowany poziom smogu")
    
    
main()