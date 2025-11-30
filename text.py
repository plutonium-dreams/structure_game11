'''
text feature testing
'''
import os

file = open(os.path.join('data', 'quaso.txt'), 'r')

print(file.read())

file.close()

with open(os.path.join('data', 'quaso.txt'), 'a') as file:
    file.write('\nadding more')

file = open(os.path.join('data', 'quaso.txt'), 'r')
print(file.read())
file.close()

with open(os.path.join('data', 'quaso.txt'), 'w') as file:
    file.write('deletion')


