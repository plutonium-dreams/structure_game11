'''
Zendo Game for Math 153 Final Project

Controls:
WASD - up down left right
J - cycle through the colors
K - cycle through the shapes
SPACE - place piece
ENTER - verify structure

To do list:
[/] create a secret rule 
[/] generate grids that follow the secret rule  
[/] render the grids
[/] user grid creation
[/] player grid verification
[ ] game polishing
    - make the computer present one correct and one wrong structure
    - add more rules, possible variation
        - add orientation/pointing/grounded
    - add the ability to delete a placed piece
    - more polished assets
    - add a main menu system with easy and hard levels
'''

import pygame, random, sys
from grid import *
from rule import *
from shape import *



''' initialize '''
pygame.init()

scrx, scry = 640, 480
# scrx, scry = 1080, 720
center = (scrx/2,scry/2)


pygame.display.set_caption('Deduction (working title)')
window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()

''' game stuff '''
secret_rule = generateSecretRule()

player = PlayerGrid((center[0], scry - (scry/4)))

# defaults
inp = [0,0]
clr = 0
shp = 0


''' testing stuff '''

grid_1 = Grid((scrx/4, 125))
grid_2 = Grid((3 *scrx/4, 125))
grid_1.genGrid(secret_rule)
grid_2.genGrid(secret_rule)

print(f'Secret Rule: {secret_rule}')
print()
print(grid_1)
print()
print(grid_2)

while True:
    hand = Shape(attributes['color'][clr % 3], attributes['shape'][shp % 2])


    ''' rendering '''
    window.fill(('gray'))
    grid_1.render(window)
    grid_2.render(window)
    pygame.draw.circle(window, 'black', center, 5)

    player.render(window)
    hand.render(window, (scrx - 128, scry - 128))
    


    ''' logic '''    
    player.playerUpdate(window, inp)




    ''' event handling '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if inp[1] > 0:
                    inp[1] -= 1
            if event.key == pygame.K_s:
                if inp[1] < 2:
                    inp[1] += 1
            if event.key == pygame.K_d:
                if inp[0] < 2:
                    inp[0] += 1
            if event.key == pygame.K_a:
                if inp[0] > 0:
                    inp[0] -= 1
            
            # for placing a piece
            if event.key == pygame.K_SPACE:
                player.place(hand.color, hand.type)
                print(player)
            if event.key == pygame.K_j:
                clr += 1
            if event.key == pygame.K_k:
                shp += 1
            if event.key == pygame.K_RETURN:
                if player.checkGrid(secret_rule):
                    print(True)
                else:
                    print(False)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_d:
                pass
    

    ''' technical shi '''
    pygame.display.update()
    pygame.clock.tick(60)
    
