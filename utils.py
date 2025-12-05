'''
Utilities module
'''

import pygame, random
from defaults import *
from rule import *
from grid import *


pygame.init()



''' global module dependent variables '''

text = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),28)
nametext = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),36)
wintext = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),46)

if os.path.exists(os.path.join('data', 'highscores.txt')):
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'r')
    highscores_file.close()
else:
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'x')
    highscores_file.close()
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'r')
    highscores_file.close()

''' global functions '''




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
        
            
class Timer():
    def __init__(self, pos):
        global scrx
        global wins

        self.duration = scrx
        self.pos_copy = pos
        self.pos_1 = list(pos)
        self.pos_2 = [self.duration + pos[0], pos[1]]
        self.velocity = 10

    def reset(self):
        self.duration = scrx
        self.pos_1 = list(self.pos_copy)
        self.pos_2 = [self.duration + self.pos_copy[0], self.pos_copy[1]]

    def render(self, surf):
        if self.duration > 0:
            self.pos_1[0] += self.velocity
            self.duration -= self.velocity
            
            self.surface = pygame.Surface((scrx, 64))
            self.surface.fill('dark gray')
            self.surface.set_alpha(80)

            surf.blit(self.surface, (self.pos_1[0], self.pos_1[1]))

            
class Highscore():
    def __init__(self, pos):
        global name
        self.pos = pos
        self.name = name

        self.highscores = list()
        with open(os.path.join('data', 'highscores.txt'), 'r') as highscores_file:
            for score in highscores_file:
                self.highscores.append(score)
        
        self.button_A = Button((pos[0]+8,pos[1]), 'upbutton1.png', (64, 64))
        self.button_B = Button((pos[0]+72, pos[1]), 'upbutton1.png', (64, 64))
        self.button_C = Button((pos[0]+136, pos[1]), 'upbutton1.png', (64, 64))
        self.buttons = [self.button_A, self.button_B, self.button_C]

        self.leaderboard_image = pygame.image.load(os.path.join('assets', 'images', 'leaderboard.png'))

        self.A = 0
        self.B = 0
        self.C = 0

        self.state = [0,0,0]

        
    def update(self):
        self.state = [(self.A % 26) + 65, (self.B % 26) + 65, (self.C % 26) + 65]
        
        for button in self.buttons:
            button.update()

        if self.button_A.status:
            self.A += 1
            self.button_A.status = False
        if self.button_B.status:
            self.B += 1
            self.button_B.status = False
        if self.button_C.status:
            self.C += 1
            self.button_C.status = False

        # print(self.state)
    
    def save_highscore(self, name, wins):
        with open(os.path.join('data', 'highscores.txt'), 'a') as highscores_file:
            highscores_file.write(f'{name}:{wins}\n')
    
    def sort_s(self, e):      # for sorting the high scores
        return e[3:e.find('\n')]

    def sort_highscores(self):
        sort = []
        for score in self.highscores:
            if int(score[4:score.find('\n')]) >= 100:
                sort.append(score)
        for score in self.highscores:
            if 10 <= int(score[4:score.find('\n')]) < 100:
                sort.append(score)
            self.highscores.sort(reverse=True, key=self.sort_s)
        for score in self.highscores:
            if 1 <= int(score[4:score.find('\n')]) < 10:
                sort.append(score)
            self.highscores.sort(reverse=True, key=self.sort_s)
        return sort


    def render(self, surf):
        for button in self.buttons:
            button.render(surf, True)
        
        surf.blit(self.leaderboard_image, (self.pos[0]+8, self.pos[1]-290))

        for i in range(len(self.state)):
            surf.blit(nametext.render(chr(self.state[i]), 0, 'black'), (32 + self.pos[0] + 64 * i, self.pos[1]-32))

        for i in range(5):
            try:
                score = nametext.render(self.sort_highscores()[i], 0, 'black')
            except IndexError:
                score = nametext.render('-------', 0, 'black')
            surf.blit(score, (self.pos[0]+64, (self.pos[1]-234) + 32*i))
        
        

        
        # print(self.highscores)
        # print(self.sort_highscores())

    def savename(self):
        name = ''
        for i in self.state:
            name += chr(i)
        
        return name
        
        

