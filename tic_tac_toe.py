#this is a game of tic tac toe
# To win the player must get a 3 in a row vertically, horonzontally and 
# diagonally. 

def empty_grid (grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    return True


grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

while True:
    for i in range(9):
        if 