'''
Shapes module

'''

import pygame, os

pygame.init()

class Shape():
    def __init__(self, color, tipe):
        self.color = color
        self.type = tipe
        self.image = pygame.image.load(os.path.join('assets', 'images', '.'.join([f'{color}_{tipe}', 'png'])))

        self.pos = (0,0)

    def render(self, surf, pos):
        self.pos = pos
        surf.blit(self.image, self.pos)



        
