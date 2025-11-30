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


text = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),28)
nametext = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),36)
button = pygame.font.SysFont('comic_sans',36)

if os.path.exists(os.path.join('data', 'highscores.txt')):
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'r')
    highscores_file.close()
else:
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'x')
    highscores_file.close()
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'r')
    highscores_file.close()



''' global functions '''
# turn into a high score class
def sort_s(e):      # for sorting the high scores
    return e[3:e.find('\n')]

def save_highscore(name, wins):
    with open(os.path.join('data', 'highscores.txt'), 'a') as highscores_file:
        highscores_file.write(f'{name}:{wins}\n')

def read_highscore():
    highscores = list()
    with open(os.path.join('data', 'highscores.txt'), 'r') as highscores_file:
        for score in highscores_file:
            highscores.append(score)
        return highscores

# def update_highscore():
#     with open(os.path.join('data', 'highscores.txt'), 'r') as highscores_file:
#         for score in highscores_file:
#             if score[4:score.find('\n')] > highscores[score[:3]]:
#                 highscores.update({score[:3] : score[4:score.find('\n')]})




''' global classes '''

class Button():
    def __init__(self, pos, image, scale):
        self.pos = pos
        self.text = 'CVBNM'
        self.status = False
        
        self.image = pygame.image.load(os.path.join('assets', 'images', image))
        self.image = pygame.transform.scale(self.image, scale)
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
        
            

        
        
        
