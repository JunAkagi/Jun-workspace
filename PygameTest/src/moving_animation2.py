'''
Created on 2016/04/18

@author: JUN_AKAGI
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCR_width = 640
SCR_height = 480

pygame.init()
screen = pygame.display.set_mode((SCR_width,SCR_height))
pygame.display.set_caption(u"画像の移動と跳ね返り処理")

img = pygame.image.load("python.png").convert_alpha()
img_rect = img.get_rect()
print(img_rect)  # テスト用


# 1秒間の移動ピクセル
vx = 120
vy = 120
clock = pygame.time.Clock()

while True:
    time_passed = clock.tick(60)                # 60fpsで前回からの経過時間を返す（ミリ秒）
    time_passed_sec = time_passed / 1000.0      # ミリ秒を秒に変換

    vxf = vx * time_passed_sec
    vyf = vy * time_passed_sec
    
    img_rect.x += vx * time_passed_sec
    img_rect.y += vy * time_passed_sec

    if img_rect.left < 0 or img_rect.right > SCR_width:
        vx = -vx
        print(vxf,vyf)
    if img_rect.top < 0 or img_rect.bottom > SCR_height:
        vy = -vy
        print(vxf,vyf)

    screen.fill((0,0,255))
    screen.blit(img,img_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
