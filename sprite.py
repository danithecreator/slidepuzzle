
import pygame as pg
from settings import *

pg.font.init()

#Se encarga de crear las casillas
class Tile(pg.sprite.Sprite):
    def __init__(self, puzzle,x,y,text) :
        # Constructor de la clase, se inicializan las variables, de color, posicion tamaño y texto
       self.groups = puzzle.all_sprites
       pg.sprite.Sprite.__init__(self,self.groups)
       self.puzzle=puzzle
       self.image = pg.Surface((TILESIZE,TILESIZE))     
       self.x ,self.y = x,y
       self.text = text
       self.rect = self.image.get_rect()
       
       # Si dentro del paramentro text se pasa el texto "empty" se dibuja un espacio vacio de lo contrario el numero 
       if self.text != "empty":
            self.font = pg.font.SysFont("Consolas",50)
            font_surface = self.font.render(self.text, True,NUMBER)
            self.image.fill(TILE)
            self.font_size = self.font.size(self.text)
            draw_x=(TILESIZE/2)-self.font_size[0]/2
            draw_y=(TILESIZE/2)-self.font_size[1]/2
            self.image.blit(font_surface,(draw_x,draw_y))
       else:
            self.image.fill(WHITE)

#Realiza los diferentes movimientos
    # Actualiza la posicion de la casilla
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    #  Valida si la ficha esta dentro de los limites del tablero
    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    # Valida si la ficha se puede mover hacia la derecha sin salirse del tablero
    def right(self):
        return self.rect.x +TILESIZE < GAME_SIZE*TILESIZE
    # Valida si la ficha se puede mover hacia la izquierda sin salirse del tablero
    def left(self):
        return self.rect.x - TILESIZE>= 0
    # Valida si la ficha se puede mover hacia arriba sin salirse del tablero
    def up(self):
        return self.rect.y - TILESIZE>= 0
    # Valida si la ficha se puede mover hacia abajo sin salirse del tablero
    def down(self):
        return self.rect.y + TILESIZE < GAME_SIZE*TILESIZE
     
            
       
       
       
   


        
  
       
       
     
        
