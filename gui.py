import pygame
import snake
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
    for x,y in had:
        vykresli_ctverecek(x,y,(0,0,255))
    vykresli_ctverecek(x,y,(255,0,0))

had = snake.had()
vykresli(had,set())

        
pygame.display.flip()

