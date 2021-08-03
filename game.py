import pygame

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('draughts game')

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
        pygame.quit()
