# This will be a backtracking experiment
# I have to implement an algorith to solve a sudoku grid

# I should list the methods I'm gonna need:
# @todo Print the board, so i can see what's happening          *
# @todo Some way of looking for the empty spaces in the matrix  *
# @todo check if a number is valid in a certain position        *
# @todo the solving backtracking mad procedure                  *

def solve(bo):
    """
    Tries to solve the sudoku board
    """
    # pos is a pair of coordinates for a place in the board
    # where no number has been placed yet.

    pos = find_empty(bo)
    # pos empty is the final solution state
    if pos:
        row, col = pos
    else:
        return True

    # Check the numbers from 1 to 9
    for num in range(1, 10):

        # If it's safe to put some number
        if safe_write(bo, (row, col), num):
            # try to assign it
            bo[row][col] = num
            """
            ESTA ES LA LECCIÓN MÁS IMPORTANTE
            Fran, si al siguiente if le sacás una tabulación
            te quedás en un bucle infinito.
            Python es sensible a la indentación y te
            llevó una hora notarlo...
            Lección for evah
            """
            print_board(bo)
            input()
            if solve(bo):
                return True
        # We are coming back from the recursion
        # And the changes must be undone to try again
        bo[row][col] = 0

    # This triggers the recursion coming back from itself
    return False


def find_empty(bo):
    """
    Finds an empty space in the board
    bo is a 2d list of ints
    returns (row, col)
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def safe_write(bo, pos, num):
    """
    Checks if it's safe to write num in pos
    returns bool
    """
    # Check row
    for i in range(0, len(bo)):
        # (pos[0], [i]) must clearly be different from (pos[0], pos[1])
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(0, len(bo)):
        # ([i], pos[1]) must clearly be different from (pos[0], pos[1])
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    """
        #Prints the board so i can debug and show onscreen
        #bo is a 2d list of ints
        #return none, just print
        # Simple print
        for i in range(0, len(bo)):
            print(bo[i], "\n")
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
    print(end="\n")


# Main function for testing
if __name__ == '__main__':
    print("The initialized board: ", end="\n")
    board = [
      [0,0,0,5,0,0,6,3,0],
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

    print("The Solution: \n")
    if solve(board):
        print_board(board)
    else:
        print("There's no solution for this board!")
