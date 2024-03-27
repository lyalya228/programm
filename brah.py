import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
win.fill((0, 187, 97))


class Circle:
    def __init__(self, surface, color, x, y, radius, dir):
        self.surface = surface
        self.color = color
        self.radius = radius
        self.y = y
        self.x = x
        self.dir = dir

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3
        elif keys[pygame.K_UP]:
            self.y -= 3
        elif keys[pygame.K_DOWN]:
            self.y += 3

    def rikoshet(self):
        self.x = self.x + 1 * self.dir
        if self.x > 500:
            self.dir = -1
        if self.x < 0:
            self.dir = 1

    win.fill((0, 187, 97))

w, h = 10, 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    mouse = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()


    if keys[0] == True:
        pygame.draw.rect(win, (255, 255, 0), (mouse[0], mouse[1], w, h))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        w = w + 2
        h = h + 2
    if keys[pygame.K_z]:
        w = w - 2
        h = h - 2

    if keys[pygame.K_SPACE]:
        win.fill((0, 187, 97))


    pygame.time.delay(10)
    pygame.display.update()
