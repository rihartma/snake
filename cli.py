import snake
a = snake.had()
jidlo=set()
snake.pridej_zradlo(a, jidlo)

while True:
    snake.vykresli(a,jidlo)
    s = raw_input("Zadej směr: ")
    snake.pohyb(s, a,jidlo)
