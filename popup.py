'''
Pop-ups module

'''
import pygame, os, math
from utils import *
from shape import *
from rule import *

pygame.init()

# guess_window = pygame.Surface((360,240))
# guess_image = pygame.image.load(os.path.join('assets', 'images', 'window.png'))
# guess_window = pygame.transform.scale(guess_window, (360,240))

# def guess(surf, inp):
#     guess_num = -inp[1] % 4
#     guess_shape = Shape(attributes['color'][(inp[2]) % 3], attributes['shape'][(inp[3]) % 2])

#     # guess_window.fill('black')
#     # pygame.draw.rect(guess_window, 'dark gray', ((16,16), (360-32, 240-32)))
#     guess_window.blit(guess_image, (0,0))

#     guess_window.blit(text.render('Amount', 0, 'black'), (64,32))
#     guess_window.blit(text.render('Shape and Color', 0, 'black'), (128+32,32))

#     guess_window.blit(text.render(f'{guess_num}', 0, 'black'), (64+16,64+16))
#     guess_shape.render(guess_window, (128+16+32,64+16))

#     surf.blit(guess_window, (scrx/4, scry/4))

#     return [guess_num, guess_shape.color, guess_shape.type]

# pause_window = pygame.Surface((256, 128))

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
        self.velocity = 0

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

        print(self.velocity)

class Highscore():
    def __init__(self, pos, highscores):
        self.pos = pos
        self.name = 'XYZ'

        self.highscores = highscores
        
        self.button_A = Button(pos, 'button.png', (64, 64))
        self.button_B = Button((pos[0]+64, pos[1]), 'button.png', (64, 64))
        self.button_C = Button((pos[0]+128, pos[1]), 'button.png', (64, 64))
        self.buttons = [self.button_A, self.button_B, self.button_C]

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
    
    def sort_highscores(self):
        sort = []
        for score in self.highscores:
            if int(score[4:score.find('\n')]) >= 100:
                sort.append(score)
        for score in self.highscores:
            if 10 <= int(score[4:score.find('\n')]) < 100:
                sort.append(score)
            self.highscores.sort(reverse=True, key=sort_s)
        for score in self.highscores:
            if 1 <= int(score[4:score.find('\n')]) < 10:
                sort.append(score)
            self.highscores.sort(reverse=True, key=sort_s)
        return sort


    def render(self, surf):
        for button in self.buttons:
            button.render(surf, True)
        
        for i in range(len(self.state)):
            surf.blit(nametext.render(chr(self.state[i]), 0, 'black'), (32 + self.pos[0] + 64 * i, self.pos[1]-32-16))

        for i in range(5):
            try:
                score = nametext.render(self.sort_highscores()[i], 0, 'black')
            except IndexError:
                score = nametext.render('-------', 0, 'black')
            surf.blit(score, (self.pos[0]+64, (self.pos[1]-224) + 32*i))
        
        surf.blit(nametext.render('High Scores',0,'gold', bgcolor='black'), (self.pos[0]+48, self.pos[1]-272))
        # print(self.highscores)
        # print(self.sort_highscores())

    def savename(self):
        name = ''
        for i in self.state:
            name += chr(i)
        
        return name
        
''' dependent variables '''
timer = Timer((0, center[1]-32), 1)    
guess_window = Guess((scrx/4, scry/4), (360,240))
pause_window = Pause((25, 25), (scrx * 7/8 + 32, scry * 7/8))