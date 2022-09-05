import pygame as pg
import random as rdm
import time as tm
from sprite import *
from settings import *
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
class Puzzle:
    #Inicia la pantalla
    def __init__(self):
        pg.init()
        self.screen =pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE) 
        self.clock = pg.time.Clock()

    #Crea el grid con los numeros aleatorios
    def create_game(self):
        grid = []
        initialNumbers=self.create_random_numbers()
        initialNumbers.append(0)
        z=0
        for x in range(GAME_SIZE):
            grid.append([])
            for y in range(GAME_SIZE):
                grid[x].append(initialNumbers[z])
                z+=1
       
        print(grid)
        return grid
    #Crea una matriz ordenada para determinar si gana
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
    
    #Crea numeros aleatorios
    def create_random_numbers(self):
        randomlist=[]
        randomlist = rdm.sample(range(1,(GAME_SIZE*GAME_SIZE)), (GAME_SIZE*GAME_SIZE)-1)
        return randomlist
  
    #Se encarga de inicializar la partida y dibujar el primer grid
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.win_game_order()
        self.draw_tiles()

    #corre el hilo del juego
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            if(self.tiles_grid==self.tiles_grid_completed):
                self.playing=False
      
    #Actualiza el grid
    def update(self):
       self.all_sprites.update()
    
    #dibuja el grid
    def draw_grid(self):
        for row in range(-1, GAME_SIZE*TILESIZE,TILESIZE):
            pg.draw.line(self.screen, GRID,(row,0),(row,GAME_SIZE*TILESIZE))

        for col in range(-1, GAME_SIZE*TILESIZE,TILESIZE):
              pg.draw.line(self.screen, GRID,(0,col),(GAME_SIZE*TILESIZE,col))

    #dibuja los numeros y celdas
    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile !=0:
                    self.tiles[row].append(Tile(self,col,row,str(tile)))
                else:
                    self.tiles[row].append(Tile(self,col,row,"empty"))
 
    #dibuja la pantalla incial
    def draw(self):
        self.screen.fill(BG)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
       
        pg.display.flip()

    def draw2(self):
        pg.display.set_caption(TITLE)     
        font = pg.font.Font('freesansbold.ttf', 50)
 
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('¡¡GANASTE¡¡', True, white)
 
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        textRect.center = (WIDTH / 2, HEIGHT / 2)
        self.screen.fill(BG)
        self.screen.blit(text, textRect)
        pg.display.flip()
        
    #captura el vevento
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit(0)
                
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                
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

puzzle = Puzzle()
# print(puzzle.create_random_numbers())

while True:
    puzzle.new()
    puzzle.run()
    puzzle.draw2()
    tm.sleep(2)
   
