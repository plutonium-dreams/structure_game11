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
[ ] make the guess mode amount counter always be 0

[ ] polish the timer system
[ ] game polishing
    - make the computer present one correct and one wrong structure
    - add more rules, possible variation
        - add orientation/pointing/grounded
    - add the ability to delete a placed piece
    - more polished assets
    - add a main menu system with easy and hard levels
'''

import pygame, random, sys
from utils import *
from defaults import *
from grid import *
from rule import *
from shape import *
from popup import *



''' initialize '''
pygame.init()

pygame.display.set_caption('Deduction (working title)')
window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()

# buttons
guess_button = Button((64, scry - (scry/4)-32), 'button.png', (128, 64))
start_button = Button((center[0]-128-32, center[1]+128), 'button.png', (128, 64))

secret_rule = []
fake_rule = []

grid_1 = Grid((scrx/4, 128))
grid_2 = Grid((3*scrx/4, 128))

player = PlayerGrid((center[0], scry - (scry/4)))


''' global functions '''

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
        grid_1.genGrid(secret_rule)
        grid_2.genGrid(fake_rule)


    print(f'Secret Rule: {secret_rule}')
    print()
    print(grid_1)
    print()
    print(grid_2)


''' game stuff '''
hand = Shape(attributes['color'][0], attributes['shape'][0]) # default hand

''' testing stuff '''


# main menu
def menu():
    global inp
    global name
    title = pygame.image.load(os.path.join('assets', 'images', 'title.png'))
    title = pygame.transform.scale_by(title, 9/10)

    highscores = read_highscore()
    nameinput = NameInput((center[0]+128+16, center[1]+128), highscores)
    
    while True:
        window.fill(('gray'))

        start_button.render(window, True)
        window.blit(title, (center[0] - title.get_width()/2-110,center[1]-title.get_height()/2-64))

        nameinput.update()

        nameinput.render(window)


        start_button.update()

        if start_button.status:
            start_button.status = False
            name = nameinput.savename()
            return game()

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
                    name = nameinput.savename()
                    return game()

        pygame.display.update()
        pygame.clock.tick(60)



# main game loop
def game():
    global inp
    global clr
    global shp
    global verifies
    global correct_verifies
    global wins
    global draw_guess
    global hand
    timer = Timer((0, center[1]-32), 1)     # put in utils soon

    # background testing
    bg = pygame.image.load(os.path.join('assets', 'images', 'bg1.png'))
    bg = pygame.transform.hsl(bg, hue=-230, saturation=-0.2, lightness=0.1)
    # bg = pygame.transform.invert(bg)
    bg = pygame.transform.box_blur(bg, 10)
    bg = pygame.transform.smoothscale(bg, (scrx, scry))
    
    newGame()
    default()

    # pygame.mixer.music.load(os.path.join('assets', 'audios', 'country.mp3'))
    # pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    

    while True:
        
        ''' rendering '''
        # window.blit(bg, (0,0))
        window.fill('gray')

        timer.render(window)
        # computer 
        grid_1.render(window)
        grid_2.render(window)
        pygame.draw.circle(window, 'black', center, 5)
        pygame.draw.circle(window, 'black', (scrx/4-128-16, 128), 32)
        pygame.draw.circle(window, 'white', (3 * scrx/4 + 128 + 16, 128), 32)

        


        # player area
        player.render(window)

        # hand
        hand.render(window, (scrx-128, scry - (scry/4)))
        window.blit(text.render('current piece', 0, 'black'), (scrx-128-32, scry - (scry/4)-32))
        

        # interface
        # guess_button = pygame.Rect((64, scry - (scry/4)-32), (64+32, 64))
        # if correct_verifies < 1:
        #     button_status = 'dark gray'
        # else: 
        #     button_status = 'dark green'
        # pygame.draw.rect(window, button_status, guess_button)

        window.blit(text.render(f'number of verifies: {verifies}', 0, 'black'), (scrx-128-64-16, scry - (scry/4)-64))
        window.blit(text.render(f'wins: {wins}', 0, 'black'),(scrx-128-16, scry - (scry/4)-64-32))


        # guess_button.image = pygame.transform.hsl(guess_button.image, hue=-120, saturation=-1, lightness=0)
        guess_button.render(window, correct_verifies)
        

        ''' logic '''
        if correct_verifies:
            guess_button.update()

        # for the guessing mechanic
        if guess_button.status and correct_verifies:
            gss = guess(window, inp)
        else:
            player.playerUpdate(window, inp)
            hand = Shape(attributes['color'][inp[2] % 3], attributes['shape'][inp[3] % 2])

        if timer.duration <= 0:
            # make an exit function for this
            default()
            pygame.mixer.music.stop()
            guess_button.status = False
            save_highscore(name, wins)
            return menu()

        ''' event handling '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if guess_button.status:
                    correct_verifies = False
                    guess_button.status = False
                if not guess_button.status and correct_verifies:
                    inp[0], inp[1] = 0,0

            if event.type == pygame.KEYDOWN:
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
                        verifies += 1
                        if player.checkGrid(secret_rule):
                            correct_verifies = True
                    
                    if guess_button.status:
                        if gss == secret_rule:
                            wins += 1
                            inp[0], inp[1] = 4,4
                            verifies = 0
                            timer.velocity += 0.1
                            timer.reset()
                            newGame()
                            player.clear()
                        
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
                    default()
                    pygame.mixer.music.stop()
                    guess_button.status = False
                    return menu()
                        

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    pass
                if event.key == pygame.K_s:
                    pass
                if event.key == pygame.K_a:
                    pass
                if event.key == pygame.K_d:
                    pass
        

        ''' technical shi '''
        pygame.display.update()
        pygame.clock.tick(60)

menu()    
game()