# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:07:38 2019

@author: pichi
"""

import statistics
import matplotlib.pyplot as plt
import numpy as np

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
    
    
    
    
def podziel(lista,minimum,maximum,param,dane): #param - po którym parametrze dzielić
    res = [[] for x in range(maximum-minimum)]
    sd= [[] for x in range(maximum-minimum)]
    mn=[[] for x in range(maximum-minimum)]
    j=0
    for l in lista:
        for i in l:

            if (dane[j]!="BRAK" and i[param]!="CLM" and i[param]!=0):
                x=windangle(i[param])
                res[(((x))-minimum)].append(dane[j][0])
            j=j+1
    
    w=0
    todel=[]
    for q in res:
        if(len(q)>1):
            sd[w]=statistics.stdev(q)
        if(len(q)>0):
            mn[w]=statistics.mean(q)
        else:
            todel=[w]+todel
            
        w=w+1
    print(todel)
    
    for td in todel:
        print(td)
        del mn[td]
        del sd[td]
        del res[td]

    return res,sd,mn

g = [i for i in range(0,360)]

x0=0
x1=360
par=6

td=[359, 358, 357, 356, 355, 354, 353, 352, 351, 350, 349, 348, 347, 346, 345, 344, 343, 342, 341, 340, 339, 338, 337, 336, 335, 334, 333, 332, 331, 329, 328, 327, 326, 325, 324, 323, 322, 321, 320, 319, 318, 317, 316, 314, 313, 312, 311, 310, 309, 308, 307, 306, 305, 304, 303, 302, 301, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290, 289, 288, 287, 286, 285, 284, 283, 282, 281, 280, 279, 278, 277, 276, 275, 274, 273, 272, 271, 269, 268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227, 226, 224, 223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 209, 208, 207, 206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for t in td:
    del g[t]


g0,sg0,mg0=podziel(p,x0,x1,par,pm10_2017[0])
g1,sg1,mg1=podziel(p,x0,x1,par,pm10_2017[1])
g2,sg2,mg2=podziel(p,x0,x1,par,pm10_2017[2])
g3,sg3,mg3=podziel(p,x0,x1,par,pm10_2017[3])
g4,sg4,mg4=podziel(p,x0,x1,par,pm10_2017[4])
g5,sg5,mg5=podziel(p,x0,x1,par,pm10_2017[5])
g6,sg6,mg6=podziel(p,x0,x1,par,pm10_2017[6])
g7,sg7,mg7=podziel(p,x0,x1,par,pm10_2017[7])

wyniki=[[sg0,sg1,sg2,sg3,sg4,sg5,sg6,sg7],[mg0,mg1,mg2,mg3,mg4,mg5,mg6,mg7],[g]]

plt.plot(g,mg0,'o')
plt.plot(g,mg1)
plt.plot(g,mg2)
plt.plot(g,mg3)
plt.plot(g,mg4)
plt.plot(g,mg5)
plt.plot(g,mg6)
plt.plot(g,mg7)
