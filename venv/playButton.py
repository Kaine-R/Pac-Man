import pygame
import pygame.font

class Play():
    def __init__(self, screen, settings):
        self.showBack = False
        self.screen, self.settings = screen, settings
        self.font = pygame.font.SysFont(None, 60)
        self.image = self.font.render("Play", True, (250, 250, 250))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 2* settings.screenWidth /5, 6* settings.screenHeight /7

        self.HSimage = self.font.render("HighScore", True, (250, 250, 250))
        self.HSrect = self.HSimage.get_rect()
        self.HSrect.x, self.HSrect.y = settings.screenWidth /3, 10* settings.screenHeight /11
        
        self.backImage = self.font.render("Back", True, (250, 250, 250))
        self.backRect = self.backImage.get_rect()
        self.backRect.x, self.backRect.y = 2* settings.screenWidth /5, 10* settings.screenHeight /11

    def hideRect(self):
        if self.showBack:
            self.HSrect.x, self.HSrect.y = -100, -100
        else:
            self.HSrect.x, self.HSrect.y = self.settings.screenWidth / 3, 10 * self.settings.screenHeight / 11

    def blit(self):
        self.screen.blit(self.image, self.rect)
        if self.showBack:
            self.hideRect()
            self.screen.blit(self.backImage, self.backRect)
        else:
            self.hideRect()
            self.screen.blit(self.HSimage, self.HSrect)
