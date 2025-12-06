'''
Secret Rule Module

Overview: The purpose of this module is for all the code relating to the secret rule, including its generation, to be in one place. This isolation allows for easy modification by the user in case they wish to change the parameters for the secret rule.
This module contains the attributes dictionary and the generateSecretRule function.

Dependencies: random

'''
import random


'''
    Attributes Dictionary
    Description: Container of all possible quantities, colors, and shapes that can be used to build up the secret rule. 
    One can utilize the dictionary to create a custom secret ruleset for their game.
'''
attributes = {
    'quantity': [1,2,3],
    'color': ['red','yellow','blue'],
    'shape': ['square','triangle'],
}


def generateSecretRule():
    '''
    Generate Secret Rule Function
    Description: Iterates through attributes dictionary and appends a random value from the indexed element in attributes to secret_rule
    '''
    secret_rule = [attributes[i][random.randint(0,len(attributes[i])-1)] for i in attributes]
    return secret_rule      # secret rule format [quantity, color, shape]
