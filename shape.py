'''
Shapes module

Overview

Dependencies


'''

import pygame, os, random

pygame.init()

class Shape():
    '''
    Shape class
    Description: Holds functions responsible grabbing specific shapes, color and type, from the game assets
    and rendering them on the grids. 
    '''

    # function for loading specific shape images from the game assets and scaling them
    def __init__(self, color, tipe):
        '''
        Initializes the class
        '''
        self.color = color
        self.type = tipe
        self.image = pygame.image.load(os.path.join('assets', 'images','.'.join([f'{color}_{tipe}', 'png'])))
        self.image = pygame.transform.scale(self.image, (64,64))

        self.pos = (0,0)

    # function rendering a shape, based on the class, on a set position on a surface
    def render(self, surf, pos):
        '''
        Class method for rendering the shape class instance
        '''
        self.pos = pos
        surf.blit(self.image, self.pos)



        
