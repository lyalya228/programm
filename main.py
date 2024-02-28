import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 0
y = 225

x1 = 225
y1 = 0
dir = 1
dir1 = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = x + 1 * dir
    if x > 500:
        dir = -1
    if x < 0:
        dir = 1

    color = (177, 100, 255)
    win.fill(color)
    pygame.draw.rect(win, (255, 255, 0), (x, y, 75, 75))

    y1 = y1 + 1 * dir1
    if y1 > 500:
       dir1 = -1
    if y1 < 0:
        dir1 = 1


    pygame.draw.circle(win, (0, 255, 255), (x1, y1), 30)
    pygame.display.update()
    pygame.time.delay(5)