# This will be a backtracking experiment
# I have to implement an algorith to solve a sudoku grid

# @fixme something's broken
# @question are crabs inmortal?
# @idea how about some soup?

# I should list the methods I'm gonna need:
# @todo Print the board, so i can see what's happening          *
# @todo Some way of looking for the empty spaces in the matrix  *
# @todo check if a number is valid in a certain position
# @todo

def print_board(bo):
    """
    Prints the board so i can debug and show onscreen
    bo is a 2d list of ints
    return none, just print
    """
    # Simple print
    for i in range(len(bo)):
        print(bo[i], "\n")
    # @todo print should be pretty and separated like a sudoku in 3x3 squares

def check_blank(bo, i, j):
    """
    Check if a given space is 0 
    bo is a 2d list of ints
    i, j a pair of coordinates
    returns a bool
    """
    if bo[i][j] == 0:
        return True
    return False

def write_number(bo, i, j, num):
    """
    Tries to write num in in a blank space
    The number is writable if it's not already present
    in the row, column, or box where it's gonna be placed
    bo is a 2d list of ints
    i,j is a pair of coordinates of bo
    num is an int
    returns none
    """
    # Check if it's a blank space
    if not (check_blank(bo, i, j)):
        return None

    # Check row
    for x in range(len(bo)):
        if bo[i][j] == bo[i][x]:
            return None

    # Check column
    # @todo check column and box on write_number

    # Check box

board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]
# By Fran
print_board(board)
