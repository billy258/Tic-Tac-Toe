#this is a game of tic tac toe
# To win the player must get a 3 in a row vertically, horonzontally and 
# diagonally. 

def empty_grid (grid):
    for row in grid:
        for cell in row:
            if cell != 0:
                continue
            else: return True
    return False 

    


grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

while True:

    player1 = input('where on the grid would you like to go?\n')
    
    if empty_grid(grid) == False :break
    
    if player1 == '1' : grid[0][0] = 'x'
    elif player1 == '2' : grid[0][1] = 'x'
    elif player1 == '3' : grid[0][2] = 'x'
    elif player1 == '4' : grid[1][0] = 'x'
    elif player1 == '5' : grid[1][1] = 'x'
    elif player1 == '6' : grid[1][2] = 'x'
    elif player1 == '7' : grid[2][0] = 'x'
    elif player1 == '8' : grid[2][1] = 'x'
    elif player1 == '9' : grid[2][2] = 'x'

    else: print('enter a valid grid value')

    print(grid)