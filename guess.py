'''
Guessing module

'''
import pygame, os
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

    
    

