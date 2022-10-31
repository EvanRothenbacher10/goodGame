import random
import threading
import time

import pygame as pg

from playerClass import *

#Variables

pg.init()

bgColor = (0, 0, 0)
screen = pg.display.set_mode((640, 360))
screen.fill(bgColor)
pg.display.set_caption("Good Game (pygame)")
running = True
origin = (0, 0)
player = playerClass("player1", 0, 0, 100)


#Functions

def keyCheck():
    print("keyCheck thread running")
    while True:
        keys=pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            player.jump()
            time.sleep(6)
                
keysThread = threading.Thread(target= keyCheck)

keysThread.start()

while True:
    screen.fill(bgColor)
    screen.blit()

    pg.display.flip() #Updates screen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
