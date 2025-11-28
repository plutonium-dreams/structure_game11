'''
testing codes

'''
# for testing a grid
grid = Grid((100,100))
colors = ["red", "yellow", "blue", "green", "orange", "purple", "brown", "pink", "sky blue"]
orientations = ["up","down","left","right"] * 3
rects = []
tris = []

for i in range(3):
    tris.append(Triangle(colors[i], orientations[i]))
    grid.update(i, tris[i].triItem())

for i in range(3,9):
    tris.append(Triangle(colors[i], orientations[i]))
    grid.update(i, tris[i-3].triItem())

for i in range(3):
    rects.append(Rectangle(colors[i]))
    grid.update(i, rects[i].rectItem())

for i in range(3,9):
    print(colors[i], i)
    rects.append(Rectangle(colors[i]))
    grid.update(i, rects[i-3].rectItem())

