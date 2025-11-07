'''
grid - cell testing

# parameters
cell = an integer from 0 to 8 designating a position on the 3x3 grid
item = [shape, color, orientation]

# to do
- Grid /
- Shapes /
- Transition to Pygame / 

'''
import sys
import pygame
from shapes import *

pygame.init()

class Grid():
    def __init__(self, pos):
        self.size = (150,150)       # default (150, 150)
        self.n = 3
        self.grid = [[], [], [],
                     [], [], [],
                     [], [], []]
        self.pos = (pos[0] - self.size[0] / 2, pos[1] - self.size[1] / 2)
        self.center = pos

    def update(self, cell, item):    
        if self.grid[cell] == []:
            self.grid[cell] = item
        else:
            print('\nAn item already exists in the cell!\n')

    def swap(self, cell_1, cell_2):
        self.grid[cell_1], self.grid[cell_2] = self.grid[cell_2], self.grid[cell_1]

    def render(self, surf):
        k = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[k] != []:
                    # can be simplified into pygame.surf.blits if we have images of the rectangle and triangle instead
                    
                    if self.grid[k][0] == 'rectangle':
                        pygame.draw.rect(surf, self.grid[k][1], ((self.pos[0] + (j * 50), self.pos[1] + (i * 50)), (self.size[0] / self.n, self.size[1] / self.n)))
                        
                    elif self.grid[k][0] == 'triangle':
                        pygame.draw.polygon(surf, self.grid[k][1], tri_orient(self.grid[k][2], (self.center[0] + ((j-1) * 50), self.center[1] + ((i-1) * 50)), (self.size[0]/3,self.size[1]/3)))
                
                k += 1








