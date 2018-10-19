class GameStats():
    def __init__(self):
        self.score = 0
        self.lives = 3

        self.power = False
        self.powerTimer = 0
        self.fruitPresent = False
        self.fruitTimer = 0

        self.gameActive = False
        self.showHS = False
        self.pause = False
        self.pauseTimer = 0
        self.round = 2
        self.nextRound = False

        self.pacPosX, self.pacPosY = 50, 50