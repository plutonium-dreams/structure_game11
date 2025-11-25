'''
secret rules

# you are currently working on implementing this one


secret rule format: 
sru =  <exacty/atleast> <quantity> <color/s> <orientation> <shape>
rule = sru <interaction> sru

a koan can be a rule by iself
'''

'''
to do:
- make a secret rule generator
    - for each attribute, make a collection of all of their possibilities
    - randomly pull an item from each attribute collection and put it in the secret rule list
    - print out the secret rule list

# can turn this whole thing into a class
'''

import pygame, random
from shapes import *


# important collections

attributes = {
    'shape': ['rectangle','triangle'],
    'color': ['red', 'blue','yellow'],
    'orientation': ['up', 'down', 'left', 'right'],
    'quantity': [0,1,2,3],
}

# interactions
def adjacent(shape_1, shape_2):
    pass

# def grounded(shape):
#     pass

def pointing(shape):
    pass

# def on_top(shape_above, shape_below):
#     pass

interactions = ['adjacent', 'pointing']


# secret rule generator
def generateSecretRule():
    global attributes, interactions
    rule1 = list()
    rule2 = list()
    
    secret_rule = [rule1, rule2]        # can be turned into a dictionary 
    
    for i in range(random.randint(1,2)):
        for j in attributes:
            attr = attributes[j][random.randint(0,len(attributes[j])-1)]
            secret_rule[i].append(attr)
                
    
    if secret_rule[1]:
        secret_rule.append(interactions[random.randint(0,len(interactions)-1)])

    return secret_rule
