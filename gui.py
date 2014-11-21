import pygame
import snake
from random import randint
from pygame.locals import *
pygame.init()
okno = 500
velikost_policka = 50
pocet_pole = 10
screen = pygame.display.set_mode((okno,okno))

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


while True:
    vykresli(had,jidlo)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                snake.pohyb("dolu", had, jidlo)
            elif event.key == K_UP:
                snake.pohyb("nahoru", had, jidlo)
            if event.key == K_LEFT:
                snake.pohyb("vlevo", had, jidlo)
            if event.key == K_RIGHT:
                snake.pohyb("vpravo", had, jidlo)
            
    pygame.display.flip()

