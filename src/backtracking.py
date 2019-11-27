"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Edmund Lui
ID:      160635540
Email:   luix5540@mylaurier.ca
Section: CP164
__updated__ = "2018-08-"
-------------------------------------------------------
"""
#main solve function
def backtrack_solve(board):
    #find first slot that has a 0
    find = find_empty(board)
    
    if not find:
        return True
    else:
        row, col = find
    
    #put the numbers in the slots and check if it is valid
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            
            if backtrack_solve(board):
                return True, board
            
            #backtrack and set it to 0
            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True
                
#function to find first empty slot
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

#print sudoku board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("--------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")