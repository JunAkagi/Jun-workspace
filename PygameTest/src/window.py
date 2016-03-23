'''
Created on 2016/03/21

@author: JUN_AKAGI
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

screen_size=(640,480)   # 画面サイズ

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("")


while True:
    screen.fill((0,0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()