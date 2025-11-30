'''
Grid module
'''

from rule import *
from shape import *

class Grid:
    def __init__(self, pos):
        self.grid = [
            [], [], [],
            [], [], [],
            [], [], []
            ]
        self.pos = pos
        self.center = (pos[0] - 192/2, pos[1] - 192/2)

    def __str__(self):
        for i in range(len(self.grid)):
            print(self.grid[i], end='')
            if (i+1) % 3 == 0:
                print()

        return ''


    def render(self, surf):            # can be optimized more
        cell = 0
        for i in range(3):
            for j in range(3):
                if self.grid[cell] != []:
                    shape = Shape(self.grid[cell][0], self.grid[cell][1])
                    shape.render(surf, (self.center[0] + (shape.image.width * j), self.center[1] + (shape.image.height * i)))

                cell += 1

    def update(self, cell, item):    
        if self.grid[cell] == []:
            self.grid[cell] = item
            return 1
        else:
            # print('\nAn item already exists in the cell!\n')
            return 0

    def swap(self, cell_1, cell_2):
        self.grid[cell_1], self.grid[cell_2] = self.grid[cell_2], self.grid[cell_1]

    def clear(self):
            self.grid = [
            [], [], [],
            [], [], [],
            [], [], []
            ]


    def checkGrid(self, srule):
        # secret rule format
        # [qty, color, shape]
        qty = 0
        for cell in self.grid:
            try:
                if cell[0] == srule[1] and cell[1] == srule[2]:
                    qty += 1
            except IndexError:
                pass

        if qty == srule[0]:
            return 1

        return 0

    def genGrid(self, srule):
        self.clear()
        snum = [0, 0]

        for i in range(len(self.grid)):
            shp = random.randint(0,1)
            if snum[shp] > 2:           
                continue

            if self.update(random.randint(0,8), [attributes['color'][random.randint(0,2)], attributes['shape'][shp]]):
                snum[shp] += 1
                
                # grid element
                # ['color', 'shape']

        if self.checkGrid(srule):
            return 1
        else:
            self.clear()
            return self.genGrid(srule)



class PlayerGrid(Grid):
    def __init__(self, pos):
        super().__init__(pos)
        self.cursor = pygame.image.load(os.path.join('assets', 'images', 'cursor.png'))
        self.curs_pos = [0,0]
        self.cell_pos = 0 

    def place(self, color, tipe):
        if self.grid[self.cell_pos] == [color, tipe]:
            self.grid[self.cell_pos] = []
        else:
            self.grid[self.cell_pos] = [color, tipe]

    def playerUpdate(self, surf, inp):
        # checks if the player moved or placed a piece; or verified a grid
        inp = [inp[0] % 3, inp[1] % 3]
        self.curs_pos = inp
        self.cell_pos = (self.curs_pos[0]) + (self.curs_pos[1] * 3) 

        surf.blit(self.cursor, (self.center[0] + (64 * self.curs_pos[0]), self.center[1] + (64 * self.curs_pos[1])))


# grid_1 = Grid((400,400)).genGrid(generateSecretRule())