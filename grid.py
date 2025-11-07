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
import pygame
from shapes import *
from secret_rules import *

pygame.init()

class Grid():
    def __init__(self, pos, token=None):
        self.size = (150,150)       # default (150, 150)
        self.grid = [[], [], [],
                     [], [], [],
                     [], [], []]
        self.pos = (pos[0] - self.size[0] / 2, pos[1] - self.size[1] / 2)
        self.center = pos
        self.token = token

    def __str__(self):
        # print(self.grid)
        for i in range(len(self.grid)):
            print(self.grid[i], end='')
            if (i+1) % 3 == 0:
                print('')

            
        return ''


    def update(self, cell, item):    
        if self.grid[cell] == []:
            self.grid[cell] = item
        else:
            print('\nAn item already exists in the cell!\n')

    def swap(self, cell_1, cell_2):
        self.grid[cell_1], self.grid[cell_2] = self.grid[cell_2], self.grid[cell_1]

    def render(self, surf):
        k = 0
        for i in range(3):
            for j in range(3):
                if self.grid[k] != []:
                    # can be simplified into pygame.surf.blits if we have images of the rectangle and triangle instead
                    
                    if self.grid[k][0] == 'rectangle':
                        pygame.draw.rect(surf, self.grid[k][1], ((self.pos[0] + (j * 50), self.pos[1] + (i * 50)), (self.size[0] / 3, self.size[1] / 3)))
                        
                    elif self.grid[k][0] == 'triangle':
                        pygame.draw.polygon(surf, self.grid[k][1], tri_orient(self.grid[k][2], (self.center[0] + ((j-1) * 50), self.center[1] + ((i-1) * 50)), (self.size[0]/3,self.size[1]/3)))
                
                k += 1
    
        if self.token:
            pygame.draw.circle(surf, self.token, (self.center[0], self.center[1] + 2 * self.size[1]/3), (self.size[0]/6))
    




def genUpdate(grd, item):
    cell = random.randint(0,8)
    if grd.grid[cell] == []:
        grd.grid[cell] = item
    else:
        return genUpdate(grd, item)

def generateGrid(surf, pos, token=None):
    grid = Grid(pos, token)

    # generate shapes        
    shapes = []

    for typ in range(random.randint(1,3)):
        for qty in range(random.randint(1,3)):
            shp = random.randint(1,2) 
            if shp == 2:
                shapes.append(Triangle(attributes['color'][random.randint(0,2)], attributes['orientation'][random.randint(0,3)]).triItem())
            elif shp == 1:
                shapes.append(Rectangle(attributes['color'][random.randint(0,2)]).rectItem())

    # place the shapes on the grid
    for shape in shapes:
        genUpdate(grid, shape)
        
    return grid
        
