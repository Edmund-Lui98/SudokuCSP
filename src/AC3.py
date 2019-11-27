"""
-------------------------------------------------------
AC3 algorithm implementation
-------------------------------------------------------
Section: CP468
-------------------------------------------------------
"""
from Queue_array import Queue

def ac3(sudoku):
    #initialize queue
    q = Queue()
    
    #add all constraints to the queue
    for i in sudoku.constraints:
        q.insert(i)    
    
    #go through all the constraints
    while q.is_empty() != True:
        #print("Length of queue: " + str(q.length))
        
        xi, xj = q.remove()

        if revise(sudoku, xi, xj):

            if len(sudoku.domains[xi]) == 0:
                return False
            
            for xk in sudoku.neighbors[xi]:
                if xk != xi:
                    q.insert([xk, xi])

    return True
    
def revise(sudoku, xi, xj):

    revised = False

    for x in sudoku.domains[xi]:
        if not any([sudoku.constraint(x, y) for y in sudoku.domains[xj]]):
            sudoku.domains[xi].remove(x)
            revised = True

    return revised