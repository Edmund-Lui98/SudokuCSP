"""
-------------------------------------------------------
Main program
-------------------------------------------------------
Section: CP468
-------------------------------------------------------
"""
from AC3 import ac3
from sudoku import sudoku
from backtracking import print_board

#helper functions

#changes a board to string
def board_to_string(b):
    s = ""
    for i in b:
        for j in i:
            s += str(j)
            
    return s

#changes a string to board
def string_to_board(s):
    board = []
    
    i = 0
    for _ in range(9):
        x = []
        for _ in range(9):
            x.append(int(s[i]))
            i += 1
        board.append(x)
    return board
               
#main function 
def main():
    #open file
    fv = open("input.txt","r")
    
    #keep track of sudoku number being solved
    i = 1
    
    #iterate through file for each line
    for x in fv:
        print("Sudoku #" + str(i))
        i +=1
        
        #check if sudoku is valid
        if len(x) >= 82 and len(x[:-1]) == 81:
            board = x[:81]
            print_board(string_to_board(board))
            s = sudoku(board)
            
            solved = ac3(s) #use the ac3 algorithm
            
#             print(s.variables)
#             print(s.domains)
#             print(s.constraints)
#             print(s.neighbors)

            #if solved by ac3, print board
            if solved and s.solved():
                string_board = ""
                for var in s.variables:
                    string_board += str(s.domains[var][0])
                print("Solved using AC3!")
                print_board(string_to_board(string_board))
            else:
                string_board = ""
                for var in s.variables:
                    if len(s.domains[var]) == 1:
                        string_board += str(s.domains[var][0])
                    else:
                        print(var, end=" ")
                        print(s.domains[var])
                #print("using AC3")
                #print_board(string_to_board(string_board))
            """
            else: #if not solved by ac3, use backtracking
                print("Not solved by AC3. Now using backtracking algorithm...", end = " ")
                if backtrack_solve(board):
                    print("Solved using backtracking!")
                    print_board(board)
                    
                else:
                    print("Not solvable")
            """

        else:
            print("Sudoku is invalid")

main()