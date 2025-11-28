'''
Utilities module
'''

import pygame, random
from defaults import *
from rule import *
from grid import *

pygame.init()

''' global variables '''
scrx, scry = 720, 480
# scrx, scry = 1080, 720
center = (scrx/2,scry/2)


text = pygame.font.SysFont('comic_sans',20)
button = pygame.font.SysFont('comic_sans',36)


''' global classes '''


class Button():
    def __init__(self, pos, image):
        self.pos = pos
        self.text = 'CVBNM'
        self.status = False
        
        self.image = pygame.image.load(os.path.join('assets', image))
        self.image = pygame.transform.scale(self.image, (128, 64))
        self.image.set_colorkey('white')

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos


    def update(self): 
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            if not self.status:
                self.status = True
            else:
                self.status = False

    def message(self, surf, msg, color):
        self.text = text.render(msg, 0, color)

    def render(self, surf, clickable):
        # pygame.draw.rect(surf, 'violet', self.rect)
        if clickable:
            surf.blit(self.image, self.pos)
        else:
            surf.blit(pygame.transform.hsl(self.image, hue=-120, saturation=-1, lightness=0), self.pos)
        
            

        
        
        
