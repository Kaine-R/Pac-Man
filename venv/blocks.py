import pygame
from pygame.sprite import Sprite


class Blocks(Sprite):
    def __init__(self, screen):
        super(Blocks, self).__init__()
        self.screen = screen
        self.color = (20, 40, 100)
        self.gateColor = (10, 20, 50)
        self.rect = pygame.Rect(50, 50, 15, 15)
        self.type = 0
        
    def draw(self):
        if self.type == 0:
            pygame.draw.rect(self.screen, self.color, self.rect)
        elif self.type == 1:
            pygame.draw.rect(self.screen, self.gateColor, self.rect)