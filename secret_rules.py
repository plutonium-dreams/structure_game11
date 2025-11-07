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
'''

import pygame, random
from shapes import *
from grid import *


secret_rule = []    # secret rule is a string (list will be turned into a string later)

# attributes
quantity = [0,1,2,3, 'any']
color = ['red', 'blue', 'yellow', 'any']
orientation = ['up', 'down', 'left', 'right', 'any']
shape = ['rectangle','triangle', 'any']

attributes = [quantity, color, orientation, shape]

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
def srule_gen(amt):
    global attributes, interactions
    rule1 = list()
    rule2 = list()
    ineract = None
    
    secret_rule = [rule1, rule2, ineract]
    
    for num in range(amt):
        for i in range(2):
            for j in range(len(attributes)):
                # gaka list index out of range; collections of attribute possibilitoies dont have the same length
                attr = attributes[j][random.randint(0,len(attributes)-1)]
                secret_rule[i].append(attr)
            # fix interactions to only have 1 string allowed at secret_rule[2]
            
        ineract = interactions[1]

    print(secret_rule)


srule_gen(1)





