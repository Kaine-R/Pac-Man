import pygame
import random
import sys
from pygame.mixer import music

# CHECK EVENTS -------------------------------------------------------

def checkEvents(player, gameStats, play):
    y = [60, 145, 220, 295, 370, 445, 520, 600, 670, 750]
    for j in range(int(len(y))):
        pygame.draw.line(player.screen, (0, 0, 0), (0, y[j]), (700, y[j]))

    x = [35, 90, 155, 235, 305, 380, 455, 535, 605, 650]
    for i in range(int(len(x))):
        pygame.draw.line(player.screen, (0, 0, 0), (x[i], 0), (x[i], 1000))

    gameStats.pacPosX, gameStats.pacPosY = player.rect.x, player.rect.y
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            checkDown(event, player)
        elif event.type == pygame.KEYUP:
            checkUp(event, player)
        elif not gameStats.gameActive and event.type == pygame.MOUSEBUTTONDOWN:
            checkMouse(event, gameStats, play)
        elif event.type == pygame.QUIT:
            sys.exit()

def checkDown(event, player):
    if event.key == pygame.K_LEFT:
        player.movementLeft = True
    elif event.key == pygame.K_RIGHT:
        player.movementRight = True
    elif event.key == pygame.K_UP:
        player.movementUp = True
    elif event.key == pygame.K_DOWN:
        player.movementDown = True

def checkUp(event, player):
    if event.key == pygame.K_LEFT:
        player.movementLeft = False
    elif event.key == pygame.K_RIGHT:
        player.movementRight = False
    elif event.key == pygame.K_UP:
        player.movementUp = False
    elif event.key == pygame.K_DOWN:
        player.movementDown = False

def checkMouse(event, gameStats, play):
    mouseX, mouseY = pygame.mouse.get_pos()
    if play.rect.collidepoint(mouseX, mouseY):
        gameStats.gameActive = True
        gameStats.lives = 3
    elif play.HSrect.collidepoint(mouseX, mouseY):
        gameStats.showHS = True
        play.showBack = True
    elif play.backRect.collidepoint(mouseX, mouseY):
        play.showBack= False
        gameStats.showHS = False

# COLLIDE ------------------------------------------------------

def wallCollide(player, blocks):
    for block in blocks:
        if pygame.sprite.collide_rect(player, block):
            checkDirection(player, block)

def checkDirection(player, block):
    left = False
    right = False
    up = False
    down = False
    if player.rect.centerx <= block.rect.x:
        right = True
    else:
        left = True
    if player.rect.y + player.rect.height/2 <= block.rect.y + block.rect.height/2:
        up = True
    else:
        down = True

    if left and (not up or not down):
        player.x += 1
    elif right and (not up or not down):
        player.x -= 1
    if up:
        player.y -= 1
    elif down:
        player.y += 1

def dotCollide(player, dots, gameStats):
    if pygame.sprite.spritecollide(player, dots, True):
        gameStats.score += 5

def fruitCollide(player, fruit, gameStats):
    if pygame.sprite.collide_rect(player, fruit):
        gameStats.score += 50
        pygame.mixer.music.load('sound/pacSound.mp3')
        pygame.mixer.music.play(0)
        gameStats.fruitPresent = False

def pillCollide(player, powerPills, gameStats):
    if pygame.sprite.spritecollide(player, powerPills, True):
        gameStats.power = True
        gameStats.powerTimer = pygame.time.get_ticks()

    if gameStats.power and pygame.time.get_ticks() - gameStats.powerTimer > 7500:
        gameStats.power = False

def playerGhostCollide(player, ghosts, gameStats, mainMenu):
    if pygame.sprite.collide_rect(player, ghosts):
        pygame.time.wait(200)
        gameStats.lives -= 1
        player.reset()
        ghosts.reset()
        ghosts.instructions = 0

    if gameStats.lives < 0:
        pygame.mixer.music.load('sound/deathSound.mp3')
        pygame.mixer.music.play(0)
        mainMenu.changeScores(gameStats.score)
        gameStats.gameActive = False


def ghostCollide(ghost, blocks):
    checkPoint = (-10, -10)
    ghost.timer += 1

    if ghost.checkX() and ghost.checkY() and ghost.timer > 50:
        ghost.timer = 0
        for i in range(4):
            ghost.openWays[i] = True
        for block in blocks:
            checkPoint = (ghost.x, ghost.y -15)
            if block.rect.collidepoint(checkPoint):
                ghost.openWays[0] = False
            checkPoint = (ghost.x + ghost.rect.width/2 + 15, ghost.y + ghost.rect.height/2)
            if block.rect.collidepoint(checkPoint):
                ghost.openWays[1] = False
            checkPoint = (ghost.x, ghost.y + ghost.rect.height + 15)
            if block.rect.collidepoint(checkPoint):
                ghost.openWays[2] = False
            checkPoint = (ghost.x - ghost.rect.width/2 - 20, ghost.y + ghost.rect.height/2)
            if block.rect.collidepoint(checkPoint):
                ghost.openWays[3] = False

        print(ghost.openWays, end = "")
        setDirection(ghost)
        print(" : " + str(ghost.lastAxis) )


def setDirection(ghost):

    if ghost.lastAxis == 0:
        if ghost.pacX < ghost.x and ghost.openWays[3]:
            setmove(ghost, 3)
            ghost.lastAxis = 1
        elif ghost.openWays[1]:
            setmove(ghost, 1)
            ghost.lastAxis = 1
        else:
            if ghost.pacY <= ghost.y and ghost.openWays[0]:
                setmove(ghost, 0)
                ghost.lastAxis = 0
            elif ghost.pacY > ghost.y and ghost.openWays[2]:
                setmove(ghost, 2)
                ghost.lastAxis = 0
    else:
        if ghost.pacY < ghost.y and ghost.openWays[0]:
            setmove(ghost, 0)
            ghost.lastAxis = 0
        elif ghost.openWays[2]:
            setmove(ghost, 2)
            ghost.lastAxis = 0
        else:
            if ghost.pacX <= ghost.x and ghost.openWays[3]:
                setmove(ghost, 3)
                ghost.lastAxis = 1
            elif ghost.pacX > ghost.x and ghost.openWays[1]:
                setmove(ghost, 1)
                ghost.lastAxis = 1

def setmove(ghost, num):
        ghost.moveDirection = num


def checkScreenLimits(object):
    if object.x < -3:
        object.x = object.settings.screenWidth +3
    if object.x > object.settings.screenWidth +3:
        object.x = 0

def addDiff(ghost, gameStats):
    ghost.diff = gameStats.score/3000


# Spawn ---------------------------------------------------------------

def spawnFruit(gameStats, fruit):
    if gameStats.fruitPresent == False and pygame.time.get_ticks() - gameStats.fruitTimer > 10000:
        fruit.type = random.randint(0, 2)
        gameStats.fruitPresent = True
        gameStats.fruitTimer = pygame.time.get_ticks()

def roundEnd(gameStats, player, ghosts, dots, powerPills, map):
    if len(dots) <= 0:
        if pause(gameStats, 2300):
            player.reset()
            map.reset(dots, powerPills)
            for ghost in ghosts:
                ghost.addDiff()
                ghost.reset()
            gameStats.pause = False
            gameStats.nextRound = False
            gameStats.round += 1
        else:
            gameStats.nextRound = True

def pause(gameStats, time):
    if pygame.time.get_ticks() - gameStats.pauseTimer > time and gameStats.pause == True:
        return True
    elif gameStats.pause == False:
        gameStats.pauseTimer = pygame.time.get_ticks()
        gameStats.pause = True
        return False
