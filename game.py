import pygame


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('draughts game')

    def run(self):
        running = True
        board = Board()
        selection = Selection(board.origin, board.width, board.heigh)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        selection.click(event.pos, board)

            board.display(self.screen)
            selection.display(self.screen)
            pygame.display.flip()


class Selection:

    def __init__(self, origin, width, heigh):
        self.origin = origin
        self.width = width
        self.heigh = heigh
        self.pos = (10, 10)
        self.selection = None

    def display(self, screen):
        if self.selection is not None:
            pygame.draw.rect(screen,
                             (0, 0, 255),
                             (self.selection.x, self.selection.y, self.width, self.heigh),
                             width=3)

    def click(self, pos, board):
        # self.pos = (
        #     (pos[0] - self.origin[0]) // self.width * self.width + self.origin[0],
        #     (pos[1] - self.origin[1]) // self.heigh * self.heigh + self.origin[1]
        # )
        if self.selection is None:
            i = 0
            for pawn in board.list_pawns:
                if pawn.rect.collidepoint(pos):
                    self.selection = pawn
                    break
                i += 1
                print(i)
                # self.selection = None
        else:
            new_selection = False
            for pawn in board.list_pawns:
                if pawn.rect.collidepoint(pos):
                    self.selection = pawn
                    new_selection = True
            if new_selection is False:
                for case in board.list_cases:
                    if case.collidepoint(pos):
                        self.selection.move(case.center)
                        self.selection = None


class Board:

    def __init__(self):
        self.board = pygame.image.load('data/images/board.jpg').convert()
        self.origin = (41, 41)
        self.dim = (52, 52)
        self.width = 52.6
        self.heigh = 51.9
        self.list_cases = []
        self.list_pawns = []
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.setup()

    def setup(self):

        pos_white = list(range(30, 50))

        pos_black = list(range(20))

        origin = self.origin

        for row in range(10):
            if row % 2 == 0:
                origin = (origin[0] - self.dim[0], origin[1])
            else:
                origin = (origin[0] - self.dim[0] * 2, origin[1])

            for col in range(5):
                origin = (origin[0] + self.dim[0] * 2, origin[1])
                self.list_cases.append(pygame.Rect(origin, self.dim))
            origin = (self.origin[0], origin[1] + self.dim[1])

        for pos in pos_white:
            self.list_pawns.append(Pawn('white', self.list_cases[pos]))

        for pos in pos_black:
            self.list_pawns.append(Pawn('black', self.list_cases[pos]))

    def display(self, screen):

        screen.blit(self.board, (0, 0))

        for box in self.list_cases:
            pygame.draw.rect(screen, (255, 0 , 0), box)

        for pawn in self.list_pawns:
            pawn.display(screen)


class Pawn:

    def __init__(self, color, case):
        if color == 'white':
            self.sprite = pygame.image.load('data/images/white.png').convert()
        elif color == 'black':
            self.sprite = pygame.image.load('data/images/black.png').convert()
        self.sprite.set_colorkey([0, 0, 255])

        self.rect = self.sprite.get_rect(center=case.center)
        self.x = self.rect.center[0] - self.rect.w / 2
        self.y = self.rect.center[1] - self.rect.h / 2
        self.type = 'pawn'

    def display(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def select(self):
        pass

    def move(self, pos):
        self.x = pos[0] - self.rect.w / 2
        self.y = pos[1] - self.rect.h / 2
        self.rect.update(self.x, self.y, self.rect.w, self.rect.h)

    def kill(self):
        pass

    def upgrade(self):
        self.type = 'draught'
