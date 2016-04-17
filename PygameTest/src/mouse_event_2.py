'''
Created on 2016/04/14

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
pygame.display.set_caption(u"マウスイベント2")

backImg = pygame.image.load("moriyama.jpg").convert()
pythonImg = pygame.image.load("python.png").convert_alpha()

cur_pos = (0,0)
pythons_pos = []

while True:
    screen.blit(backImg, (0,0))

    # マウスクリックで蛇をコピー
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:                        # 左クリック
        x,y = pygame.mouse.get_pos()
        x -= pythonImg.get_width() / 2
        y -= pythonImg.get_height() / 2
        pythons_pos.append((x,y))               # 蛇の位置を追加

    # マウス移動で蛇を移動
    x,y = pygame.mouse.get_pos()
    x -= pythonImg.get_width() / 2
    y -= pythonImg.get_height() / 2
    cur_pos = (x,y)

    # 蛇を表示
    screen.blit(pythonImg, cur_pos)
    for i,j in pythons_pos:
        screen.blit(pythonImg, (i,j))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
