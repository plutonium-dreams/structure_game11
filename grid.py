'''
Grid module

Overview: This module is for the game's grids. As a major subject of the program, it is treated seperately. The grid and player grid classes are present here for ease of access in the modification of one of the game's essential components.

Dependencies: rule, shape

'''

from rule import *
from shape import *

class Grid:
    '''
    Grid class
    Description: The grid class provides a template for all of the grids used inside the program. It contains class methods for grid modification, rendering, checking, generation, and even debugging.

    '''
    def __init__(self, pos):
        '''
        Initializes the grid class
        Description: Creates a 9 - item list of lists that will act as the 3x3 grid for the grid class instance. Furthermore, the grid's center is computed based on the position specified
        '''
        # grid element format: ['color', 'shape']
        self.grid = [
            [], [], [],
            [], [], [],
            [], [], []
            ]
        self.pos = pos
        self.center = (pos[0] - 192/2, pos[1] - 192/2)

    def __str__(self):
        '''
        String Method
        Description: This is a python special method that we leverage to have the print statement output the grid and its elements in text form on the terminal. This is very useful for debugging purposes
        '''
        for i in range(len(self.grid)):
            print(self.grid[i], end='')
            if (i+1) % 3 == 0:
                print()

        return ''


    def render(self, surf):
        '''
        Render Method
        Description: This method renders the grid unto the surface specified
        '''
        cell = 0
        for i in range(3):
            for j in range(3):
                if self.grid[cell] != []:
                    # for each cell in the grid, create a shape instance based on the information extracted (if the cell is not empty)
                    shape = Shape(self.grid[cell][0], self.grid[cell][1])
                    # use the shape instance's render function to render it unto the surface specified
                    shape.render(surf, (self.center[0] + (shape.image.width * j), self.center[1] + (shape.image.height * i)))
                    # position of the shape render depends on the loop variables i and j

                cell += 1

    def update(self, cell, item):
        '''
        Update Method
        Description: Updates a cell on the grid with the specified item
        '''
        # item format: ['color', 'shape']
        if self.grid[cell] == []:
            self.grid[cell] = item
            return 1
        else:
            # print('\nAn item already exists in the cell!\n')  # for debugging
            return 0

    def swap(self, cell_1, cell_2):
        '''
        Swap Method
        Description: Used for swapping the contents of one cell with another
        '''
        self.grid[cell_1], self.grid[cell_2] = self.grid[cell_2], self.grid[cell_1]

    def clear(self):
        '''
        Clear Method
        Description: Empties the grid instance's grid
        '''
        self.grid = [
        [], [], [],
        [], [], [],
        [], [], []
        ]


    def checkGrid(self, srule):
        '''
        Check Grid Method
        Description: Checks the grid instance if it follows the secret rule specified.
        '''
        # secret rule format
        # [qty, color, shape]
        qty = 0
        for cell in self.grid:
            # for each cell in the grid, we check if that piece in the cell follows the color and size of the shape specified in the secret rule. if so, we add 1 to the counter
            try:
                if cell[0] == srule[1] and cell[1] == srule[2]:
                    qty += 1
            except IndexError:
                # for handling the case of an empty cell
                pass
                
        # if the number of pieces that follow the secret rule is the same as the quantity specified in the secret rule, we return 1 to signify that the grid is valid
        if qty == srule[0]:
            return 1

        # otherwise, we return 0 to signify that the grid is invalid
        return 0

    def genGrid(self, srule):
        '''
        Generate Grid Method
        Overview: Generates the grid instance's grid.
        '''
        self.clear()

        # for 9 times, we update a random cell on the grid with the a randomly generated item of the form ['color', 'attribute']
        for i in range(len(self.grid)):
            shp = random.randint(0,1)

            self.update(random.randint(0,8), [attributes['color'][random.randint(0,2)], attributes['shape'][shp]])
                
            # grid element
            # ['color', 'shape']

        # checks if the newly formed grid follows the secret rule
        if self.checkGrid(srule):
            # signifies a succesful generation
            return 1
        else:
            # recursively calls the function if it does not follow the secret rule
            return self.genGrid(srule)



class PlayerGrid(Grid):
    '''
    Player Grid Class
    Description: For the player's modifiable grid. Inherits the methods from the Grid class.
    '''
    def __init__(self, pos):
        '''
        Initializes the player grid instance
        Description: In additon to initializing the methods and class attributes from the grid class, the player's cursor as well as cursor position are intialized here.
        '''
        super().__init__(pos)
        self.cursor = pygame.image.load(os.path.join('assets', 'images', 'cursor.png'))
        self.curs_pos = [0,0]       # pos is of the format [cursor x, cursor y]
        self.cell_pos = 0 

    def place(self, color, tipe):
        '''
        Place Method
        Description: Unique to the player grid. Provides the player the functionality to place down a piece with a specified color and type
        '''
        if self.grid[self.cell_pos] == [color, tipe]:
            self.grid[self.cell_pos] = []       # empties the grid if the same color and shape type is being placed
        else:
            self.grid[self.cell_pos] = [color, tipe]

    def playerUpdate(self, surf, inp):
        '''
        Update Method
        Description: Updates the player grid instance's cursor position. In addition, it also renders the player's cursor based on its pos. 
        '''
        # inp = [cursor x, cursor y]
        inp = [inp[0] % 3, inp[1] % 3]
        self.curs_pos = inp
        # cell position is determined based on cursor position
        self.cell_pos = (self.curs_pos[0]) + (self.curs_pos[1] * 3) 

        # draws the cursor on the specified surface based on the position calculated
        surf.blit(self.cursor, (self.center[0] + (64 * self.curs_pos[0]), self.center[1] + (64 * self.curs_pos[1])))