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
pygame.display.set_caption("Hello, world!")

# フォントの作成
sysfont = pygame.font.SysFont(None, 80)
# テキストを描画したSurfaceを作成
hello1 = sysfont.render("Hello, world!",False,(0,0,0))
hello2 = sysfont.render("Hello, world!",True,(0,0,0))
hello3 = sysfont.render("Hello, world!",True,(255,0,0),(255,255,0))


# ゲームグループ
while True:
    screen.fill((0,0,255))  # 画面を青色で塗り潰す
    
    # テキストを描画
    screen.blit(hello1,(20,50))
    screen.blit(hello2,(20,150))
    screen.blit(hello3,(20,250))
    
    pygame.display.update() # 画面を更新
    # 終了イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 終了イベント
            sys.exit()