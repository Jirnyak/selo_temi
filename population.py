#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:41:13 2019

@author: Jirnyak
"""
import random

nameslist = []

fnames = []

mnames = []

population = []

dead = []

linesnames = 0

percentage = 0.1

yeardate = 0

game = 1

mujikov = []

bab = []

graveyard = []


with open("russian_names.txt") as openfile:
    print("Генерирую библиотеки имён")
    num_lines = sum(1 for line in open("russian_names.txt"))
    print(num_lines, " строк")
    for line in openfile:
        linesnames += 1
        for part in line.split():
            if "Sex" in part:
                part = part.replace('<Sex>', '' )
                part = part.replace('</Sex>', '' )
                nameslist.append(part)
                if linesnames/num_lines > percentage:
                    percentage += 0.1
                    print(int((percentage)*100),"%")
            if "Name" in part:
                part = part.replace('<Name>', '' )
                part = part.replace('</Name>', '' )
                nameslist.append(part)
                if linesnames/num_lines > percentage:
                    percentage += 0.1
                    print(int((percentage)*100),"%")

for i in range(len(nameslist)):
    if nameslist[i] == "Ж":
        fnames.append(nameslist[i-1])
    if nameslist[i] == "М":
        mnames.append(nameslist[i-1])
  
print("Имена загружены.", len(mnames), "мужских и", len(fnames), "женских имён.")

class villager:
    age = 0
    pol = random.randint(0,1)
    name = ''
    deathdate = None
    children = []
    mother = None
    father = None
    
    def __init__(self, pol = None, name = '', age = 0, deathdate = None):
        self.pol = random.randint(0,1)
        self.age = random.randint(15, 60)
        if self.pol == 0:
            self.name =  mnames[random.randint(0, len(mnames)-1)]
            self.pol = 'мужчина'
        if self.pol == 1:
            self.name =  fnames[random.randint(0, len(fnames)-1)]
            self.pol = 'женщина'

def mujcount(array):
    mujikov = []
    for i in range(len(array)):
        if array[i].pol == 'мужчина' and array[i].age > 14 and array[i].age < 70:
            mujikov.append(array[i])
    return mujikov
        
            
def babcount(array):
    bab = []
    for i in range(len(array)):
        if array[i].pol == 'женщина' and array[i].age > 12 and array[i].age < 40:
            bab.append(array[i])
    return bab
     
def birth(population, mujikov, bab, femalen):
    global birthstat
    momlist = []
    dadlist = []
    dads = 0
    for i in range(femalen):
        luckymom = random.randint(1,10)
        if luckymom == 1:
            mamka = random.choice(bab)
            momlist.append(mamka)
            bab.remove(mamka)
            dads += 1
    for i in range(dads):
        dadlist.append(random.choice(mujikov))
    for i in range(len(momlist)):
        child = villager()
        child.mother = momlist[i].name
        child.father = dadlist[i].name
        momlist[i].children.append(child.name)
        dadlist[i].children.append(child.name)
        population.append(child)
        child.age = 0
        birthstat += 1
     # print(momlist[i].name, "и", dadlist[i].name, "родили ребёнка и назвали его:", child.name,". Это" , child.pol )
    
def yearoflife(array):
    global deathstat
    for i in range(len(array)):
        if array[i].deathdate == None:
            array[i].age += 1
        if array[i].age >= 60 and array[i].age < 70 and array[i].deathdate == None:
            deathprobability = random.randint(1, 20)
            if  deathprobability == 1:
                array[i].deathdate = yeardate
                deathstat += 1
        if array[i].age >= 70 and array[i].age < 80 and array[i].deathdate == None:
            deathprobability = random.randint(1, 10)
            if  deathprobability == 1:
                array[i].deathdate = yeardate
                deathstat += 1
        if array[i].age >= 80 and array[i].age < 90 and array[i].deathdate == None:
            deathprobability = random.randint(1, 5)
            if  deathprobability == 1:
                array[i].deathdate = yeardate
                deathstat += 1
        if array[i].age >= 90 and array[i].deathdate == None:
            deathprobability = random.randint(0, 1)
            if  deathprobability == 1:
                array[i].deathdate = yeardate
                deathstat += 1

def horonim(array, graveyard):
    for i in range(len(array)-1):
        if array[i].deathdate != None:
            graveyard.append(array[i])
            array[i] = 0
    while 0 in array:
        array.remove(0)
         
            

print('Скока людей будет жить в вашем селе?')

naselenje = input()

naselenje = int(naselenje)

for i in range(naselenje):
    population.append(1)
 
populsize = len(population)

for i in range(populsize):
    population[i] = villager()
    
for i in range(len(population)):
    print(population[i].pol, population[i].name, population[i].age, " лет" )

while game == 1:
    print('Скока лет будем ждать?')
    yeartowait = int(input())
    birthstat = 0
    deathstat = 0
    
    for i in range(yeartowait):
        mujikov = mujcount(population)
        bab = babcount(population)
        malen = len(mujikov)
        femalen = len(bab)
        if femalen*100 < malen:
            femalen = malen*100
        if len(bab) != 0 and len(mujikov) != 0:
            birth(population, mujikov, bab, femalen)
        yeardate += 1
        yearoflife(population)
        
        horonim(population, graveyard)
     
    for i in range(len(population)):
        print()
        print(population[i].pol, population[i].name, population[i].age, " лет" )
        if population[i].deathdate != None and population[i].pol == "мужчина":
            print("Умер в: ", population[i].deathdate, " году.")
        if population[i].deathdate != None and population[i].pol == "женщина":
            print("Умерла в: ", population[i].deathdate, " году.")
        if population[i].mother != None:
            print("Родители:", population[i].mother, "и", population[i].father)         

    print("За этот период родилось", birthstat, "детей и умерло", deathstat, "людей.")
    print("Население", len(population))
    
  
    
        
            
            
        
        
        
        
        
        
        