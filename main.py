'''
Zendo Game for Math 153 Final Project

Controls:
WASD - up down left right
J - cycle through the colors
K - cycle through the shapes
SPACE - place piece
ENTER - verify structure
click green button to put in guess

To do list:
[/] create a secret rule 
[/] generate grids that follow the secret rule  
[/] render the grids
[/] user grid creation
[/] player grid verification
[/] guessing mechanic
[/] make the game restart with points for each won round
[ ] add a delete button for the structure creation
[ ] add the interaction rules
[ ] game polishing
    - make the computer present one correct and one wrong structure
    - add more rules, possible variation
        - add orientation/pointing/grounded
    - add the ability to delete a placed piece
    - more polished assets
    - add a main menu system with easy and hard levels
'''

import pygame, random, sys
from grid import *
from rule import *
from shape import *
from guess import *



''' initialize '''
pygame.init()

scrx, scry = 720, 480
# scrx, scry = 1080, 720
center = (scrx/2,scry/2)


pygame.display.set_caption('Deduction (working title)')
window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()

guess_window = pygame.Surface((360, 240))

text = pygame.font.SysFont('comic_sans',20)
button = pygame.font.SysFont('comic_sans',36)

cursor = pygame.image.load(os.path.join('assets', 'cursor.png'))

''' game stuff '''
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
        grid_2.genGrid(fake_rule)


    print(f'Secret Rule: {secret_rule}')
    print()
    print(grid_1)
    print()
    print(grid_2)

    
newGame()



# defaults
inp = [0,0]     # input cursor
clr = 0         # color of piece in hand
shp = 0         # shape of piece in hand
cooldown = 10   # mouse click cooldown
guess_amt = 0   # guess for the amount
verifies = 0    # number if correct verifies
correct_verifies = 0    # verify pass
wins = 0    # number of wins
draw_guess = False      # guessing screen status

''' testing stuff '''



while True:
    if not draw_guess:
        hand = Shape(attributes['color'][clr % 3], attributes['shape'][shp % 2])


    ''' rendering '''
    window.fill(('gray'))
    
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
    guess_button = pygame.Rect((64, scry - (scry/4)-32), (64+32, 64))
    if correct_verifies < 1:
        button_status = 'dark gray'
    else: 
        button_status = 'dark green'
    pygame.draw.rect(window, button_status, guess_button)

    window.blit(text.render(f'number of verifies: {verifies}', 0, 'black'), (scrx-128-64-16, scry - (scry/4)-64))
    window.blit(text.render(f'wins: {wins}', 0, 'black'),(scrx-128-16, scry - (scry/4)-64-32))

    

    ''' logic '''
    if not draw_guess:
        player.playerUpdate(window, inp)


    # for the guessing mechanic
    if draw_guess and correct_verifies > 0:
        guess_num = -inp[1] % 4
        guess_shape = Shape(attributes['color'][clr % 3], attributes['shape'][shp % 2])

        guess_window.fill('black')
        pygame.draw.rect(guess_window, 'dark gray', ((16,16), (360-32, 240-32)))

        guess_window.blit(text.render('Amount', 0, 'black'), (64,32))
        guess_window.blit(text.render('Shape and Color', 0, 'black'), (128+32,32))


        guess_window.blit(text.render(f'{guess_num}', 0, 'black'), (64+16,64+16))
        guess_shape.render(guess_window, (128+16+32,64+16))
        

        guess = [guess_num, attributes['color'][clr % 3], attributes['shape'][shp % 2]]
        # print(guess, secret_rule)


        window.blit(guess_window, (scrx/4, scry/4))
           

    cooldown -= 1

    

    ''' event handling '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and cooldown <= 0:
                if guess_button.collidepoint((pygame.mouse.get_pos())) and not draw_guess and correct_verifies > 0:
                    draw_guess = True
                else:
                    draw_guess = False

            cooldown = 10

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
                player.place(hand.color, hand.type)
            if event.key == pygame.K_j:
                clr += 1
            if event.key == pygame.K_k:
                shp += 1
            if event.key == pygame.K_RETURN:
                if not draw_guess:
                    verifies += 1
                    if player.checkGrid(secret_rule):
                        correct_verifies += 1
                
                if draw_guess:
                    if guess == secret_rule:
                        wins += 1
                        verifies = 0
                        newGame()
                    
                    correct_verifies -= 1
                    draw_guess = False
                
                
            if event.key == pygame.K_BACKSPACE:
                player.clear()

            if event.key == pygame.K_TAB:
                if not draw_guess and correct_verifies > 0:
                    draw_guess = True
                else:
                    draw_guess = False

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
    
