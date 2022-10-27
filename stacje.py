# -*- coding: utf-8 -*-
"""
Created on Thu May  9 03:34:40 2019

czyta położenie stacji + podgląd ich rozkładu + rozmiar zależny od poziomu PM10 dnia 01.01.2017

@author: pi
"""

import xlrd
import matplotlib.pyplot as plt
import datetime


def ststart():
    s = xlrd.open_workbook('dane/MetadaneKrk.xls')
    stacje = s.sheet_by_index(0)
    
    p = xlrd.open_workbook('dane/2017_PM10_1g.xls')
    pm10 = p.sheet_by_index(0)
    pc=pm10.ncols-1
    
    p2 = xlrd.open_workbook('dane/2017_PM25_1g.xls')
    
    
    w, h = 4, pc; #8 stacji, 4 pola: nazwa, dł i szer, dane testowe
    res = [[0 for x in range(w)] for y in range(h)] #w tym jest zapisane id i koordynaty
    
    for i in range (8):
        print(stacje.cell(i, 1).value,stacje.cell(i, 14).value,stacje.cell(i, 15).value)
        res[i][0]=stacje.cell(i, 1).value
        res[i][1]=stacje.cell(i, 14).value
        res[i][2]=stacje.cell(i, 15).value
        
        for j in range (pc):
        
            if (pm10.cell(1,j).value == res[i][0] and pm10.cell(6,j).value!=""):
                q=pm10.cell(6,j).value
                res[i][3]=float(q.replace(',', '.'))
            
        
        #plt.scatter(res[i][1],res[i][2],s=res[i][3]+10)
    stacje=res
    return p,p2,res

#czytanie danych do listy [dane, czas]

def czytaj(id,pl):
    
    plik = pl.sheet_by_index(0)
    c=plik.ncols
    r=plik.nrows
    res=[]
    
    for i in range (r-6):
        for j in range (c):
            if (plik.cell(1,j).value == id and plik.cell(6+i,j).value!=""):
                q=plik.cell(6+i,j).value
                
                a1 = plik.cell_value(rowx=6+i, colx=0)
                d1 = datetime.datetime(*xlrd.xldate_as_tuple(a1, pl.datemode))
                
                res.append([float(q.replace(',', '.')),d1])
            elif (plik.cell(1,j).value == id):
                res.append("BRAK")
                
            
    return res


def load():
    p,p2,res=ststart()
    pm10_2017=[]
    pm25_2017=[]
    for i in range (8):
        pm10_2017.append(czytaj(res[i][0],p))
        pm25_2017.append(czytaj(res[i][0],p2))
        
    p2017=[]
    plik = p.sheet_by_index(0)
    r=plik.nrows
    for i in range (r-6):
        a1 = plik.cell_value(rowx=6+i, colx=0)
        d1 = datetime.datetime(*xlrd.xldate_as_tuple(a1, p.datemode))
        p2017.append(d1)
    return pm10_2017,pm25_2017,p2017