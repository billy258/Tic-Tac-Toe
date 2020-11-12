#this is a game of tic tac toe
# To win the player must get a 3 in a row vertically, horonzontally and 
# diagonally. 
from random import randint
grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
def empty_grid (grid):
    for row in grid:
        for cell in row:
            if cell != 0:
                continue
            else: return True
    return False 

def rows (grid,row,col):
    first = grid[row][col]
    for j in grid[row]:
        if j != first or j == 0:
            return False
    return True
    
def columns (grid, row, col):
    first = grid[row][col]
    for w in [grid[0][col], grid[1][col], grid[2][col]]:
        if w != first or w == 0:
            return False
    return True

def diagonal_left (grid, row, col):
    first = grid[row][col]
    for q in [grid[0][0], grid[1][1], grid[2][2]]:
        if q != first or q == 0:
            return False
    return True

def diagonal_right (grid, row, col):
    first = grid[row][col]
    for w in [grid[0][2], grid[1][1], grid[2][0]]:
       if w != first or w == 0:
            return False
    return True

while empty_grid(grid):
    
    player1 = input('where on the grid would you like to go?\n')
    if player1 == 'quit':break

    valid = False
    win = False
    
    try:
        iplayer1 = int(player1)
        if iplayer1 < 0 or iplayer1 > 9: 
            raise Exception
    except:
        valid = True
 
    for i in range(9):
        row = i // 3
        col = i % 3
        selection = iplayer1 - 1
        if i == selection and grid[row][col] == 0:
            grid[row][col] = 'X'
            if rows (grid, row, col) == True:
                win = True
                win_player = grid[row][col]
                break
            if columns (grid, row, col):
                win = True
                win_player = grid[row][col]
                break
            if diagonal_left (grid, row, col):
                win = True
                win_player = grid[row][col]
                break
            if diagonal_right (grid, row, col):
                win = True
                win_player = grid[row][col]
                break
            break
        if i == selection and grid[row][col] != 0:
            valid = True
            break

    #Player 2 makes a random move if player one has played
    while empty_grid(grid):
        if valid is True:
            break
        rrow = randint(0,2)
        rcol = randint(0,2)
        if grid[rrow][rcol] == 0:
            grid[rrow][rcol] = 'O'
            break

    print('\n')
    for r in grid:
        print(*r)
        print('-----')
    print('\n')
    if valid == True:
        print('Not a valid move.')
    if win == True:
        print(win_player+' has won')
        break
        