import pygame
import time
import random

class playerClass():

    def __init__(self, name, posX, posY, health):
        self.name = name
        self.posX = 0
        self.posY = 0
        self.health = health

    def jump(self):
        x = 0
        copyosY = self.posY
        for i in range(0, 12):
            print(self.posY)
            self.posY = copyosY + -0.5* x ** 2 + 5 * x
            x = x + 1
            time.sleep(0.2)
        x = 0

#y\ =-.5x^{2}\ +\ 5x

player = playerClass("player1", 0, 0, 100)
player.jump()