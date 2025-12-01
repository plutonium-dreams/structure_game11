'''
Defaults module
to compile all the default stuff into one file
'''
scrx, scry = 720, 480
# scrx, scry = 1080, 720
center = (scrx/2,scry/2)

name = 'KNB'
highscores = []

inp = [0,0,0,0,0]     # input cursor
verifies = 0    # number if correct verifies
correct_verifies = False    # verify pass
wins = 0    # number of wins
draw_guess = False      # guessing screen status
paused = False