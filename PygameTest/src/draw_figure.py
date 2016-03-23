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
pygame.display.set_caption(u"図形の描画")

while True:
    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,255,0),Rect(10,10,300,200),0) #(描画したいSuraface,色,Rect(左上の座標,大きさ),線の太さ)
    pygame.draw.circle(screen,(255,0,0),(320,240),100)
    pygame.draw.ellipse(screen,(255,0,255),(400,300,200,100))
    pygame.draw.line(screen,(255,255,255),(0,0),(640,480))
#    pygame.draw.screen.fill((0,255,0),Rect(200,200,500,400))  高速描画が可能（構文要研究）

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()