'''
shapes file
'''
import pygame

pygame.init()

def tri_orient(orientation, center, size):
    # can be optimized
    # maybe not use the center; use the top left position instead like with the rect?
    # the triangles don't line up perfectly, representation error i guess

    if orientation == 'up':     # only the second component is flipped
        return [(center[0], center[1] - size[1]/2), 
                            (center[0] - size[0]/2, center[1] + size[1]/2), 
                            (center[0] + size[0]/2, center[1] + size[1]/2)]
    elif orientation == 'down':
        return [(center[0], center[1] + size[1]/2),
                            (center[0] - size[0]/2, center[1] - size[1]/2), 
                            (center[0] + size[0]/2, center[1] - size[1]/2)]

    elif orientation == 'right':     # only the first component is flipped
        return [(center[0] + size[0]/2, center[1]), 
                            (center[0] - size[0]/2, center[1] - size[1]/2), 
                            (center[0] - size[0]/2, center[1] + size[1]/2)]
    elif orientation == 'left':     
        return [(center[0] - size[0]/2, center[1]), 
                            (center[0] + size[0]/2, center[1] - size[1]/2), 
                            (center[0] + size[0]/2, center[1] + size[1]/2)]

class Rectangle():
    def __init__(self, color):
        self.pos = (0,0)
        self.center = (0,0)
        self.size = (50,50)
        self.color = color
        self.type = 'rectangle'
        self.orientation = 'any'

        self.rect = pygame.Rect(self.pos, self.size)

    def update(self, pos, color):
        self.pos = (pos[0] - self.size[0] / 2, pos[1] - self.size[1] / 2)
        self.center = pos

    def render(self,surf):
        pygame.draw.rect(surf, self.color, self.rect)
    
    def rectItem(self):
        return [self.type, self.color, self.orientation]


class Triangle():
    def __init__(self, color, orientation):
        self.pos = (0,0)
        self.center = (0,0)
        self.size = (50,50)
        self.color = color
        self.type = 'triangle'
        self.orientation = orientation
        self.points = [(self.center[0], self.center[1] - self.size[1]/2), 
                            (self.center[0] - self.size[0]/2, self.center[1] + self.size[1]/2), 
                            (self.center[0] + self.size[0]/2, self.center[1] + self.size[1]/2)]
        # rects need ((left, top), (width, height)) and color
        # triangles need a tuple list of 3 points and color

    def update(self, pos, color, orientation):
        self.pos = (pos[0] - self.size[0] / 2, pos[1] - self.size[1] / 2)
        self.center = pos
        self.color = color
        self.orientation = orientation

        # can still optimize the orientation code
        self.points = tri_orient(self.orientation, self.center, self.size)

    def render(self,surf):       # will only be used for rendering the shape by itself
        pygame.draw.polygon(surf, self.color, self.points)

    def triItem(self):
        return [self.type, self.color, self.orientation]
        
