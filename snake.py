# -*- coding: utf-8 -*-
from random import randrange


def had():
    """vytvoří seznam pozic hada"""
    return [(1, 2), (2, 2), (3, 2)]

def pridej_zradlo(had, jidlo,vodorovne = 10,svisle = 10):
    while True:
        x = randrange(0, vodorovne)
        y = randrange(0, svisle)
        if (x,y) not in had and (x,y) not in jidlo:
            jidlo.add((x,y))
            return
            
def vykresli(had, jidlo,vodorovne = 10,svisle = 10):
    print (10*"-")
    pole = [["."]*vodorovne for i in range(svisle)]
    for x, y in had[:-1]:
        pole[y][x] = "X"

    hlavicka = had[-1]
    pole[hlavicka[1]][hlavicka[0]] = "O"

    for x,y in jidlo:
        pole[y][x] = "?" 

    for radek in pole:
        print " ".join(radek)
        
    
def pohyb(smer,had, jidlo, vodorovne,svisle):
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

    if x >= vodorovne:
        x = 0
    elif x < 0:
        x = vodorovne - 1
    if y >= svisle:
        y = 0
    elif y < 0:
        y = svisle - 1
    if (x,y) in had:
        raise ValueError("Game over!")
    if (x,y) in jidlo:
        jidlo.discard((x,y))
        pridej_zradlo(had, jidlo,vodorovne,svisle)
    else:    
        del had[0]

    had.append((x, y)) 



