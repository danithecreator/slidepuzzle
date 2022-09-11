# Diferentes librerias y utilidades usadas en el proyecto
import pygame as pg
import random as rdm
import time as tm
from sprite import *
from settings import *


# Clase principal del programa, es la encargada de dibujar la pantalla, el tablero y las fichas
# asi como de iniciar el hilo de juego
class Puzzle:
    # Inicia la pantalla
    def __init__(self):
        pg.init()
        self.size=GAME_SIZE*TILESIZE
        self.screen =pg.display.set_mode(( self.size, self.size))
        pg.display.set_caption(TITLE) 
        self.clock = pg.time.Clock()

    # Crea el tablero con los numeros aleatorios
    def create_game(self):
        grid = []
        initialNumbers=self.create_random_numbers()

        z=0
        for x in range(GAME_SIZE):
            grid.append([])
            for y in range(GAME_SIZE):
                grid[x].append(initialNumbers[z])
                z+=1
       
        
        return grid
    # Crea una matriz ordenada para determinar cuando se gana el juego
    def win_game_order(self):
        grid = []
        number = 1
        for x in range(GAME_SIZE):
            grid.append([])
            for y in range(GAME_SIZE):
                grid[x].append(number)
                number+=1
        grid[-1][-1]=0
       
        return grid
    
    # Crea una lista de numeros aleatorios desde 0
    def create_random_numbers(self):
        randomlist=[]
        randomlist = rdm.sample(range(0,(GAME_SIZE*GAME_SIZE)), (GAME_SIZE*GAME_SIZE))
     
        return randomlist
  
    # Se encarga de inicializar la partida y dibujar el primer tablero
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.win_game_order()
        self.draw_tiles()

    # Corre el hilo del juego, cuando el jugador organiza todas las fichas finaliza la partida
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            if(self.tiles_grid==self.tiles_grid_completed):
                self.playing=False
      
    # Actualiza el tablero de juego
    def update(self):
       self.all_sprites.update()
    
    # Dibuja el grid
    def draw_grid(self):
        for row in range(-1, GAME_SIZE*TILESIZE,TILESIZE):
            pg.draw.line(self.screen, WHITE,(row,0),(row,GAME_SIZE*TILESIZE))

        for col in range(-1, GAME_SIZE*TILESIZE,TILESIZE):
              pg.draw.line(self.screen, WHITE,(0,col),(GAME_SIZE*TILESIZE,col))

    # Dibuja los numeros y celdas
    def draw_tiles(self):
        
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            print(row)
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile !=0:
                    self.tiles[row].append(Tile(self,col,row,str(tile)))
                else:
                    self.tiles[row].append(Tile(self,col,row,"empty"))
 
    # Dibuja la pantalla incial
    def draw(self):
        self.screen.fill(BG)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
       
        pg.display.flip()
        
    # Dibuja el mensaje de ganaste en la pantalla
    def draw_winnig_screen(self):
        pg.display.set_caption(TITLE)     
        font = pg.font.Font('freesansbold.ttf', 50)  
        text = font.render('¡¡GANASTE¡¡', True, WHITE)
        textRect = text.get_rect()
        textRect.center = ( self.size / 2,  self.size / 2)
        self.screen.fill(BG)
        self.screen.blit(text, textRect)
        pg.display.flip()
        
    # Captura los eventos
    def events(self):
        for event in pg.event.get():
            # Captura el evento de cerrar la ventana
            if event.type == pg.QUIT:
                pg.quit()
                quit(0)
            
            # Captura el evento de dar click sobre una ficha
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                
                # Valida si la ficha se puede mover en la direccion donde esta el espacio en blanco, si se puede traslada la ficha
                # a ese espacio
                for row, tiles in enumerate(self.tiles):
                    for col,tile in enumerate(tiles):
                        if tile.click(mouse_x,mouse_y):
                            if tile.right() and self.tiles_grid[row][col+1]==0:
                                self.tiles_grid[row][col],self.tiles_grid[row][col+1] = self.tiles_grid[row][col+1] ,self.tiles_grid[row][col]
                            
                            if tile.left() and self.tiles_grid[row][col-1] ==0:
                                 self.tiles_grid[row][col],self.tiles_grid[row][col-1] = self.tiles_grid[row][col-1] ,self.tiles_grid[row][col]
                            
                            if tile.up() and self.tiles_grid[row-1][col] ==0:
                                 self.tiles_grid[row][col],self.tiles_grid[row-1][col] = self.tiles_grid[row-1][col] ,self.tiles_grid[row][col]
                            
                            if tile.down() and self.tiles_grid[row+1][col] ==0:
                                 self.tiles_grid[row][col],self.tiles_grid[row+1][col] = self.tiles_grid[row+1][col] ,self.tiles_grid[row][col]
                                 
                            self.draw_tiles()

# Instancia de la clase principal
puzzle = Puzzle()

# Inicio del ciclo del juego
while True:
    puzzle.new()
    puzzle.run()
    puzzle.draw_winnig_screen()
    tm.sleep(2)
   
