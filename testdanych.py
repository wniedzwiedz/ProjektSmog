# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:02:12 2019

@author: pichi
"""
import stacje
import pogoda


a,b,p2017=stacje.load()
s=473-6
l=24
p=[]
i=s


while i < (l+s):
    p.append(pogoda.pogodaD(p2017[i].day,p2017[i].month,p2017[i].year))
    print(i/24)
    i=i+24

for g in range (len(p)):
    p=p+p[g]

t=[]
i=s
while (i<l+s):
    t.append(a[0][i-1][0])
    i=i+1
#zapisz listę p do pliku
#with open('dane/pogoda2017.txt', 'wb') as fp:
#    pickle.dump(p, fp)

