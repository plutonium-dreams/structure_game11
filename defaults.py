'''
Defaults module

Overview: This module compiles all of the default variables required by many of the python scripts. Essentially, this acts as a "bank" for variables that have no dependency and are required by several modules. This also serves to declutter the main module.

Dependencies: None
'''
scrx, scry = 720, 480           # window size
center = (scrx/2,scry/2)        # calculated center of the screen

name = 'KNB'                    # default name (must be a three letters only)
inp = [0,0,0,0]               # input cursor
# inp format: inp = [player grid cursor x, player grid cursor y / amount, piece color, piece shape]

correct_verifies = False        # verify pass
wins = 0                        # number of wins

draw_guess = False              # guessing screen status
paused = False                  # pause screen status