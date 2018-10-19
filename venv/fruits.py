import pygame


class Fruit():
    def __init__(self, screen, settings):
        super(Fruit, self).__init__()
        self.screen, self.settings = screen, settings
        self.image = [pygame.image.load("image/fruit1.png"), pygame.image.load("image/fruit2.png"), pygame.image.load("image/fruit3.png")]
        self.image[0] = pygame.transform.scale(self.image[0], (settings.rectSize *2, settings.rectSize *2))
        self.image[1] = pygame.transform.scale(self.image[1], (settings.rectSize *2, settings.rectSize *2))
        self.image[2] = pygame.transform.scale(self.image[2], (settings.rectSize *2, settings.rectSize *2))
        self.rect = self.image[0].get_rect()
        self.rect.x, self.rect.y = 300, 300
        self.type = 0

    def blit(self, gameStats):
        if gameStats.fruitPresent == True:
            self.rect.x, self.rect.y = 330, 445
            self.screen.blit(self.image[self.type], self.rect)
        else:
            self.rect.x, self.rect.y = -100, -100
