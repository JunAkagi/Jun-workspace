'''
Created on 2016/03/22

@author: JUN
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

screen_size=(640,480)   # 画面サイズ

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(u"イメージ描画") #キャプション

# イメージを用意
backImg = pygame.image.load("moriyama.jpg").convert()   # 背景
pythonImg = pygame.image.load("python.png").convert_alpha()

while True:
    screen.blit(backImg,(0,0))         # 背景を描画
    screen.blit(pythonImg,(320,400))    # 蛇を描画
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()