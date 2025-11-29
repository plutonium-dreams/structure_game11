'''
Pop-ups module

'''
import pygame, os, math
from utils import *
from shape import *
from rule import *

pygame.init()

guess_window = pygame.Surface((360, 240))

def guess(surf, inp):
    guess_num = -inp[1] % 4

    guess_shape = Shape(attributes['color'][(2 + inp[2]) % 3], attributes['shape'][(2 + inp[3]) % 2])

    guess_window.fill('black')
    pygame.draw.rect(guess_window, 'dark gray', ((16,16), (360-32, 240-32)))

    guess_window.blit(text.render('Amount', 0, 'black'), (64,32))
    guess_window.blit(text.render('Shape and Color', 0, 'black'), (128+32,32))


    guess_window.blit(text.render(f'{guess_num}', 0, 'black'), (64+16,64+16))
    guess_shape.render(guess_window, (128+16+32,64+16))

    surf.blit(guess_window, (scrx/4, scry/4))

    return [guess_num, guess_shape.color, guess_shape.type]


class Timer():
    def __init__(self, pos, difficulty):
        global scrx
        global wins

        self.duration = scrx/2
        if difficulty == 1:
            pry = 0.5

        self.pos_copy = pos
        self.pos_1 = list(pos)
        self.pos_2 = [self.duration + pos[0], pos[1]]
        self.velocity = wins + 0.1
        
    
    def reset(self):
        self.duration = scrx/2
        self.pos_1 = list(self.pos_copy)
        self.pos_2 = [self.duration + self.pos_copy[0], self.pos_copy[1]]

    def render(self, surf):
        if self.duration > 0:
            self.pos_1[0] += self.velocity

            self.duration -= self.velocity
        if not self.duration <= 0:
            pygame.draw.rect(surf, 'dark gray', ((self.pos_1[0]+1, self.pos_1[1]), (self.duration, 64)))
            pygame.draw.rect(surf, 'dark gray', ((self.pos_2[0]-1, self.pos_2[1]), (self.duration, 64)))

