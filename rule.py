'''
Secret Rule module
Description: 

'''
import pygame, random

# dictionary containing all the possible quantities, colors, and shapes that can make the secret rule
attributes = {
    'quantity': [1,2,3],
    'color': ['red','yellow','blue'],
    'shape': ['square','triangle'],
}

# creates the secret rule stored in the secret_rule list
# secret rule format [quantity, color, shape]
def generateSecretRule():
    # iterates through attributes dictionary and appends a random value from the indexed element in attributes to secret_rule
    secret_rule = [attributes[i][random.randint(0,len(attributes[i])-1)] for i in attributes]
    return secret_rule
