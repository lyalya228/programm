
import pygame as pg
import pygame.sprite

pg.init()
size = W, H = 500, 500
win = pg.display.set_mode(size)

fon = pg.image.load('fon.png')
fon = pg.transform.scale(fon, (600, 500))


meteor = pg.image.load('bolshoi_meteorit.png')

meteor = pg.transform.scale(meteor, (700, 700))

fond = pg.image.load('fond.png')

yoda = pg.image.load('yoda_v_bochke.png')

yoda = pg.transform.scale(yoda, (250, 250))

samolet = pg.image.load('razbiti_samolet.png')

samolet = pg.transform.scale(samolet, (500, 500))

y = 250
x = 250
x_meteor = 600
x_samolet = 1000
y2 = 450
x2 = 450
death = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    win.fill("black")
    if death == 1:
        win.blit(fond, (0, 0))
    else:
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            y -= 3
        elif keys[pg.K_DOWN]:
            y += 3

        win.blit(fon, (0, 0))
        win.blit(meteor, (750, 352))


        x_meteor -= 2
        x_samolet -= 2

        if x_meteor < -450:
            x_meteor = 600

        if x_samolet < -450:
            x_samolet = 600


        if 200 < y < 300 and -300 < x_meteor < 0:
            death = 1

        elif -75 < y < 65 and -270 < x_samolet < 50:
            death = 1


        win.blit(yoda, (0, y))
        win.blit(samolet, (x_samolet, 20))
        win.blit(meteor, (x_meteor, 100))
    pg.time.delay(10)
    pg.display.update()