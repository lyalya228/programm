
import pygame as pg

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

    x_meteor -= 2
    x_samolet -= 2

    if x_meteor < -450:
        x_meteor = 600

    if x_samolet < -450:
        x_samolet = 600

    if x2 < yoda.get_rect() < x2 + 675 and y2 < yoda < y2 + 675:
        win.blit(yoda, (10000, 10000))
        win.blit(samolet, (10000, 10000))
        win.blit(meteor, (10000, 1000))
        win.blit(fond, (500, 500))

    win.blit(yoda, (0, y))
    win.blit(samolet, (x_samolet, 20))
    win.blit(meteor, (x_meteor, 100))
    pg.time.delay(100)
    pg.display.update()