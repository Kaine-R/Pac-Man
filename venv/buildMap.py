import pygame
from blocks import Blocks
from dot import Dot
from powerPill import PowerPill

class BuildMap():
    def __init__(self, screen, settings):
        self.screen, self.settings = screen, settings
        self.file = open("map.txt", "r")
        self.textNewLine = "/n"
        self.line = ""
        self.lines = []
        self.xShift = 0
        self.yShift = 35
        
        if self.file.mode == "r":
            self.contents = self.file.read()
            print("Start of read")

        for chars in self.contents:
            if chars != "\n":
                self.line += chars
            else:
                self.lines.append(self.line)
                self.line = ""

    def makeMap(self, blocks, dots, powerPills):
        size = self.settings.rectSize
        for row in self.lines:
            for chars in row:
                if chars == "X":
                    newBlock = Blocks(self.screen)
                    newBlock.rect.x, newBlock.rect.y = self.xShift, self.yShift
                    self.xShift += size
                    blocks.add(newBlock)
                elif chars == ".":
                    newDot = Dot(self.screen, self.settings)
                    newDot.rect.x, newDot.rect.y = self.xShift +size/4, self.yShift +size/4
                    self.xShift += size
                    dots.add(newDot)
                elif chars ==" ":
                    self.xShift += size
                elif chars == "o":
                    newPill = PowerPill(self.screen, self.settings)
                    newPill.rect.x, newPill.rect.y = self.xShift +size/4, self.yShift +size/4
                    powerPills.add(newPill)
                    self.xShift += size
                elif chars == "x":
                    newBlock = Blocks(self.screen)
                    newBlock.rect.x, newBlock.rect.y = self.xShift, self.yShift
                    newBlock.type = 1
                    self.xShift += size
                    blocks.add(newBlock)
            self.xShift = 0
            self.yShift += size

    def drawMap(self, blocks, dots, powerPills):
        for block in blocks:
            block.draw()
        for dot in dots:
            dot.blit()
        for pill in powerPills:
            pill.blit()

    def reset(self, dots, powerPills):
        size = self.settings.rectSize
        self.xShift = 0
        self.yShift = 35
        for row in self.lines:
            for chars in row:
                if chars == "X" or chars == "x":
                    self.xShift += size
                if chars == ".":
                    newDot = Dot(self.screen, self.settings)
                    newDot.rect.x, newDot.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    self.xShift += size
                    dots.add(newDot)
                elif chars == " ":
                    self.xShift += size
                elif chars == "o":
                    newPill = PowerPill(self.screen, self.settings)
                    newPill.rect.x, newPill.rect.y = self.xShift + size / 4, self.yShift + size / 4
                    powerPills.add(newPill)
                    self.xShift += size

            self.xShift = 0
            self.yShift += size