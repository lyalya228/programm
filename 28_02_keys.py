import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x=250
y=250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_UP]:
        y -= 3
    elif keys[pygame.K_DOWN]:
        y += 3
    else:
        x = 250
        y = 250

    color = (0, 0, 255)

    if x > 150 and y > 150 or x > 300 and y > 300:
        color = (255, 0, 0)
    else:
        color = (0, 0, 0)

    win.fill((0, 187, 97))
    pygame.draw.circle(win, color, (x,y),  30)

    pygame.time.delay(10)
    pygame.display.update()