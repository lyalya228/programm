
import pygame as pg

pg.init()
size = W, H = 500, 500
win = pg.display.set_mode(size)

fon = pg.image.load('fon.png')
fon = pg.transform.scale(fon, (600, 500))


meteor = pg.image.load('bolshoi_meteorit.png')

meteor = pg.transform.scale(meteor, (700, 700))

yoda = pg.image.load('yoda_v_bochke.png')

yoda = pg.transform.scale(yoda, (250, 250))

samolet = pg.image.load('razbiti_samolet.png')

samolet = pg.transform.scale(samolet, (500, 500))

y = 250
x = 250

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    win.fill("black")

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        y -= 3
    elif keys[pg.K_DOWN]:
        y += 3

    win.blit(fon, (0, 0))
    win.blit(meteor, (750, 352))
    if meteor.

    win.blit(yoda, (0, y))
    win.blit(samolet, (675, 437))
    pg.time.delay(10)
    pg.display.update()