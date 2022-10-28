import pygame
import time
import random

class player():
    posX = None
    posY = 4
    weight = None
    health = None

    def __init__(self, posX, posY, weight, health):
        self.posX = posX
        self.posY = posY
        self.weight = weight
        self.health = health

    def jump(x):
        global posY
        copyosY = posY
        x = 0
        for i in range(0, 10):
            print(posY)
            posY = copyosY + -0.5* x ** 2 + 5 * x
            x = x + 1
            time.sleep(0.2)
        x = 0

#y\ =-.5x^{2}\ +\ 5x

player.jump(0)