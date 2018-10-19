import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from mainMenu import Menu
from playButton import Play
from details import Details
from player import Player
from ghost import Ghost
from fruits import Fruit
from gameStats import GameStats
from buildMap import BuildMap
from pygame.mixer import music
import gameFunctions as gf
 
def runGame():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("PacMan")
    mainMenu = Menu(screen, settings)
    play = Play(screen, settings)
    gameStats = GameStats()
    map = BuildMap(screen, settings)
    details = Details(screen, settings)
    blocks = Group()
    dots = Group()
    ghosts = []
    for i in range(4):
        new = Ghost(screen, settings)
        new.type = i
        new.x += 30*i
        new.prep()
        ghosts.append(new)
    fruit = Fruit(screen, settings)
    powerPills = Group()
    player = Player(screen, settings)
    map.makeMap(blocks, dots, powerPills)
    pygame.mixer.init()

    while True:
        screen.fill((50, 20, 20))
        map.drawMap(blocks, dots, powerPills)

        details.blit()
        gf.checkEvents(player, gameStats, play)
        if gameStats.gameActive:
            if gameStats.pause == False:
                if player.movementRight or player.movementLeft or player.movementUp or player.movementDown:
                    pygame.mixer.music.load('sound/dotSound.mp3')
                    pygame.mixer.music.play(0, .052)
                player.update()
                player.blit()
                for i in range(4):
                    ghosts[i].update(gameStats)
                    ghosts[i].blit()
                    gf.checkScreenLimits(ghosts[i])
                gf.checkScreenLimits(player)
            details.prep(gameStats)
            fruit.blit(gameStats)
            gf.spawnFruit(gameStats, fruit)
            gf.ghostCollide(ghosts[0], blocks)
            gf.ghostCollide(ghosts[2], blocks)
            gf.fruitCollide(player, fruit, gameStats)
            gf.addDiff(ghosts[2], gameStats)
            gf.wallCollide(player, blocks)
            gf.dotCollide(player, dots, gameStats)
            gf.pillCollide(player, powerPills, gameStats)
            for ghost in ghosts:
                gf.playerGhostCollide(player, ghost, gameStats, mainMenu)
            gf.roundEnd(gameStats, player, ghosts, dots, powerPills, map)
        else:
            mainMenu.checkShowHS(gameStats.showHS)
            mainMenu.update()
            mainMenu.blit()
            play.blit()

        pygame.display.flip()

runGame()