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
pygame.display.set_caption(u"イメージロード関数のテスト") #キャプション

"""

"""

def load_image(filename, colorkey = None):
#    try:                                                        # 画像ファイルの読み込み
    image = pygame.image.load(filename)
#    except pygame.error, message:                               # 失敗した時はメッセージを出して終了
#        print "Cannot load image:", filename
#        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

planeImg, planeRect = load_image("plane.png", colorkey = -1)

while True:
    screen.fill((0,0,0))
    screen.blit(planeImg,(100,100))
#    screen.blit(planeImg2,(200,100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()