# PROJECT - SUDOKU SOLVER

I chose to use user input for the creation of the puzzle as a 2D array in the form of a grid, using the numpy library import for representing the puzzles as matrices for readability.  I wrote three functions, errorHandling(), for testing the user input for incorrect length, or value errors, possible(), for testing possible numbers to insert in the row and columns, and solve(), for solving and printing the completed puzzle with the correct numbers. 

I first wrote the program having the user write into the code as a 2D array the unsolved puzzle, but after further reading on the subject, I wanted the user to input the given numbers and blanks(represented by zeroes) directly on the terminal and not manipulating the code.  I needed to use a 2D array to represent the grid containing rows and columns that are within the puzzle.  I chose to create functions to run the tests on the grid, since the puzzle required not only checking for possible numbers, but also for input errors, as well as a solve option that would print out the final puzzle.  They contained for-loops, if statements, and the grid as a global variable to be used in the throughout the functions.  I also chose to use the numpy library, since it creates readable matrices for multi-dimensional arrays, and I thought it would make the output look more like the true sudoku puzzle.  

* sample run: </br>
<img width="700" alt="Screen Shot 2022-05-19 at 2 21 53 PM" src="https://user-images.githubusercontent.com/87743069/169372716-76239f91-d44e-4712-9291-f490adc80ab7.png">

# INSTRUCTIONS

* Execute python file (sudoku.py) in terminal by navigating to the directory where the file is found i.e.(cd Desktop).
* Type --> python3 sudoku.py <-- in terminal to execute the script. <PROGRAM MUST COMPILE FROM PYTHON 3 VERSION>
* Complete the input following the directions.

* main method: [sudoku.py](sudoku.py)
