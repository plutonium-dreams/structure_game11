'''
Windows Module

Overview: This module aims to group together all of the functionality that involves a window being displayed on the player's screen. This includes the pause and guess menus. A Window class was made in order to provide a template from which subsequent windows could inherit from.

Dependencies: pygame, os, math, utils, shape, rule

'''
import pygame, os, math
from utils import *

pygame.init()

class Window():
    '''
    Window Class
    Description: Class template for all objects that involve a window being displayed on top of the player's screen
    '''

    def __init__(self, pos, size):
        '''
        Initializes the Window class instance
        Description: Creates a surface for the window itself based on the specified size. Said surface will aid in rendering the window and all of its elements.
        '''
        self.pos = pos
        self.size = size
        self.window = pygame.Surface(self.size)
        self.window = pygame.transform.scale(self.window, self.size)
        
    def render(self, surf):
        '''
        Render Method
        Description: Renders the window to the surface and position specified
        '''
        surf.blit(self.window, self.pos)


class Guess(Window):
    '''
    Guess Class
    Description: This is a class for the guessing menu window. It enables the player to place their guess for the secret rule. Inherits class methods and attributes from the window class.
    '''
    def __init__(self, pos, size):
        '''
        Initializes the Guess class instance
        Loads the image for the guess menu background and scales it appropriately.
        '''
        super().__init__(pos, size)
        self.image = pygame.image.load(os.path.join('assets', 'images', 'guess_menu.png'))
        self.image = pygame.transform.scale(self.image, self.size)
        self.image = pygame.transform.scale_by(self.image, 1.1)
        self.number = 0

    def guess(self, surf, inp):
        '''
        Guess Function
        Description: Backend for the guessing mechanic. Takes the list inp as user input and uses specific list elements (that can be modified by keyboard input) to determine the amount and shape that the player wishes to input for their guess. This information is then used to render the amount and shape from the window surface.
        '''
        self.number = attributes['quantity'][-inp[1] % len(attributes['quantity'])]
        self.shape = Shape(attributes['color'][(inp[2]) % 3], attributes['shape'][(inp[3]) % 2])

        self.window.blit(self.image, (-10,-10))

        self.window.blit(nametext.render(f'{self.number}', 0, 'black'), (64,64+48))
        self.shape.render(self.window, (128+112,64+48))

        self.render(surf)

        return [self.number, self.shape.color, self.shape.type]

class Pause(Window):
    '''
    Pause Class
    Description: Class for the pause menu. Inherits class methods and attributes from the window class.
    '''
    def __init__(self, pos, size):
        '''
        Pause Class Initialization
        Description: Initializes the pause class instance with the necessary images and buttons give its position (pos) and size.
        '''
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
        '''
        Pause Method
        Description: Provides functionality for the resume and menu buttons and calls the render method of the class instance to draw the button images as well as the pause window image to the screen.
        '''
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
        '''
        Render Method
        Description: Calls the menu and resume button instances' render methods and blits them to the pause class instance's surface. Then, the said surface is blitted on the surface placed in the argument (usually the surface for the screen)
        '''
        self.exit_button.render(self.window, True)
        self.resume_button.render(self.window, True)
    
        surf.blit(self.window, self.pos)