'''
Zendo-inspired game for Math 153 final project

dev notes here for

'''


import sys
import pygame

from shapes import *
from grid import *

''' initialize '''
scrx, scry = 640, 480
#scrx, scry = 1080, 720

pygame.init()
pygame.display.set_caption("Zendo Prototype in Pygame")
pygame.window = pygame.display.set_mode((scrx, scry))
#pygame.nres = pygame.Surface(((1)* scrx * (3 / 4), (1)*scry * (3/4)))
pygame.nres = pygame.Surface((scrx, scry))
pygame.clock = pygame.time.Clock()

''' vars / funcs '''
structures = {'a'}
print(structures)

# testing setup
colors = ["red", "yellow", "blue", "green", "orange", "purple", "brown", "pink", "sky blue"]
orientations = ["up","down","left","right"] * 3

player_grid = Grid((scrx/2,scry - 150))
comp_grid1 = Grid((scrx/3,125))
comp_grid2 = Grid((2 * scrx/3,125))

for i in range(len(colors)):
    player_grid.update(i, Rectangle(colors[i]).rectItem())
# player_grid.update(4, Triangle('green', 'down').triItem())
# player_grid.update(6, Triangle('sky blue', 'left').triItem())

for i in range(len(colors)):
    comp_grid1.update(i, Triangle(colors[i], orientations[i]).triItem())

for i in range(len(colors)):
    comp_grid2.update(i, Rectangle(colors[-i]).rectItem())


''' game loop '''
def game():
    while True:
        pygame.nres.fill(("dark gray"))

        # playing around
        for cell in range(9):
            try:
                player_grid.swap(cell, cell + 1)
                comp_grid1.swap(cell, cell + 1)
                comp_grid2.swap(cell, cell+1)
            except IndexError:
                pass
            
            
        player_grid.render(pygame.nres)
        comp_grid1.render(pygame.nres)
        comp_grid2.render(pygame.nres)



        for i in range(3):
            for j in range(3):
                pygame.draw.circle(pygame.nres, 'white', ((scrx/2)+ ((i-1) * 50), (scry - 150)+ ((j-1) * 50)), 5) 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gri.render()
                if event.key == pygame.K_t:
                    pass

        pygame.window.blit(pygame.transform.scale(pygame.nres, pygame.window.get_size()), (0,0))
        pygame.display.update()
        pygame.clock.tick(1)

game()