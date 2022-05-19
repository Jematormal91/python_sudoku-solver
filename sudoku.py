# SUDOKU
# make a 9x9 grid with numbers 1 thru 9 never repeating every row and column

import numpy as np # add import to print completed grid as matrix

# SAMPLE UNSOLVED SUDOKU PUZZLE AS MATRIX
# grid = [
# [0,0,6,0,0,0,0,0,8],
# [0,0,0,9,0,8,7,0,1],
# [0,7,0,5,4,0,3,0,0],
# [8,9,0,2,5,1,0,3,7],
# [7,6,5,8,0,3,0,4,2],
# [0,0,1,0,0,0,0,9,5],
# [6,0,3,1,8,0,0,0,0],
# [4,8,0,0,0,0,0,0,3],
# [0,0,0,0,0,4,5,0,0]
# ]

# create user input matrix
grid=[]
for i in range(9):
    grid.append([int(j) for j in input("Enter row of NINE numbers, less than or equal to 9, or 0 if a blank, WITH SPACES: ").split()])

# write function to check for errors
def errorHandling():
    for i in range(9):
        if len(grid[i]) != 9:
            print("Error. Invalid entry.")
            for i in range(9):
                grid.append([int(j) for j in input("Enter row of NINE numbers, less than or equal to 9, or 0 if a blank, WITH SPACES: ").split()])

# check for errors in grid
errorHandling()

print("\nUnsolved puzzle:\n")
print(np.matrix(grid))

# write function to check for possible numbers
def possible(row,column,number):
    global grid

# first scan for number in row
    for i in range (0,9):
        if grid[i][column]==number:
            return False
 

# second scan for number in column
    for i in range (0,9):
        if grid[row][i]==number:
            return False


# third scan for number in 3x3 grid box
    x0=(row//3)*3
    y0=(column//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if grid[x0+i][y0+j]==number:
                return False
    
    return True
 
# write function to solve puzzle
def solve():
    global grid
    for row in range (0,9):
        for column in range (0,9):
            if grid[row][column]==0:
                for number in range (1,10):
                    if possible(row,column,number):
                        grid[row][column]=number
                        solve()
                        # if solution still has 0s return back to for-loop
                        grid[row][column]=0
                return

    # print grid as matrix using numpy import
    print("\nSolved puzzle:\n")               
    print(np.matrix(grid))

# solve puzzle
solve()
