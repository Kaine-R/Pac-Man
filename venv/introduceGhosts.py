import pygame
import pygame.font

class IntroGhosts():
    def __init__(self, screen, settings):
        self.screen, self.settings = screen, settings
        self.font = pygame.font.SysFont(None, 50, False, True)
        self.names = ["Blinky", "Pinky", "Inkey", "Clyde"]
        self.ghostImages = [pygame.image.load("image/ghostRed.png"), pygame.image.load("image/ghostPink.png"), pygame.image.load("image/ghostLBlue.png"), pygame.image.load("image/ghostYellow.png")]
        self.ghostRect = [self.ghostImages[0].get_rect(), self.ghostImages[1].get_rect(), self.ghostImages[2].get_rect(), self.ghostImages[3].get_rect()]
        self.nameImage = []
        self.nameRect = []
        xShift, yShift = settings.screenWidth /5, 2* settings.screenHeight /5
        for i in range(4):
            image = self.font.render(self.names[i], True, (250, 250, 250))
            self.nameImage.append(image)
            rect = image.get_rect()
            rect.x, rect.y = xShift, yShift
            self.ghostRect[i].x, self.ghostRect[i].y = rect.right + 10, rect.y
            xShift += 2* settings.screenWidth/5
            self.nameRect.append(rect)
            if i == 1:
                xShift = settings.screenWidth /5
                yShift += settings.screenHeight /5

    def blit(self):
        for i in range(len(self.nameImage)):
            self.screen.blit(self.nameImage[i], self.nameRect[i])
            self.screen.blit(self.ghostImages[i], self.ghostRect[i])
