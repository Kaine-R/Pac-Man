import pygame
from pygame.sprite import Sprite


class Dot(Sprite):
    def __init__(self, screen, settings):
        super(Dot, self).__init__()
        self.screen, self.settings = screen, settings

        self.image = pygame.image.load("image/dot.png")
        self.image = pygame.transform.scale(self.image, (settings.rectSize -5, settings.rectSize -5))
        self.rect = self.image.get_rect()




    def blit(self):
        self.screen.blit(self.image, self.rect)