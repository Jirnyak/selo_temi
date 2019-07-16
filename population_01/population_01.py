
print("деревня хачей")

import random
import numpy
import tkinter

fnames = []
mnames = []
population = []
cemetry = []
familiainfluence = []
royalfamilia = ''
kinglist = []
tsarcandidate = None

def imena(textfile, list):
    f = open(textfile, 'r', encoding = 'utf8')
    for line in f:
        list.append(line.strip())

def familynamegenerator():

    glasny = 1097*["о"]+845*["е"]+801*["а"]+735*["и"]+262*["у"]+201*["я"]+190*["ы"]+64*["ю"]+32*["э"]+4*["ё"]

    soglasny = 121*["й"]+48*["ц"]+349*["к"]+670*["н"]+170*["г"]+73*["ш"]+36*["щ"]+165*["з"]+97*["х"]+26*["ф"]+454*["в"]+281*["п"]+473*["р"]+440*["л"]+298*["д"]+94*["ж"]+144*["ч"]+547*["с"]+321*["м"]+626*["т"]+159*["б"]+174*["ь"]+4*["ъ"]

    slovar = ""
    
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

    return slovar
    
imena('fnames.txt', fnames)
imena('mnames.txt', mnames)

class villager:

    age = 0
    pol = None
    name = ""
    familia = None
    deathdate = None
    mother = "неизвестна"
    father = "незвестен"
    health = 0
    genius = 0
    fertile = 0
    children = []
    royal = 0
    pretendent = 0
    number_of_villagers = 0
    
    def __init__(self):
        self.age = random.randint(15,30)
        self.pol = random.randint(0,1)
        if self.pol == 0:
            self.name =  mnames[random.randint(0, len(mnames)-1)]
            self.pol = 'мужчина'
            self.familia = familynamegenerator()
            if self.age > 12:
                self.fertile = 1
        if self.pol == 1:
            self.name =  fnames[random.randint(0, len(fnames)-1)]
            self.pol = 'женщина'
            self.familia = familynamegenerator()
            if self.age > 12 and self.age < 50:
                self.fertile = 1
        self.health = round(numpy.random.normal(0.5, 0.1, None), 3)
        self.children = []
        self.deathdate = None
        self.royal = 0
        self.pretendent = 0
        villager.number_of_villagers += 1




def appeality(health, age):
    return


def deathrate(health, age):
    if health == 0:
        return 0
    if age < 12:
        return 0.001/(health**2)
    if age > 11 and  age < 30:
        return 0.0001/health
    else:
        return (0.01/health)*(1.2**((age-30)/5))
    #return int(health*100+10)-age


def babcounter(list):
    plodovityh = []
    for i in range(len(list)):
        if list[i].fertile == 1 and list[i].pol == 'женщина':
            plodovityh.append(list[i])
    return plodovityh

def mujcounter(list):
    plodovityh = []
    for i in range(len(list)):
        if list[i].fertile == 1 and list[i].pol == 'мужчина':
            plodovityh.append(list[i])
    return plodovityh

naselenje = int(input("Сколько людей будет жить в вашем селе?"))


for i in range(naselenje):
    population.append(1)
 
populsize = len(population)

for i in range(populsize):
    population[i] = [villager()]

for i in range(len(population)):
    print(population[i][0].pol, population[i][0].name, population[i][0].familia, population[i][0].age, " лет", " здоровье ", population[i][0].health, " дети: ", population[i][0].children, " отец: ", population[i][0].father, " мать ", population[i][0].mother)

year = 0
tsar = 0
thronewar1 = 0
tsarnumber = 0
food = 10

while 1 == 1:
    simulationtime = int(input("Сколько лет ждать?"))
  
    dolgojitel = villager()
    dolgojitel.age = 0
    deathstat = 0
    rodstat = 0
    foodproduced = 0
    immigration = 0
    pretendent = None

    while simulationtime > 0:

        familycounter = 0
        temppop = []

        for k in range(len(population)):

            subjectfamily = population[k]
            familycounter += 1
            temppop.append([])
            

            for i in range(len(subjectfamily)):

                
                subjecthuman = subjectfamily[i]

                deathchance = random.random()

                food = food - subjecthuman.health

                if tsar == 0 and pretendent == None:
                    if thronewar1 < subjecthuman.health and subjecthuman.pol == "мужчина":
                        thronewar1 = subjecthuman.health
                     
                if tsar == 0 and pretendent != None:
                    tsarcandidate = pretendent
                    tsarcandidate.name = "Царь " + tsarcandidate.name
                    kinglist.append(tsarcandidate.name + tsarcandidate.familia + " начал править в " + str(year) + " год ")
                    tsarnumber += 1
                    tsar = 1


                if subjecthuman.familia == royalfamilia and subjecthuman.royal == 0:
                    subjecthuman.royal = 1
                    if subjecthuman.pol == "мужчина" and pretendent == None:
                        pretendent = subjecthuman
                       

                if subjecthuman.pol == "мужчина"  and subjecthuman.age > 12:  
                    subjecthuman.fertile = 1
                    subjecthuman.age += 1
                elif subjecthuman.pol == "женщина" and subjecthuman.age > 12 and subjecthuman.age < 50:
                    subjecthuman.fertile = 1
                    subjecthuman.age += 1
                else:
                    subjecthuman.fertile = 0
                    subjecthuman.age += 1
               
                if subjecthuman.royal != 1 and subjecthuman.age > 10 and subjecthuman.pol == "мужчина" and subjecthuman.age < 31:
                    food = food + subjecthuman.age/5*(subjecthuman.health)

                if subjecthuman.royal != 1 and subjecthuman.age > 10 and subjecthuman.pol == "женщина" and subjecthuman.age < 31:
                    food = food + subjecthuman.age/10*(subjecthuman.health)

                if subjecthuman.royal != 1 and subjecthuman.age > 30 and subjecthuman.pol == "мужчина":
                    food = food + (180/subjecthuman.age)*(subjecthuman.health)

                if subjecthuman.royal != 1 and subjecthuman.age > 30 and subjecthuman.pol == "женщина":
                    food = food + (90/subjecthuman.age)*(subjecthuman.health)

                if subjecthuman.deathdate == None and subjecthuman.age > dolgojitel.age:

                    dolgojitel = subjecthuman


                if deathrate(subjecthuman.health, subjecthuman.age) > deathchance or food < 0:

                    if subjecthuman == pretendent:
                        pretendent = None

                    if subjecthuman == tsarcandidate:
                        tsar = 0
                        thronewar1 = 0

                    subjecthuman.deathdate = year
                    cemetry.append(subjecthuman)
                    deathstat += 1
 
                if subjecthuman.deathdate == None:

                    temppop[familycounter-1].append(subjecthuman)


        if thronewar1 > 0:
            tsarcandidate = subjecthuman
            royalfamilia = tsarcandidate.familia
            tsarcandidate.name = "Царь " + tsarcandidate.name
            kinglist.append(tsarcandidate.name + tsarcandidate.familia + " начал править в " + str(year) + " год ")
            tsarnumber += 1
            tsarcandidate.royal = 1
            tsar = 1
            thronewar1 = 0



  

        population = temppop

        year += 1

        simulationtime -= 1

        

    for k in range(len(population)):

        subjectfamily = population[k]

        for i in range(len(subjectfamily)):
            print(subjectfamily[i].pol, subjectfamily[i].name, subjectfamily[i].familia, subjectfamily[i].age, " лет", " здоровье ", subjectfamily[i].health, " дети: ",  subjectfamily[i].children, " отец: ", subjectfamily[i].father, " мать ",  subjectfamily[i].mother)

    print("Кладбище")

    for i in range(len(cemetry)):
        print(cemetry[i].pol, cemetry[i].name, cemetry[i].familia, cemetry[i].age, " лет", " здоровье было ", cemetry[i].health, " дети: ", cemetry[i].children, " отец: ", cemetry[i].father, " мать ", cemetry[i].mother, " Дата смерти: ", cemetry[i].deathdate)


    print("Население :", len(population), ". Родилось: ", rodstat, ". Умерло: ", deathstat)

    print("Самый старый житель: ", dolgojitel.name, dolgojitel.familia, dolgojitel.age, " лет" )

    print("Правители: ", kinglist)

    print("Еды : ", food,)

    
    
   
    







    
    #print("Прибыло ", immigration, " иммигрантов.")

#def deathrate(health, age):
#   return 0.01*((health**-1)*(1.05**(age/10)))

'''

mujikov = mujcounter(population)
        bab = babcounter(population)
        if len(bab) == 0:
            mdelj = 0
        else:
            mdelj = len(mujikov)/len(bab)
            momlist = []
        dadlist = []
        temppop = []


        for i in range(len(bab)):
            mamka = random.choice(bab)
            if len(mujikov) > 0:
                papka = random.choice(mujikov)
                bab.remove(mamka)
                rodilka = mdelj * 0.2 *(mamka.health * papka.health)**0.5
                rody = random.random()
            else:
               rody = 1
               rodilka = 0
            if rody < rodilka:
                child = villager()
                child.age = 0
                child.fertile = 0
                child.familia = papka.familia
                child.health = round(((mamka.health + papka.health)/2) + random.uniform(-0.05, 0.05), 3)
                child.mother = mamka.name + mamka.familia
                child.father = papka.name + papka.familia
                mamka.children.append(child.name)
                papka.children.append(child.name)
                population.append(child)
                rodstat += 1
                #print(mamka.name, "и", papka.name, "родили ребёнка и назвали его", child.name,". Это" , child.pol )

                  if food > 0:
            migrants = int(food/10000)
            for i in range(migrants):
                population.append(villager())
                immigration += 1
'''