from lib2to3.pgen2 import pgen
from tkinter import font
import pygame as pg
from settings import *

pg.font.init()

#Se encarga de crear las casillas
class Tile(pg.sprite.Sprite):
    def __init__(self, puzzle,x,y,text) :
       self.groups = puzzle.all_sprites
       pg.sprite.Sprite.__init__(self,self.groups)
       self.puzzle=puzzle
       self.image = pg.Surface((TILESIZE,TILESIZE))     
       self.x ,self.y = x,y
       self.text = text
       self.rect = self.image.get_rect()
       
       if self.text != "empty":
            self.font = pg.font.SysFont("Consolas",50)
            font_surface = self.font.render(self.text, True,NUMBER)
            self.image.fill(TILE)
            self.font_size = self.font.size(self.text)
            draw_x=(TILESIZE/2)-self.font_size[0]/2
            draw_y=(TILESIZE/2)-self.font_size[1]/2
            self.image.blit(font_surface,(draw_x,draw_y))
       else:
            self.image.fill(GRID)

#Realiza los diferentes movimientos
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    def right(self):
        return self.rect.x +TILESIZE < GAME_SIZE*TILESIZE
    
    def left(self):
        return self.rect.x - TILESIZE>= 0
    
    def up(self):
        return self.rect.y - TILESIZE>= 0
    
    def down(self):
        return self.rect.y + TILESIZE < GAME_SIZE*TILESIZE
     
            
       
       
       
   


        
  
       
       
     
        
