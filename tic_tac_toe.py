#this is a game of tic tac toe
# To win the player must get a 3 in a row vertically, horonzontally and 
# diagonally. 

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

def row_checker (grid,row,col):
    first = grid[row][col]
    for j in grid[row]:
        if j != first or j == 0:
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
            if row_checker(grid,row,col) == True:
                win = True
                win_player = grid[row][0]
                break
            break
        if i == selection and grid[row][col] != 0:
            valid = True
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
        


    
        

    
    
