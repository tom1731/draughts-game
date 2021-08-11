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
            self.selection.move(pos)
            self.selection = None




class Board:

    def __init__(self):
        self.board = pygame.image.load('data/images/board.jpg').convert()
        self.origin = (41, 41)
        self.width = 52.6
        self.heigh = 51.9
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
        pos_white = [(9, 0), (9, 2), (9, 4), (9, 6), (9, 8),
                     (8, 1), (8, 3), (8, 5), (8, 7), (8, 9),
                     (7, 0), (7, 2), (7, 4), (7, 6), (7, 8),
                     (6, 1), (6, 3), (6, 5), (6, 7), (6, 9)]

        pos_black = [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9),
                     (1, 0), (1, 2), (1, 4), (1, 6), (1, 8),
                     (2, 1), (2, 3), (2, 5), (2, 7), (2, 9),
                     (3, 0), (3, 2), (3, 4), (3, 6), (3, 8)]

        for pos in pos_white:
            self.list_pawns.append(Pawn('white', pos, self.origin))

        for pos in pos_black:
            self.list_pawns.append(Pawn('black', pos, self.origin))

    def display(self, screen):
        screen.blit(self.board, (0, 0))
        for pawn in self.list_pawns:
            pawn.display(screen)


class Pawn:

    def __init__(self, color, pos, origin):
        if color == 'white':
            self.sprite = pygame.image.load('data/images/white.png').convert()
        elif color == 'black':
            self.sprite = pygame.image.load('data/images/black.png').convert()
        self.sprite.set_colorkey([0, 0, 255])

        self.pos = pos
        self.board_origin = origin
        self.x = self.board_origin[0] + self.pos[1] * 53
        self.y = self.board_origin[1] + self.pos[0] * 52

        self.type = 'pawn'
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))

    def display(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def select(self):
        pass

    def move(self, pos):
        self.x = pos[0] - 26
        self.y = pos[1] - 26
        self.rect.update(self.x, self.y, 52, 52 )

    def kill(self):
        pass

    def upgrade(self):
        self.type = 'draught'
