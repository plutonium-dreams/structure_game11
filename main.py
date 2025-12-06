'''
ARKITEK

Group Mayad's Final Project for Math 153
    Kent Nico Balondro
    Josef Vincent Jaen
    John Christian Nobleza
    TJ Nathan Santillan


Controls:
WASD - up down left right
J - cycle through the colors
K - cycle through the shapes
SPACE - place piece
ENTER - verify structure
ESCAPE - go back to main menu
TAB or click green button to put in guess

'''

'''
Main Module

Overview: The primary python script of the program. Handles most of the pygame functionality, as well as rendering and user input.

Dependencies: pygame, random, os, sys, utils, defaults, grid, rule, shape, window
'''
import pygame, random, os, sys
from utils import *
from defaults import *
from grid import *
from rule import *
from shape import *
from window import *

''' Initialization '''
# initializes the pygame-related variables
pygame.init()

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()
pygame.display.set_caption('ARKI GAME')

# initializes the class instances for the timer, guess window, pause window, and the player's hand
timer = Timer((0, center[1]-32))                        
guess_window = Guess((scrx/4, scry/4), (360,240))       
pause_window = Pause((25, 25), (scrx * 7/8 + 32, scry * 7/8))       
hand = Shape(attributes['color'][0], attributes['shape'][0]) 

# initializes buttons for guess, start, and timer
guess_button = Button((64, scry - (scry/4)-32), 'button.png', (128, 64))
start_button = Button((center[0]-128-32, center[1]+128), 'start_button.png', (160, 80))
timer_button = Button((center[0]-256-48, center[1]+128), 'timer_button.png', (256*0.4, 186*0.4))

# intializes the game loop functionality: the secret rule, the computer grids, the player's editable grid
secret_rule = []

grid_1 = Grid((scrx/4, 128))
grid_2 = Grid((3*scrx/4, 128))

player = PlayerGrid((center[0], scry - (scry/4)))

def newGame():
    '''
    New Game Function
    Description: This function is called at the start of the game or after a successful guess in order to create a new set of grids (one that follows the new secret rule, one does not) to present to the player. 
    '''
    global grid_1
    global grid_2
    global secret_rule

    # this block creates two rules, one will be secret rule that the left grid follows and the other is a false rule that the right grid will follow
    secret_rule = generateSecretRule()
    fake_rule = generateSecretRule()
    # in the case of both rules being the same, we generate another false rule until both are no longer the same
    while fake_rule == secret_rule:
        fake_rule = generateSecretRule()


    # this block is responsible for generating the grids one based on the secret rule and the other on the fake rule
    grid_1.genGrid(secret_rule)
    grid_2.genGrid(fake_rule)
    # if the false grid's structure somehow follows the secret rule, we exit do the whole process all over again
    if grid_2.checkGrid(secret_rule):
        return newGame()


    # For debugging purposes:
    # print(f'Secret Rule: {secret_rule}')
    # print()
    # print(grid_1)
    # print()
    # print(grid_2)



''' Game Screens'''

# start screen
def start():
    '''
    Start Function
    Description: This function compiles many of the built functionality to create the start screen of the game. 
    '''
    global inp
    global name
    global highscore

    # highscore class instance initialized here in order for the leaderboards to be updated after every run
    highscore = Highscore((center[0]+128+16, center[1]+128))    

    # loading and modification of images for the title, start background, and decorative paperclips
    title = pygame.image.load(os.path.join('assets', 'images', 'title.png'))
    title = pygame.transform.scale_by(title, 9/10)
    title = pygame.transform.hsl(title, 0, -0.5, 0.2)
    title = pygame.transform.invert(title)

    start_bg = pygame.image.load(os.path.join('assets', 'images', 'start_bg.png'))
    start_bg = pygame.transform.scale_by(start_bg, 2)
    start_bg = pygame.transform.hsl(start_bg, 160, -0.5, 0)

    paperclips = pygame.image.load(os.path.join('assets', 'images', 'paperclips.png'))
    paperclips = pygame.transform.rotozoom(paperclips, 90, 1.2)
    paperclips = pygame.transform.invert(paperclips)


    # game loop for the start screen
    while True:
        ''' Rendering '''
        window.fill(('gray'))
        window.blit(start_bg, (-15,-15))
        window.blit(paperclips, (-20, -25))
        window.blit(title, (center[0] - title.get_width()/2-94,center[1]-title.get_height()/2-64))

        start_button.render(window, True)
        
        highscore.update()
        highscore.render(window)


        ''' Logic '''
        # start button functionality; saves the inputted name once the player clicks it
        start_button.update()
        if start_button.status:
            start_button.status = False
            name = highscore.savename()
            return game()

        # timber button functionality
        timer_button.update()
        if timer_button.status:             # on/off status of the timer present button
            Button((center[0]-256-48, center[1]+128), 'timer_button.png', (256*0.4, 186*0.4)).render(window, True)
        else:
            timer_button.render(window, False)

        ''' Input detection '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # exits the game if the player presses the close button on the program's title bar
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:    # starts the game if the player presses enter
                    start_button.status = False
                    name = highscore.savename()
                    return game()


        ''' Pygame Backend '''
        pygame.display.update()     # updates the display
        pygame.clock.tick(60)       # sets game to be 60 fps


# main game screen
def game():
    '''
    Game Functiom
    Description: This is THE program's main function. It essentially contains the main game loop of the program and where the player is gonna spend the most of their time. 
    '''
    global inp
    global clr
    global shp
    global verifies
    global correct_verifies
    global wins
    global draw_guess
    global paused
    global hand
    global highscore
    global secret_rule


    ''' Initialization'''
    # initialize default values
    wins = 0
    inp = [0,0,0,0,0]
    player.clear()
    verifies = 0
    correct_verifies = False
    draw_guess = False
    
    guess_button.status = False
    timer.reset()

    # initialize and transform the images that will be used
    bg_num = random.randint(1,3)        # background is determined at random

    # player dashboard
    dashboard = pygame.image.load(os.path.join('assets', 'images', 'dashboard.png'))
    dashboard = pygame.transform.scale_by(dashboard, 1)
    

    # initialize the audio
    if timer_button.status:         # arcade mode
        pygame.mixer.music.load(os.path.join('assets', 'audios', 'bop.mp3'))
    else:                           # zen mode
        pygame.mixer.music.load(os.path.join('assets', 'audios', 'soothe.mp3'))

    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    
    # call new game to initialize a new board
    newGame()
    
    while True:
        ''' rendering '''
        bg = pygame.image.load(os.path.join('assets', 'images', f'bg{bg_num}.png')).convert()       # background image loaded here so that it can change every time a correct guess is made.
        bg = pygame.transform.smoothscale(bg, (scrx, scry))
        window.blit(bg, (0,0))

        # renders the timer if the player chooses to turn it on
        if timer_button.status:
            timer.render(window)
        
        
        grid_1.render(window)
        grid_2.render(window)
        # pygame.draw.circle(window, 'black', center, 5)
        pygame.draw.circle(window, 'black', (scrx/4-128-16, 128), 32)
        pygame.draw.circle(window, 'white', (3 * scrx/4 + 128 + 16, 128), 32)
        pygame.draw.rect(window, 'white', ((scrx/4-128-16, 128), (64, 64)))

        # player area
        player.render(window)
        
        guess_button.render(window, correct_verifies)

        window.blit(dashboard, (scrx-128-96-16, scry - (scry/4)-96-16))

        # hand
        hand.render(window, (scrx-128-32, scry - (scry/4)+16))

        window.blit(wintext.render(f'{wins}', 0, 'black'),(scrx-96, scry - (scry/4)-64-8))


        ''' logic '''
        if not (guess_button.status and correct_verifies) and not paused:
            player.playerUpdate(window, inp)
            hand = Shape(attributes['color'][inp[2] % 3], attributes['shape'][inp[3] % 2])

        if correct_verifies:        # only when the player has a valid structure that they can click the guess button
            guess_button.update()

        # timer
        if timer_button.status and timer.duration <= 0:
            pygame.mixer.music.stop()
            highscore.save_highscore(name, wins)
            return start()

        # clicking on the guess button will bring up the guess menu
        if guess_button.status and correct_verifies:
            gss = guess_window.guess(window, inp)
            
        # pausing
        if paused:
            pause_value = pause_window.pause(window)
            timer.velocity = 0
            if pause_value == 1:
                pygame.mixer.music.stop()
                paused = False
                return start()
            if pause_value == 2:
                paused = False
        else:
            timer.velocity = wins * 0.1 + 0.1


        ''' event handling '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()

            # mouse input handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                if guess_button.status:
                    correct_verifies = False
                    guess_button.status = False
                if not guess_button.status and correct_verifies:
                    inp[0], inp[1] = 0,0

            # keyboard input handling
            if event.type == pygame.KEYDOWN:
                if not paused:
                    if event.key == pygame.K_w:
                        inp[1] -= 1
                        
                    if event.key == pygame.K_s:
                        inp[1] += 1
                    if event.key == pygame.K_d:
                        inp[0] += 1
                    if event.key == pygame.K_a:
                        inp[0] -= 1
                    
                    # for placing a piece; and not draw_guess for all these
                    if event.key == pygame.K_SPACE:
                        if not guess_button.status:
                            player.place(hand.color, hand.type)
                    if event.key == pygame.K_j:
                        inp[2] += 1
                    if event.key == pygame.K_k:
                        inp[3] += 1
                    if event.key == pygame.K_RETURN:
                        if not guess_button.status:
                            if player.checkGrid(secret_rule):
                                correct_verifies = True
                        
                        if guess_button.status:
                            if gss == secret_rule:
                                wins += 1
                                inp[0], inp[1] = 4,4
                                timer.velocity += 0.1
                                timer.reset()
                                player.clear()
                                
                                if not timer_button.status:
                                    bg_num = random.randint(1,3)

                                newGame()
                                
                            
                            correct_verifies = False
                            guess_button.status = False
                        
                    if event.key == pygame.K_BACKSPACE:
                        if not guess_button.status:
                            player.clear()

                    if event.key == pygame.K_TAB:
                        if not guess_button.status and correct_verifies:
                            inp[0], inp[1] = 0,0
                            guess_button.status = True
                        else:
                            correct_verifies = False
                            guess_button.status = False

                if event.key == pygame.K_ESCAPE:
                    if not paused:
                        paused = True
                    else:
                        paused = False


        ''' Pygame Backend '''
        pygame.display.update()     # updates the display
        pygame.clock.tick(60)       # sets the game to 60 fps
        
        # For debugging purposes
        # pygame.display.set_caption(f'Arki (working prototype) {pygame.clock.get_fps()}')


''' run the game '''
start()    