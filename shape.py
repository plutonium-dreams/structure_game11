'''
Shapes module

Overview: This module intends to host the functionality for shapes. It contains the shape class which, in turn, contains a shape class method for rendering the shape.

Dependencies: pygame, os, random


'''
import pygame, os, random

pygame.init()

class Shape():
    '''
    Shape class
    Description: Holds functions responsible grabbing specific shapes, color and type, from the game assets
    and rendering them on the grids. 
    '''
    def __init__(self, color, tipe):
        '''
        Initializes the class
        Description: Loads the shape's image based on its color and type and scales them to 64x64.
        '''
        self.color = color
        self.type = tipe
        self.image = pygame.image.load(os.path.join('assets', 'images','.'.join([f'{color}_{tipe}', 'png'])))
        self.image = pygame.transform.scale(self.image, (64,64))

        self.pos = (0,0)

    def render(self, surf, pos):
        '''
        Renders the shape class instance with a specified surface and position.
        '''
        self.pos = pos
        surf.blit(self.image, self.pos)



        
