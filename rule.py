'''
Secret Rule module

'''
import pygame, random

# attributes
attributes = {
    'quantity': [0,1,2,3],
    'color': ['red','yellow','blue'],
    'shape': ['square','triangle'],
}

# interactions

def grounded():
    pass

def touching():
    pass

def generateSecretRule():
    global attributes
    secret_rule = []

    for i in attributes:
        attr = attributes[i][random.randint(0,len(attributes[i])-1)]
        secret_rule.append(attr)

    return secret_rule


# test code
# print(generateSecretRule())