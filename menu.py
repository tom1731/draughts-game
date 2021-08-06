import pygame
from game import Game

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('draughts game')


class Menu:

    def __init__(self):

        self.buttons = []
        self.buttons.append(Button('data/images/quit.png', (20, 100), 'local pvp'))
        self.buttons.append(Button('data/images/quit.png', (20, 200), 'local pve'))
        self.buttons.append(Button('data/images/quit.png', (20, 300), 'online pvp'))
        self.buttons.append(Button('data/images/quit.png', (20, 400), 'quit'))

    def run(self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print(event.pos)
                        for obj in self.buttons:
                            obj.activate(event.pos)

            for button in self.buttons:
                button.display()

            pygame.display.flip()

        pygame.quit()


class Button:

    def __init__(self, img, pos, action):
        self.img = img
        self.pos = pos
        self.action = action

        self.sprite = pygame.image.load(img).convert()
        self.sprite.set_colorkey([0, 0, 255])

        self.rect = self.sprite.get_rect(topleft=self.pos)

        print(self.rect)

    def activate(self, pos):
        if self.rect.collidepoint(pos):
            print('touching ' + self.action + ' button!')
            if self.action == 'quit':
                pygame.quit()

    def display(self):
        screen.blit(self.sprite, self.pos)
