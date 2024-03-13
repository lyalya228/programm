import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
win.fill((0, 187, 97))


class Circle:
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        self.color = color
        self.radius = radius
        self.y = y
        self.x = x

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


bob = Circle(win, (255, 255, 255), 250, 250, 30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0, 187, 97))
    bob.draw()
    bob.move_by_keys()
    pygame.display.update()
    pygame.time.delay(10)