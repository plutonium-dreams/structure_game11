'''
Utilities Module

Overview: This module groups all of the code necessary for the game's utilities. This includes the Button, Timer, and Highscore classes. In addtion, the game's fonts are loaded in this module.

Dependencies: pygame, os, defaults, rule, grid

'''

import pygame, os, random
from defaults import *
from grid import *

pygame.init()

# Initializes the fonts used in the program.
text = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),28)
nametext = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),36)
wintext = pygame.font.Font(os.path.join('assets', 'fonts', 'Sofia_Handwritten.otf'),46)

# Creates a highscore text file if it does not exist.
if not os.path.exists(os.path.join('data', 'highscores.txt')):
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'x')
    highscores_file.close()
    highscores_file = open(os.path.join('data', 'highscores.txt'), 'r')
    highscores_file.close()

# initializes the game's sounds
pygame.mixer.init()
start_game_sound = pygame.Sound(os.path.join('assets', 'audios', 'start_game.mp3'))
end_game_sound = pygame.Sound(os.path.join('assets', 'audios', 'end_game.mp3'))
button_sound = pygame.Sound(os.path.join('assets', 'audios', 'button_sound.mp3'))
select_sound = pygame.Sound(os.path.join('assets', 'audios', 'select_sound.mp3'))
valid_board_sound = pygame.Sound(os.path.join('assets', 'audios', 'valid_board.mp3'))
invalid_board_sound = pygame.Sound(os.path.join('assets', 'audios', 'invalid_board.mp3'))
correct_guess_sound = pygame.Sound(os.path.join('assets', 'audios', 'correct_guess.mp3'))
wrong_guess_sound = pygame.Sound(os.path.join('assets', 'audios', 'wrong_guess.mp3'))

channel_1 = pygame.Channel(1)
channel_2 = pygame.Channel(2)

channel_1.set_volume(0.5)
channel_2.set_volume(0.4)

class Button():
    '''
    Button Class
    Description: This class is a template for all buttons used in the game. It has class methods for updating and rendering the class instance.
    '''
    def __init__(self, pos, image, scale):
        '''
        Initialize the button class instance
        Description: An image is loaded based on the inputted filename. This image is then used to create a pygame surface with a specified scale. Furthermore, a pygame rect object is made based on the image surface.
        '''
        self.pos = pos
        self.status = False
        
        self.image = pygame.image.load(os.path.join('assets', 'images', image))
        self.image = pygame.transform.scale(self.image, scale)
        self.image.set_colorkey('white')

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos

        self.sound = button_sound

    def update(self):
        '''
        Update Method
        Description: Checks if the mouse cursor hovers over the button instance's rect and if the left mouse button was clicked. The status variable of the button instance is modified depending on its boolean value in the case that the if condition becomes true.
        '''
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            if not self.status:
                channel_1.play(self.sound)
                self.status = True
            else:
                channel_1.play(self.sound)
                self.status = False

    def render(self, surf, clickable):
        '''
        Render Method
        Description: Renders the button class instance to the specified surface (usually the window). A clickable parameter is present in order to have buttons that have different functionality depending on its clickability.
        '''
        if clickable:
            surf.blit(self.image, self.pos)
        else:
            surf.blit(pygame.transform.hsl(self.image, hue=-120, saturation=-1, lightness=0), self.pos)
        
            
class Timer():
    '''
    Timer Class
    Description: This class is for the game's timer for its arcade-style gameplay. It has reset and render methods for the class instance.
    '''
    def __init__(self, pos):
        '''
        Initializes the timer class instance
        Description: The specified position (pos) of the timer is initialized as well as the duration and velocity of said timer.
        '''
        global scrx
        global wins

        self.duration = scrx
        self.pos_copy = pos
        self.pos = list(pos)
        self.velocity = 0

    def reset(self):
        '''
        Reset Method
        Description: Resets the timer by reassigning the instance duration with the original duration.
        '''
        self.duration = scrx
        self.pos = list(self.pos_copy)
    
    def render(self, surf):
        '''
        Render Method
        Description: Renders the timer class instance on the specified pygame surface (usually the window). Also calculates how much of the timer to be drawn by creating a new surface with a specific color and alpha level and a decreasing size while the class instance's duration is greater than 0.
        '''
        if self.duration > 0:
            self.pos[0] += self.velocity
            self.duration -= self.velocity
            
            self.surface = pygame.Surface((scrx, 64))
            self.surface.fill('dark gray')
            self.surface.set_alpha(80)

            surf.blit(self.surface, (self.pos[0], self.pos[1]))

            
class Highscore():
    '''
    Highscore Class
    Description: A container for all functions relating to the highscore system of the game. Contains an update, save_highscore, sort, render_highscore functions.
    '''
    def __init__(self, pos):
        '''
        Initializes the highscore class instance
        Description: The highscores to be displayed on the home screen's leaderboards are intialized as well as the leaderbackground and the buttons that are used for the name functionality. 
        '''
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
        '''
        Update Method
        Description: This is for updating the letters for the name that are displayed on the leaderboard area on the homescreen. Clicking on one of the buttons increases its respective value. This value is then converted into an integer that can be converted into a character (in a later method) and placed inside the instance's state list.
        '''
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
    
    def sortS(self, e):      # for sorting the high scores
        '''
        sort_s method
        Description: A "lemma" function used in the sort_highscores method. This allows for the sorting of the highscores using the score itself.
        '''
        return e[3:e.find('\n')]

    def sortHighscores(self):
        '''
        sort_highscores method
        Description: This method sorts the highscores and returning a new sorted highscores list. This sorting is done by digit place.
        '''
        sort = []
        for score in self.highscores:       # 100s
            if int(score[4:score.find('\n')]) >= 100:
                sort.append(score)
        for score in self.highscores:       # 10s
            if 10 <= int(score[4:score.find('\n')]) < 100:
                sort.append(score)
            self.highscores.sort(reverse=True, key=self.sortS)
        for score in self.highscores:       # 1s
            if 1 <= int(score[4:score.find('\n')]) < 10:
                sort.append(score)
            self.highscores.sort(reverse=True, key=self.sortS)
        return sort

    def render(self, surf):
        '''
        Render Method
        Description: Renders the leaderboard along with its contents on the screen and the buttons and text for the name input functionality. Only the top 5 scores are rendered. If there are less than 5 scores present in the highscores text file, the program will render a string of '-' over the empty places instead.
        '''
        for button in self.buttons:
            button.render(surf, True)
        
        surf.blit(self.leaderboard_image, (self.pos[0]+8, self.pos[1]-290))

        for i in range(len(self.state)):
            surf.blit(nametext.render(chr(self.state[i]), 0, 'black'), (32 + self.pos[0] + 64 * i, self.pos[1]-32))

        for i in range(5):
            try:
                score = nametext.render(self.sortHighscores()[i], 0, 'black')
            except IndexError:
                score = nametext.render('-------', 0, 'black')
            surf.blit(score, (self.pos[0]+64, (self.pos[1]-234) + 32*i))


    def saveHighscore(self, name, wins):
        '''
        save_highscore method
        Description: Saves the player's specified name and number of points accumulated in the highscore text file with a specific string format.
        '''
        with open(os.path.join('data', 'highscores.txt'), 'a') as highscores_file:
            highscores_file.write(f'{name}:{wins}\n')

    def saveName(self):
        '''
        savename method
        Description: Saves the inputted name in the name input area of the leaderboards. It converts the triple of integers from the state list into characters and returns the new string as the player's specified name.
        '''
        name = ''
        for i in self.state:
            name += chr(i)
        
        return name

class Music():
    '''
    Music Class
    Description: A class specifically made for handling the music of the game (not the sound effects). This is so that it is easy to modify the settings regarding the music used in the game.
    '''
    def __init__(self, mode):
        '''
        Initializes the Music class instance
        Description: The instance loads 2 songs into the tracklist based on the mode given (be it arcade or zen) and sets the music volume to 70%
        '''
        pygame.mixer.init()
        self.mode = mode
        self.tracklist = []
        # loads two songs based on the mode into the tracklist
        for i in range(1,3):
            self.tracklist.append(f'{self.mode}{i}.mp3')
        pygame.mixer.music.set_volume(0.7)

    def update(self):
        '''
        Update Method
        Description: loads a random song from the tracklist, plays it, and queues a 5 second silence to be played after every song
        '''
        pygame.mixer.music.load(os.path.join('assets', 'audios', 'music', f'{self.tracklist[random.randint(0, len(self.tracklist)-1)]}'))
        pygame.mixer.music.play()
        pygame.mixer.music.queue(os.path.join('assets', 'audios', 'silence.mp3'))
        
        
        
        
        
    
        
        

