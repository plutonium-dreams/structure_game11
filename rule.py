'''
Secret Rule module

'''
import pygame, random
# from grid import *

# attributes
attributes = {
    'quantity': [0,1,2,3],
    'color': ['red','yellow','blue'],
    'shape': ['square','triangle'],
}

# interactions
interactions = ['adjacent', 'grounded', 'pointing']
adjacent_directions = ['north', 'south', 'east', 'west']


def grounded():
    pass

# secret rule format
# [qty, color, shape, interaction type (#), <interaction>]
def generateSecretRule(difficulty):
    global attributes
    secret_rule = []

    for i in attributes:
        attr = attributes[i][random.randint(0,len(attributes[i])-1)]
        secret_rule.append(attr)

    if True:
        # interactions
        interact = difficulty
        if interact >= 1:        
            # adjacent interaction
            # ... 0, (direction, [color, shape])]
            touching = (adjacent_directions[random.randint(0,3)], [attributes['color'][random.randint(0,len(attributes[i])-1)], attributes['shape'][random.randint(0,len(attributes[i])-1)]])
            
            secret_rule.extend([interact, touching])

            return secret_rule
    
    return secret_rule
