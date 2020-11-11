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


while True:
    
    if empty_grid(grid) == False :break
    player1 = input('where on the grid would you like to go?\n')
    if player1 == 'quit':break
    valid = False
    
    try:
        iplayer1 = int(player1)
    except:
        print('Please enter a number between 1 and 9')

    for i in range(9):
        row = i // 3
        col = i % 3
        selection = iplayer1 - 1
        if i == selection and grid[row][col] == 0:
            grid[row][col] = 'X'
            break
        if i == selection and grid[row][col] != 0:
            valid = True
            break
        

    for r in grid:
        print(*r)
        print('-----')
    if valid == True:
        print('Not a valid move.')

    
        

    
    
