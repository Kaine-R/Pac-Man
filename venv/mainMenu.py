import pygame
import pygame.font
from introduceGhosts import IntroGhosts

class Menu():
    def __init__(self, screen, settings):
        self.screen, self.settings = screen, settings
        self.names = IntroGhosts(screen, settings)
        self.scores = [50000, 30000, 10000, 5000, 2000, 1000, 500, 300, 200, 100, 0]
        self.font = pygame.font.SysFont(None, 80, True, True)
        self.smallFont = pygame.font.SysFont(None, 48)
        self.title = self.font.render("PACMAN", True, (250, 250, 250))
        self.titleRect = self.title.get_rect()
        self.titleRect.x, self.titleRect.y = 2* settings.screenWidth /7, settings.screenHeight /9
        self.bg = (0, 0, 0)
        self.timer = 0
        self.showHS = False

        self.pacImage = [pygame.image.load("image/pacman3.png"), pygame.image.load("image/pacman2.png"), pygame.image.load("image/pacman1.png")]
        self.pacRect = self.pacImage[0].get_rect()
        self.pacRect.x, self.pacRect.y = - settings.screenWidth /4, settings.screenHeight /3
        self.pacDirection = 1

        self.allGhostImage = pygame.image.load("image/ghostAll.png")
        self.allGhostBlueImage = pygame.image.load("image/ghostAllBlue.png")
        self.allEyesImage = pygame.image.load("image/eyeAll.png")
        self.allEyesRect = self.allEyesImage.get_rect()
        self.allEyesRect.x, self.allEyesRect.y = - settings.screenWidth /2, settings.screenHeight /3 + 10
        self.allGhostRect = self.allGhostImage.get_rect()
        self.allGhostRect.x, self.allGhostRect.y = - settings.screenWidth /2, settings.screenHeight /3

    def checkShowHS(self, tempBool):
        self.showHS = tempBool

    def update(self):
        if self.timer > 900:
            self.timer = 0
        else:
            self.timer += 1
        self.pacRect.x += 2 * self.pacDirection
        self.allGhostRect.x += 2 * self.pacDirection
        self.allEyesRect.x += 2 * self.pacDirection
        if self.pacRect.x >= self.settings.screenWidth *2:
            self.pacDirection = -1
            self.flipPac()
            self.allEyesImage = pygame.transform.flip(self.allEyesImage, True, False)
        elif self.pacRect.x <= 0 - self.settings.screenWidth:
            self.pacDirection = 1
            self.flipPac()
            self.allEyesImage = pygame.transform.flip(self.allEyesImage, True, False)

    def flipPac(self):
        self.pacImage[0] = pygame.transform.flip(self.pacImage[0], True, False)
        self.pacImage[1] = pygame.transform.flip(self.pacImage[1], True, False)
        self.pacImage[2] = pygame.transform.flip(self.pacImage[2], True, False)

    def blit(self):
        self.screen.fill(self.bg)
        self.screen.blit(self.title, self.titleRect)
        if not self.showHS:
            if self.timer %31 <= 10:
                self.screen.blit(self.pacImage[0], self.pacRect)
            elif self.timer %31 <= 20:
                self.screen.blit(self.pacImage[1], self.pacRect)
            elif self.timer %31 <= 30:
                self.screen.blit(self.pacImage[2], self.pacRect)

            if self.pacDirection == 1:
                self.screen.blit(self.allGhostImage, self.allGhostRect)
            else:
                self.screen.blit(self.allGhostBlueImage, self.allGhostRect)
            self.screen.blit(self.allEyesImage, self.allEyesRect)

            self.names.blit()
        else:
            self.showScores()
            
    def showScores(self):
        self.prepScores()
        for i in range(len(self.scores)):
            self.screen.blit(self.scoreImages[i], self.scoreRect[i])


    def prepScores(self):
        self.scoreImages = []
        self.scoreRect = []
        xShift, yShift = 100, 200
        for score in self.scores:
            tempImage = self.smallFont.render("Score: " + str(score), True, (250, 250, 250))
            self.scoreImages.append(tempImage)
            tempRect = tempImage.get_rect()
            tempRect.x, tempRect.y = xShift, yShift
            yShift += 40
            self.scoreRect.append(tempRect)


    def changeScores(self, newScore):
        self.scores.append(newScore)
        self.scores.sort(reverse=True)
        self.scores.pop(len(self.scores) -1)
