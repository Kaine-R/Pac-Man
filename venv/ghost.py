import pygame
from pygame.sprite import Sprite


class Ghost():
    def __init__(self, screen, settings):
        super(Ghost, self).__init__()
        self.screen, self.settings = screen, settings
        
        self.image = [pygame.image.load("image/ghostBlue.png"), pygame.image.load("image/ghostBlue.png"), pygame.image.load("image/ghostWhite.png")]
        self.rect = self.image[0].get_rect()
        self.x, self.y = 300, 360
        self.rect.centerx, self.rect.y = self.x, self.y
        self.type = 0
        self.moveDirection = 1
        self.lastAxis = 0
        self.timer = 0
        self.setTimer = False
        self.diff = 0
        self.openWays = [False, False, False, False]
        self.instructions = 0
        # direction 0 = up, 1 = right, 2 = down, 3 = left
        self.pacX, self.pacY = 0, 0

    def prep(self):
        if self.type == 0:
            self.image[0] = pygame.image.load("image/ghostLBlue.png")
        elif self.type == 1:
            self.image[0] = pygame.image.load("image/ghostPink.png")
        elif self.type == 2:
            self.image[0] = pygame.image.load("image/ghostRed.png")
        else:
            self.image[0] = pygame.image.load("image/ghostYellow.png")

    def addDiff(self):
        self.diff +=.3

    def resetDiff(self):
        self.diff = 0

    def reset(self):
        self.x, self.y = 300, 360
        self.x += 30*self.type
        self.instructions = 0
        self.resetDiff

    def update(self, gameStats):  # #4 (clyde) s the calmest
        self.pacX, self.pacY = gameStats.pacPosX +20, gameStats.pacPosY +20
        if self.instructions == 0:
            self.instruct0_0()
        elif self.instructions == 1:
            self.instruct0_1()
        elif self.instructions == 2:
            self.instruct0_2()
        elif self.instructions == 3:
            self.instruct0_3()
        elif self.instructions == 4:
            self.instruct0_4()
        elif self.instructions == 5:
            self.basicDown()
        elif self.instructions == 6:
            self.basicLeft()
        elif self.instructions == 7:
            self.basicUp()
        elif self.instructions == 8:
            self.basicRight()
        elif self.instructions == 10:
            self.simpleAI()
        elif self.instructions == 11:
            self.instruct1_2()
        elif self.instructions == 12:
            self.instruct1_3()
        elif self.instructions == 13:
            self.instruct1_4()
        self.rect.centerx, self.rect.y = self.x, self.y

    def instruct0_0(self):
        if self.type == 0:
            if round(self.x) == self.settings.screenWidth / 2:
                self.moveUp()
                if self.y > 300:
                    self.instructions = 1
            else:
                self.moveRight()
        elif self.type == 1:
            if round(self.x) == self.settings.screenWidth / 2:
                self.moveUp()
                if self.y > 300:
                    self.instructions = 1
            else:
                self.moveRight()
        elif self.type == 2:
            if round(self.x) == self.settings.screenWidth / 2:
                self.moveUp()
                if self.y > 300:
                    self.instructions = 1
            else:
                self.moveLeft()
        else:
            if round(self.x) == self.settings.screenWidth / 2:
                self.moveUp()
                if self.y > 300:
                    self.instructions = 1
            else:
                self.moveLeft()

    def instruct0_1(self):
        self.moveUp()
        if round(self.y) == 295:
            if self.type == 1 or self.type == 2:
                self.instructions = 11
            else:
                self.instructions = 2

    def instruct0_2(self):
        self.moveRight()
        if round(self.x) == self.settings.screenWidth / 2 + 115:
            self.instructions = 3

    def instruct0_3(self):
        self.moveDown()
        if round(self.y) == self.settings.screenHeight / 2 - 30:
            self.instructions = 4

    def instruct0_4(self):
        self.moveRight()
        if round(self.x) == self.settings.screenWidth / 2 + 190:
            if self.type == 0 or self.type == 2:
                self.instructions = 10
            elif self.type == 1:
                self.instructions = 7
            else:
                self.instructions = 5

    def instruct1_2(self):
        self.moveLeft()
        if round(self.x) == 235:
            self.instructions = 12

    def instruct1_3(self):
        self.moveDown()
        if round(self.y) == 370:
            self.instructions = 13

    def instruct1_4(self):
        self.moveLeft()
        if round(self.x) == 155:
            if self.type == 0 or self.type == 2:
                self.instructions = 10
            elif self.type == 1:
                self.instructions = 5
            else:
                self.instructions = 5

    def basicDown(self):
        self.moveDown()
        if round(self.y) == self.settings.screenHeight / 2 + 200:
            if self.type == 1:
                self.instructions = 8
            else:
                self.instructions = 6

    def basicLeft(self):
        self.moveLeft()
        if round(self.x) == self.settings.screenWidth / 2 - 190:
            if self.type == 1:
                self.instructions = 5
            else:
                self.instructions = 7

    def basicUp(self):
        self.moveUp()
        if round(self.y) == self.settings.screenHeight / 2 - 250:
            if self.type == 1:
                self.instructions = 6
            else:
                self.instructions = 8

    def basicRight(self):
        self.moveRight()
        if round(self.x) == self.settings.screenWidth / 2 + 190:
            if self.type == 1:
                self.instructions = 7
            else:
                self.instructions = 5

    def simpleAI(self):
        if self.moveDirection == 0:
            self.moveUp()
        elif self.moveDirection == 1:
            self.moveRight()
        elif self.moveDirection == 2:
            self.moveDown()
        elif self.moveDirection == 3:
            self.moveLeft()

    def moveLeft(self):
        self.x -= self.settings.ghostSpeed + self.diff

    def moveRight(self):
        self.x += self.settings.ghostSpeed + self.diff

    def moveUp(self):
        self.y -= self.settings.ghostSpeed + self.diff

    def moveDown(self):
        self.y += self.settings.ghostSpeed + self.diff

    def blit(self):
        self.screen.blit(self.image[0], self.rect)

    def checkX(self):
        x = [35, 90, 155, 235, 305, 380, 455, 535, 605, 650]
        for i in range(int(len(x))):
            if round(self.x) == x[i]:
                pygame.draw.line(self.screen, (20, 250, 20), (x[i], 0), (x[i], 1000), 10)
                return True
        return False

    def checkY(self):
        y = [60, 145, 220, 295, 370, 445, 520, 600, 670, 750]
        for j in range(int(len(y))):
            if round(self.y) == y[j]:
                pygame.draw.line(self.screen, (20, 250, 20), (0, y[j]), (700, y[j]), 10)
                return True
        return False

