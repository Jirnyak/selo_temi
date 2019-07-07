#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:34:31 2019

@author: Jirnyak
"""
import random

[]

glasny = 1097*["о"]+845*["е"]+801*["а"]+735*["и"]+262*["у"]+201*["я"]+190*["ы"]+64*["ю"]+32*["э"]+4*["ё"]

soglasny = 121*["й"]+48*["ц"]+349*["к"]+670*["н"]+170*["г"]+73*["ш"]+36*["щ"]+165*["з"]+97*["х"]+26*["ф"]+454*["в"]+281*["п"]+473*["р"]+440*["л"]+298*["д"]+94*["ж"]+144*["ч"]+547*["с"]+321*["м"]+626*["т"]+159*["б"]+174*["ь"]+4*["ъ"]

slovar = ""

print("Сколько хочешь новых слов?")

go = int(input())

while go > 0:
    
    first = ''

    second = ''

    letternumber = random.randint(5,10)

    pervoglas = 0

    coin = random.randint(0,1)

    if coin == 1:
        first = glasny[random.randint(0,len(glasny)-1)]
        first = first.upper()
        pervoglas = 1
    else:
        first = soglasny[random.randint(0,len(soglasny)-180)]
        first = first.upper()

    for i in range(letternumber-1):  
        if pervoglas == 0:
            coin = random.randint(1,10)
            if coin == 1:
                second += soglasny[random.randint(0,len(soglasny)-1)]
                pervoglas = 0
            else:
                second += glasny[random.randint(0,len(glasny)-1)]
                pervoglas = 1      
        else:
            coin = random.randint(1,10)
            if coin == 1:
                second += glasny[random.randint(0,len(glasny)-1)]
                pervoglas = 1
            else:
                second += soglasny[random.randint(0,len(soglasny)-180)]
                pervoglas = 0

    slovar += ' '+ first + second
    
    go -= 1

print(slovar)
   
   
