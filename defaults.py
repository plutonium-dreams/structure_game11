'''
Defaults module
to compile all the default stuff into one file
'''
scrx, scry = 720, 480
# scrx, scry = 1080, 720
center = (scrx/2,scry/2)

name = 'KNB'
highscore = []

inp = [0,0,0,0,0]     # input cursor
correct_verifies = False    # verify pass
wins = 0    # number of wins
draw_guess = False      # guessing screen status
paused = False          # pause screen status