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


def find_empty(bo):
    """
    Finds an empty space in the board
    bo is a 2d list of ints
    returns (row, col)
    """
    for i in range(0, len(bo)):
        for j in range(0, len(bo)):
            if(bo[i][j] == 0):
                return (i, j)
    return None


def safe_write(bo, pos, num):
    """
    Checks if it's safe to write num in pos
    returns bool
    """
    # Check row
    for j in range(0, len(bo)):
        if (bo[pos[0]][j] == num):
            return False
    # Check column
    for i in range(0, len(bo)):
        if (bo[i][pos[1]] == num):
            return False
    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if (bo[i][j] == num) and (i, j) != pos:
                return False
    return True


def solve(bo):
    """
    Tries to solve the sudoku board
    """
    # pos is a pair of coordinates for a place in the board
    # where no number has been placed yet.
    # When there's no empty place left it becomes the pair (-1,-1)
    pos = find_empty(bo)

    # (-1,-1) is the final solution state
    if pos:
        row, col = pos
    else:
        return True

    # Check the numbers from 1 to 9
    for num in range(1, 10):

        # If it's safe to put some number
        if safe_write(bo, pos, num):
            # try to assign it
            bo[row][col] = num
        if solve(bo):
            return True
        # We are coming back from the recursion
        # And the changes must be undone to try again
        bo[row][col] = 0

    # This triggers the recursion coming back from itself
    return False


def print_board(bo):
    """
        #Prints the board so i can debug and show onscreen
        #bo is a 2d list of ints
        #return none, just print
        # Simple print
        for i in range(0, len(bo)):
            print(bo[i], "\n")
        # @todo print should be pretty and separated like a sudoku in 3x3 squares
    """
    for i in range(0, len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(0, len(bo[0])):
            if j % 3 == 0:
                print("|",end="")
            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


# Main function for testing
if __name__ == '__main__':
    print("The initialized board: ", end="\n")
    board = [
      [0,0,0,0,0,0,6,3,0],
      [7,0,0,0,0,6,5,0,9],
      [0,8,0,0,2,0,0,0,0],
      [4,0,0,1,9,8,0,0,6],
      [0,0,9,7,0,2,8,0,0],
      [0,0,0,6,4,3,0,0,0],
      [6,4,0,0,1,0,0,0,0],
      [9,0,0,8,0,0,2,0,0],
      [0,7,0,0,0,0,0,4,0]
    ]
    # By Fran
    print_board(board)

#    print("The Solution: \n")
#    if safe_write(board, (4,4), 5):
#        print("5 is safe in the middle")
#    else:
#        print("I don't know what's wrong, it IS SAFE!")
#    if safe_write(board, (4,4), 6):
#        print("6 is safe in the middle??!!")
#    else:
#        print("It works fine recognizing 6 is not safe in the middle")

    if(solve(board)):
        print_board(board)
    else:
        print ("There's no solution for this board!")
