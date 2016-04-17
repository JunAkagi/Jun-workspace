'''
Created on 2016/04/17

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


# 1フレームごとの移動ピクセル
vx = 10
vy = 2
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    img_rect.move_ip(vx,vy)
    """
    一般的には
    img_rect.left += vx
    img_rect.top += vy
    """


    if img_rect.left < 0 or img_rect.right > SCR_width:
        vx = -vx
    if img_rect.top < 0 or img_rect.bottom > SCR_height:
        vy = -vy

    screen.fill((0,0,255))
    screen.blit(img,img_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
