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
    Description: 
    '''
    def __init__(self, color, tipe):
        '''
        Initializes the class
        '''
        self.color = color
        self.type = tipe
        self.image = pygame.image.load(os.path.join('assets', 'images','.'.join([f'{color}_{tipe}', 'png'])))
        self.image = pygame.transform.scale(self.image, (64,64))

        self.pos = (0,0)

    def render(self, surf, pos):
        '''
        Class method for rendering the shape class instance
        '''
        self.pos = pos
        surf.blit(self.image, self.pos)



        
