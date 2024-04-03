import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_board(self, win):
        pygame.draw.line(win, (0, 0, 0), (500/3, 0), (500/3, 500), 3)
        pygame.draw.line(win, (0, 0, 0), (500/3*2, 0), (500/3*2, 500), 3)
        pygame.draw.line(win, (0, 0, 0), (0, 500/3), (500, 500/3), 3)
        pygame.draw.line(win, (0, 0, 0), (0, 500/3*2), (500, 500/3*2), 3)

    def nolik(self):
        pygame.draw.circle(win, (255, 255, 255), pygame.mouse.get_pos(), 30)

    def krestik(self):
        pygame.draw.line(win, (255, 255, 255), )


board = Board(500, 500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0, 187, 255))
    mouse = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()

    board.draw_board(win)

    board.nolik()

    pygame.display.update()
    pygame.time.delay(15)
