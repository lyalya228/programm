import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))


class Board:
    def __init__(self, width, height, dek):
        self.width = width
        self.height = height
        self.dek = dek

    def draw_board(self, win):
        pygame.draw.line(win, (0, 0, 0), (450/3, 0), (450/3, 450), 3)
        pygame.draw.line(win, (0, 0, 0), (450/3*2, 0), (450/3*2, 450), 3)
        pygame.draw.line(win, (0, 0, 0), (0, 450/3), (450, 450/3), 3)
        pygame.draw.line(win, (0, 0, 0), (0, 450/3*2), (450, 450/3*2), 3)

    def nolik(self, pos):
        pygame.draw.circle(win, (255, 255, 255), pos, 75)

    def krestik(self, pos):
        pygame.draw.line(win, (255, 255, 255), (pos[0] - 75, pos[1] - 75), (pos[0] + 75, pos[1] + 75), 6)
        pygame.draw.line(win, (255, 255, 255), (pos[0] - 75, pos[1] + 75), (pos[0] + 75, pos[1] - 75), 6)

board = Board(450, 450)
brah = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill('blue')
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()
    board.draw_board(win)

    if pygame.mouse.get_pressed()[0] and brah%2 != 0:
        brah = brah + 1
        if 0 < pos[0] < 150 and 0 < pos[1] < 150:
            board.nolik((75, 75))

        if 150 < pos[0] < 300 and 0 < pos[1] < 150:
            board.nolik((225, 75))

        if 300 < pos[0] < 450 and 0 < pos[1] < 150:
            board.nolik((375, 75))

        if 0 < pos[0] < 150 and 150 < pos[1] < 300:
            board.nolik((75, 225))

        if 0 < pos[0] < 150 and 300 < pos[1] < 450:
            board.nolik((75, 375))

        if 150 < pos[0] < 300 and 150 < pos[1] < 300:
            board.nolik((225, 225))

        if 150 < pos[0] < 300 and 300 < pos[1] < 450:
            board.nolik((225, 375))

        if 300 < pos[0] < 450 and 150 < pos[1] < 300:
            board.nolik((375, 225))

        if 300 < pos[0] < 450 and 300 < pos[1] < 450:
            board.nolik((375, 375))

    elif pygame.mouse.get_pressed()[0] and brah%2 == 0:
        brah = brah + 1
        if 0 < pos[0] < 150 and 0 < pos[1] < 150:
            board.krestik((75, 75))

        if 150 < pos[0] < 300 and 0 < pos[1] < 150:
            board.krestik((225, 75))

        if 300 < pos[0] < 450 and 0 < pos[1] < 150:
            board.krestik((375, 75))

        if 0 < pos[0] < 150 and 150 < pos[1] < 300:
            board.krestik((75, 225))

        if 0 < pos[0] < 150 and 300 < pos[1] < 450:
            board.krestik((75, 375))

        if 150 < pos[0] < 300 and 150 < pos[1] < 300:
            board.krestik((225, 225))

        if 150 < pos[0] < 300 and 300 < pos[1] < 450:
            board.krestik((225, 375))

        if 300 < pos[0] < 450 and 150 < pos[1] < 300:
            board.krestik((375, 225))

        if 300 < pos[0] < 450 and 300 < pos[1] < 450:
            board.krestik((375, 375))

    pygame.display.update()
    pygame.time.delay(100)