# -*- coding: utf-8 -*-
from random import randrange


def had():
    """vytvoří seznam pozic hada"""
    return [(1, 2), (2, 2), (3, 2)]

def pridej_zradlo(had, jidlo, velikost_pole = 10):
    while True:
        x = randrange(0, velikost_pole)
        y = randrange(0, velikost_pole)
        if (x,y) not in had and (x,y) not in jidlo:
            jidlo.add((x,y))
            return
            
def vykresli(had, jidlo, velikost_pole=10):
    print (10*"-")
    pole = [["."]*velikost_pole for i in range(velikost_pole)]
    for x, y in had[:-1]:
        pole[y][x] = "X"

    hlavicka = had[-1]
    pole[hlavicka[1]][hlavicka[0]] = "O"

    for x,y in jidlo:
        pole[y][x] = "?" 

    for radek in pole:
        print " ".join(radek)
        
    
def pohyb(smer,had, jidlo, velikost_pole=10):
    x, y = had[-1]
    if smer== "vpravo":
        x +=1
 
    elif smer=="nahoru":
        y -= 1

    elif smer == "dolu":
        y += 1

    elif smer == "vlevo":
        x -= 1

    else:
        raise ValueError("Špatný směr!")

    if x >= velikost_pole:
        x = 0
    elif x < 0:
        x = velikost_pole-1
    if y >= velikost_pole:
        y = 0
    elif y < 0:
        y = velikost_pole-1
    if (x,y) in had:
        raise ValueError("Game over!")
    if (x,y) in jidlo:
        jidlo.discard((x,y))
        pridej_zradlo(had, jidlo)
    else:    
        del had[0]
    had.append((x, y)) 


a = had()
jidlo=set()
pridej_zradlo(a, jidlo)

while True:
    vykresli(a,jidlo)
    s = raw_input("Zadej směr: ")
    pohyb(s, a,jidlo)
