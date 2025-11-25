'''
Zendo-inspired game for Math 153 final project

dev notes here for

'''
import sys, pygame

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

# testing setup
colors = ["red", "yellow", "blue"]
orientations = ["up","down","left","right"] * 3
SECRET_RULE = generateSecretRule()


player_grid = Grid((scrx/2,scry - 130))
# comp_grid1 = Grid((scrx/3,125), 'white')
# comp_grid2 = Grid((2 * scrx/3,125), 'black')

comp_grid1 = generateGrid(SECRET_RULE, (scrx/3,125), 'white')
comp_grid2 = generateGrid(SECRET_RULE, (2 * scrx/3,125), 'black')
print(SECRET_RULE)

# structures are grids with the black/white/no circle
structures = dict()

for i in (
    {player_grid: 'blank'}, 
    {comp_grid1: 'blank'}, 
    {comp_grid2: 'blank'}, 
):
    structures.update(i)



for i in range(len(colors)):
    player_grid.update(i, Rectangle(colors[i]).rectItem())
# player_grid.update(4, Triangle('green', 'down').triItem())
# player_grid.update(6, Triangle('sky blue', 'left').triItem())

# for i in range(len(colors)):
#     comp_grid1.update(i, Triangle(colors[i], orientations[i]).triItem())

# for i in range(len(colors)):
#     comp_grid2.update(i, Rectangle(colors[-i]).rectItem())







''' game loop '''
def game():
    while True:
        ''' updating '''
        
        ''' rendering '''
        pygame.nres.fill(("dark gray"))
        
        for struc in structures:
            struc.render(pygame.nres)

        ''' event handling '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gri.render()
                if event.key == pygame.K_t:
                    pass


        ''' technical shi '''
        pygame.window.blit(pygame.transform.scale(pygame.nres, pygame.window.get_size()), (0,0))    # blits nres to window
        pygame.display.update()
        pygame.clock.tick(60)

game()