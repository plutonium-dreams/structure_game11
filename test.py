'''
TEST
'''
cell = 1

grid = [
        [0], [1], [2],
        [3], [4], [5],
        [6], [7], [8]
    ]

neighbors = {
    'north': grid[cell-3], 
    'south': grid[cell+3], 
    'west': grid[cell-1], 
    'east': grid[cell+1]
}

print(('north', [7]) in neighbors.items())