'''
Windows Module

Overview

Dependencies

'''
import pygame, os, math
from utils import *
from shape import *
from rule import *

pygame.init()

class Window():
    '''
    Window Class
    Description: Class template for all objects that involve a window being displayed on top of the player's screen
    '''

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.image = pygame.image.load(os.path.join('assets', 'images', 'window.png'))
        self.image = pygame.transform.scale(self.image, self.size)
        self.window = pygame.Surface(size)
        self.window = pygame.transform.scale(self.window, self.size)
        
    def render(self, surf):
        '''
        Renders the window to the surface 
        '''
        surf.blit(self.window, self.pos)

class Guess(Window):
    '''
    Window Class
    Description: Class template for all objects that involve a window being displayed on top of the player's screen
    '''
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image = pygame.image.load(os.path.join('assets', 'images', 'guess_menu.png'))
        self.image = pygame.transform.scale(self.image, (360,240))
        self.number = 0

    def guess(self, surf, inp):
        self.number = -inp[1] % 4
        self.shape = Shape(attributes['color'][(inp[2]) % 3], attributes['shape'][(inp[3]) % 2])

        self.window.blit(self.image)

        self.window.blit(text.render('Amount', 0, 'black'), (64,32))
        self.window.blit(text.render('Shape and Color', 0, 'black'), (128+32,32))

        self.window.blit(text.render(f'{self.number}', 0, 'black'), (64+16,64+16))
        self.shape.render(self.window, (128+16+32,64+16))

        self.render(surf)

        return [self.number, self.shape.color, self.shape.type]

class Pause(Window):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image = pygame.image.load(os.path.join('assets', 'images', 'pause.png'))
        self.image = pygame.transform.scale(self.image, self.size)
        self.window = pygame.Surface(size)
        self.window = pygame.transform.scale(self.window, self.size)
        self.window.set_colorkey('black')


        self.exit_button = Button((size[0]/2 - 80,size[1]/2 - 32 + 48), 'resume_button.png', (238 * 0.63,114 * 0.63))
        self.exit_button.rect.x += self.pos[0]
        self.exit_button.rect.y += self.pos[1]
        self.resume_button = Button((size[0]/2 - 128,size[1]/2 - 32 - 48), 'menu_button.png', (248,73))
        self.resume_button.rect.x += self.pos[0]
        self.resume_button.rect.y += self.pos[1]

    def pause(self, surf):
        self.window.blit(self.image)

        self.exit_button.update()
        self.resume_button.update()

        if self.resume_button.status:
            self.resume_button.status = False
            return 1
        if self.exit_button.status:
            self.exit_button.status = False
            return 2
        

        self.render(surf)

    def render(self, surf):
        self.exit_button.render(self.window, True)
        self.resume_button.render(self.window, True)
    
        surf.blit(self.window, self.pos)
