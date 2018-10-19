import pygame
import pygame.font

class Details():
    def __init__(self, screen, settings):
        self.screen, self.settings = screen, settings
        self.bg = pygame.Rect(2, 2, settings.screenWidth, 35)
        self.color = (40, 80, 60)
        self.font = pygame.font.SysFont(None, 48)
        self.roundFont = pygame.font.SysFont(None, 68)
        self.fontColor = (10, 10, 10)
        self.show = [True, True, True]

        self.livesImage = self.font.render("Lives: ", True, self.fontColor)
        self.livesRect = pygame.Rect(5, 2, 20, 20)
        self.lifeImage = pygame.image.load("image/pacman3.png")
        self.lifeImage = pygame.transform.scale(self.lifeImage, (30, 30))
        self.life1Rect = pygame.Rect(110, 2, 20, 20)
        self.life2Rect = pygame.Rect(140, 2, 20, 20)
        self.life3Rect = pygame.Rect(170, 2, 20, 20)
        self.scoreImage = self.font.render("Score: 0", True, self.fontColor)
        self.scoreRect = pygame.Rect(400, 2, 20, 20)

        self.nextRound = False
        self.roundImage = self.roundFont.render("Round: 2", True, (0, 0, 0), (175, 175, 215))
        self.roundRect = self.roundImage.get_rect()
        self.roundRect.x, self.roundRect.y = settings.screenWidth /3 + 10, 3* settings.screenHeight/7


    def prep(self, gameStats):
        self.scoreImage = self.font.render("Score: " + str(gameStats.score), True, self.fontColor)
        if gameStats.lives == 2:
            self.show[2] = False
        elif gameStats.lives == 1:
            self.show[1] = False
        elif gameStats.lives == 0:
            self.show[0] = False
        if gameStats.nextRound:
            self.roundImage = self.roundFont.render("Round: " + str(gameStats.round), True, (0, 0, 0), (175, 175, 215))
            self.nextRound = True
        else:
            self.nextRound = False

    def blit(self):
        pygame.draw.rect(self.screen, self.color, self.bg)
        self.screen.blit(self.livesImage, self.livesRect)
        self.screen.blit(self.scoreImage, self.scoreRect)
        if self.show[0]== True:
            self.screen.blit(self.lifeImage, self.life1Rect)
        if self.show[1]== True:
            self.screen.blit(self.lifeImage, self.life2Rect)
        if self.show[2]== True:
            self.screen.blit(self.lifeImage, self.life3Rect)

        if self.nextRound == True:
            self.screen.blit(self.roundImage, self.roundRect)
