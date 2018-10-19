import pygame


class Player():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = [pygame.image.load("image/pacman1.png"), pygame.image.load("image/pacman2.png"), pygame.image.load("image/pacman3.png")]
        self.image[0] = pygame.transform.scale(self.image[0], (settings.playerSize, settings.playerSize))
        self.image[1] = pygame.transform.scale(self.image[1], (settings.playerSize, settings.playerSize))
        self.image[2] = pygame.transform.scale(self.image[2], (settings.playerSize, settings.playerSize))
        self.x, self.y = 330, 445
        self.rect = self.image[0].get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        # Bools for movement
        self.movementLeft = False
        self.movementRight = False
        self.movementUp = False
        self.movementDown = False

    def update(self):
        if self.movementRight:
            self.x += self.settings.playerSpeed
        if self.movementLeft:
            self.x -= self.settings.playerSpeed
        if self.movementUp:
            self.y -= self.settings.playerSpeed
        if self.movementDown:
            self.y += self.settings.playerSpeed

        self.rect.x, self.rect.y = self.x, self.y

    def blit(self):
        if pygame.time.get_ticks() % 200 <= 50:
            self.screen.blit(self.image[0], self.rect)
        elif pygame.time.get_ticks() % 200 <= 100:
            self.screen.blit(self.image[1], self.rect)
        elif pygame.time.get_ticks() % 200 <= 150:
            self.screen.blit(self.image[2], self.rect)
        else:
            self.screen.blit(self.image[1], self.rect)

    def reset(self):
        self.x, self.y = 330, 445

