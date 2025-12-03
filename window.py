'''
Pop-ups module

'''
import pygame, os, math
from utils import *
from shape import *
from rule import *

pygame.init()

class Window():
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.image = pygame.image.load(os.path.join('assets', 'images', 'window.png'))
        self.image = pygame.transform.scale(self.image, self.size)
        self.window = pygame.Surface(size)
        self.window = pygame.transform.scale(self.window, self.size)
        
    def render(self, surf):
        surf.blit(self.window, self.pos)

class Guess(Window):
    def __init__(self, pos, size):
        super().__init__(pos, size)
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
        self.exit_button = Button((size[0]/2 - 64,size[1]/2 - 32 - 48), 'button.png', (128,64))
        self.exit_button.rect.x += self.pos[0]
        self.exit_button.rect.y += self.pos[1]
        self.resume_button = Button((size[0]/2 - 64,size[1]/2 - 32 + 48), 'button.png', (128,64))
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
