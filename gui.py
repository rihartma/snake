import pygame
import snake
from time import time
from pygame.locals import *
pygame.init()
vodorovne = 20
svisle = 10
velikost_policka = 50
pocet_pole = 10
screen = pygame.display.set_mode((vodorovne*50,svisle*50))

def vykresli_ctverecek(x,y,color):
    screen.fill(color,pygame.Rect(
            x*velikost_policka,
            y*velikost_policka,
            velikost_policka,velikost_policka))

def vykresli(had,jidlo):
    screen.fill((0,0,0))
    for x,y in had:
        vykresli_ctverecek(x,y,(0,0,255))
    vykresli_ctverecek(x,y,(255,0,0))

    for x,y in jidlo:
        vykresli_ctverecek(x,y,(0,255,0))


had = snake.had()
jidlo=set()
snake.pridej_zradlo(had, jidlo)
smer = "dolu"
cas = time()
ukoly = []
smer = "vpravo"
while True:
    if time()-cas > .1:
        cas = time()
        if len(ukoly):
            smer = ukoly[0]
            del ukoly[0]
        snake.pohyb(smer, had, jidlo,vodorovne,svisle)
        vykresli(had,jidlo)
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                ukoly.append("dolu")
            elif event.key == K_UP:
                ukoly.append("nahoru")
            if event.key == K_LEFT:
                ukoly.append("vlevo")
            if event.key == K_RIGHT:
                ukoly.append("vpravo")
    pygame.display.flip()

