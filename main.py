import pygame as pg
import random as rdm
import time as tm
from sprite import *
from settings import *

class Puzzle:
    def __init__(self):
        pg.init()
        self.screen =pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE) 
        self.clock = pg.time.Clock()

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
    
    def create_random_numbers(self):
        randomlist=[]
        randomlist = rdm.sample(range(1,(GAME_SIZE*GAME_SIZE)), (GAME_SIZE*GAME_SIZE)-1)
        return randomlist
  
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.win_game_order()
        self.draw_tiles()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            if(self.tiles_grid==self.tiles_grid_completed):
                print("Win")
                self.playing=False
      

    def update(self):
       self.all_sprites.update()
       
    def draw_grid(self):
        for row in range(-1, GAME_SIZE*TILESIZE,TILESIZE):
            pg.draw.line(self.screen, GRID,(row,0),(row,GAME_SIZE*TILESIZE))

        for col in range(-1, GAME_SIZE*TILESIZE,TILESIZE):
              pg.draw.line(self.screen, GRID,(0,col),(GAME_SIZE*TILESIZE,col))

    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile !=0:
                    self.tiles[row].append(Tile(self,col,row,str(tile)))
                else:
                    self.tiles[row].append(Tile(self,col,row,"empty"))
 
    def draw(self):
        self.screen.fill(BG)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
       
        pg.display.flip()

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
   
