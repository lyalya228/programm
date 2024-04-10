import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_board(self, win):
        pygame.draw.line(win, (0, 0, 0), (450/3, 0), (450/3, 450), 3)
        pygame.draw.line(win, (0, 0, 0), (450/3*2, 0), (450/3*2, 450), 3)
        pygame.draw.line(win, (0, 0, 0), (0, 450/3), (450, 450/3), 3)
        pygame.draw.line(win, (0, 0, 0), (0, 450/3*2), (450, 450/3*2), 3)

    def nolik(self):
        pygame.draw.circle(win, (255, 255, 255), pygame.mouse.get_pos(), 75)

    def krestik(self, pos):
        pygame.draw.line(win, (255, 255, 255), (pos[0] - 75, pos[1] - 75), (pos[0] + 75, pos[1] + 75), 6)
        pygame.draw.line(win, (255, 255, 255), (pos[0] - 75, pos[1] + 75), (pos[0] + 75, pos[1] - 75), 6)

board = Board(450, 450)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0, 187, 255))
    pos = pygame.mouse.get_pos()
    board.krestik(pos)
    board.nolik()
    keys = pygame.mouse.get_pressed()


    board.draw_board(win)

    if 0 < pos[0] < 150 and 0 < pos[1] < 150:
        board.krestik((75, 75))

    if pos[0] > 150 and pos[1] > 300:
        board.krestik(pos)

    if pos[0] > 150 and pos[1] > 450:
        board.krestik(pos)

    if pos[0] > 300 and pos[1] > 150:
        board.krestik()

    if pos[0] > 450 and pos[1] > 150:
        board.krestik(pos)

    if pos[0] > 300 and pos[1] > 300:
        board.krestik(pos)

    if pos[0] > 450 and pos[1] > 300:
        board.krestik(pos)

    if pos[0] > 300 and pos[1] > 450:
        board.krestik(pos)

     if pos[0] > 450 and pos[1] > 450:
        board.krestik(pos)

    pygame.display.update()
    pygame.time.delay(15)