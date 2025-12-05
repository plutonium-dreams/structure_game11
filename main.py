'''
Zendo Game for Math 153 Final Project

Controls:
WASD - up down left right
J - cycle through the colors
K - cycle through the shapes
SPACE - place piece
ENTER - verify structure
ESCAPE - go back to main menu
click green button to put in guess

To do list:
[/] create a secret rule 
[/] generate grids that follow the secret rule  
[/] render the grids
[/] user grid creation
[/] player grid verification
[/] guessing mechanic
[/] make the game restart with points for each won round
[/] add a delete button for the structure creation
[/] make a button class
[/] add a main menu
[/] add a timer function
[/] fix the shape appearing on guess mode and on hand (make them the same counters nalang)
[/] add a high score system
[/] make the guess mode amount counter always be 0
[/] polish the timer system
[/] game polishing
    - make the computer present one correct and one wrong structure
    - add more rules, possible variation
        - add orientation/pointing/grounded
    - add the ability to delete a placed piece
    - more polished assets
    - add a main menu system with easy and hard levels
[/] remove the zero amount thing
[/] add a no timer mode
[/] translucent timer
[/] add the graphics
'''
import pygame, random, sys
from utils import *
from defaults import *
from grid import *
from rule import *
from shape import *
from window import *


''' initialize '''
pygame.init()

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()


''' functions that cant go anywhere else'''
timer = Timer((0, center[1]-32))
# (323,187)
guess_window = Guess((scrx/4, scry/4), (360,240))
pause_window = Pause((25, 25), (scrx * 7/8 + 32, scry * 7/8))

hand = Shape(attributes['color'][0], attributes['shape'][0]) # default hand

# buttons
guess_button = Button((64, scry - (scry/4)-32), 'button.png', (128, 64))
start_button = Button((center[0]-128-32, center[1]+128), 'start_button.png', (160, 80))
timer_button = Button((center[0]-256-48, center[1]+128), 'timer_button.png', (256*0.4, 186*0.4))

''' main functions '''
# new game
secret_rule = []
fake_rule = []

grid_1 = Grid((scrx/4, 128))
grid_2 = Grid((3*scrx/4, 128))

player = PlayerGrid((center[0], scry - (scry/4)))

def newGame():
    global grid_1
    global grid_2
    global secret_rule
    global fake_rule

    secret_rule = generateSecretRule()
    fake_rule = generateSecretRule()
    while fake_rule == secret_rule:
        fake_rule = generateSecretRule()

    grid_1.genGrid(secret_rule)
    grid_2.genGrid(fake_rule)
    if grid_2.checkGrid(secret_rule):       # needs to be more efficient so that grid 2 can never accidentally follow the secret rule even when its following the fake rule
        return newGame()

    print(f'Secret Rule: {secret_rule}')
    print()
    print(grid_1)
    print()
    print(grid_2)



# main menu
def menu():
    global inp
    global name
    global highscore

    highscore = Highscore((center[0]+128+16, center[1]+128))

    title = pygame.image.load(os.path.join('assets', 'images', 'title.png'))
    title = pygame.transform.scale_by(title, 9/10)



    while True:
        window.fill(('gray'))

        window.blit(pygame.image.load(os.path.join('assets', 'images', 'paperclips.png')))

        
        start_button.render(window, True)
        window.blit(title, (center[0] - title.get_width()/2-94,center[1]-title.get_height()/2-64))

        

        highscore.update()

        highscore.render(window)

        start_button.update()
        if start_button.status:
            start_button.status = False
            name = highscore.savename()
            return game()

        timer_button.update()
        if timer_button.status:             # on/off status of the timer present button
            Button((center[0]-256-48, center[1]+128), 'timer_button.png', (256*0.4, 186*0.4)).render(window, True)
        else:
            timer_button.render(window, False)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    inp[1] -= 1
                if event.key == pygame.K_s:
                    inp[1] += 1
                if event.key == pygame.K_d:
                    inp[0] += 1
                if event.key == pygame.K_a:
                    inp[0] -= 1
                if event.key == pygame.K_RETURN:
                    start_button.status = False
                    name = highscore.savename()
                    return game()

        pygame.display.update()
        pygame.clock.tick(60)
        pygame.display.set_caption(f'Arki (working prototype) {pygame.clock.get_fps()}')



# main game loop
def game():
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

    # default values
    wins = 0
    inp = [0,0,0,0,0]
    player.clear()
    verifies = 0
    correct_verifies = False
    draw_guess = False
    
    guess_button.status = False
    timer.reset()

    # backgrounds
    bg_num = random.randint(1,3)

    grid_wrapper = pygame.image.load(os.path.join('assets', 'images', 'grid_wrapper.png')).convert_alpha()
    grid_wrapper = pygame.transform.scale_by(grid_wrapper, 1.1)
    grid_wrapper = pygame.transform.hsl(grid_wrapper, hue=240, saturation=1, lightness=0.1)
    # grid_wrapper.set_alpha(1)
    grid_wrapper = grid_wrapper.premul_alpha()

    # player dashboard
    dashboard = pygame.image.load(os.path.join('assets', 'images', 'dashboard.png'))
    dashboard = pygame.transform.scale_by(dashboard, 1)
    

    # audio
    if timer_button.status:
        pygame.mixer.music.load(os.path.join('assets', 'audios', 'funk.mp3'))
    else:
        pygame.mixer.music.load(os.path.join('assets', 'audios', 'zen.mp3'))

    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    
    newGame()               # NEW GAME
    
    while True:
        # print(timer.velocity)
        ''' rendering '''
        bg = pygame.image.load(os.path.join('assets', 'images', f'bg{bg_num}.png')).convert()
        bg = pygame.transform.smoothscale(bg, (scrx, scry))
        window.blit(bg, (0,0))
        # window.fill('gray')

        # window.blit(pygame.image.load(os.path.join('assets', 'images', 'paperclips.png')))

        if timer_button.status:
            timer.render(window)

        # computer 
        # window.blit(grid_wrapper, (scrx/4 - 96-9, 128 - 96-9), special_flags=pygame.BLEND_RGBA_MIN)       # draws the background of the grids; put inside the computer function in the grid class
        # window.blit(grid_wrapper, (3 * scrx/4 - 96-9, 128 - 96-9), special_flags=pygame.BLEND_PREMULTIPLIED)
        
        grid_1.render(window)
        grid_2.render(window)
        # pygame.draw.circle(window, 'black', center, 5)
        pygame.draw.circle(window, 'black', (scrx/4-128-16, 128), 32)
        pygame.draw.circle(window, 'white', (3 * scrx/4 + 128 + 16, 128), 32)

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
            return menu()

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
                return menu()
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
 
                            # pygame.mixer.music.set_volume(1)
                            # pygame.mixer.music.load(os.path.join('assets', 'audios', 'correct.mp3'))
                            # pygame.mixer.music.play()
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


        ''' technical stuff'''
        pygame.display.update()
        pygame.clock.tick(60)
        pygame.display.set_caption(f'Arki (working prototype) {pygame.clock.get_fps()}')


''' run the game '''
menu()    