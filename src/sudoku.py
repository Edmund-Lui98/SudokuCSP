"""
-------------------------------------------------------
Sudoku class
-------------------------------------------------------
Section: CP468
-------------------------------------------------------
"""
import itertools

rows = characters = "ABCDEFGHI"
cols = numbers = "123456789"

class sudoku:
    
    def __init__(self, board):
        self.variables = list()
        self.domains = dict()
        self.constraints = list()
        self.neighbors = dict()
        
        self.prepare(board)
        
    def prepare(self,board):
        game = list(board)
        
        self.variables = self.def_variables(rows,cols)
        self.domains = {v: list(range(1, 10)) if game[i] == '0' else [int(game[i])] for i, v in enumerate(self.variables)}
        self.def_constraints()
        self.def_neighors()
        
    
    def def_variables(self,a,b):
        var = []
        for x in a:
            for i in b:
                var.append(x+i)
        return var
        
    def def_constraints(self):
        
        blocks = (
            [self.combine(rows, number) for number in cols] +
            [self.combine(character, cols) for character in rows] +
            [self.combine(character, number) for character in ('ABC', 'DEF', 'GHI') for number in ('123', '456', '789')]
        )

        for block in blocks:
            combinations = self.permutate(block)
            for combination in combinations:
                if [combination[0], combination[1]] not in self.constraints:
                    self.constraints.append([combination[0], combination[1]])
    
    def def_neighors(self):
        
        for x in self.variables:
            self.neighbors[x] = list()
            for c in self.constraints:
                if x == c[0]:
                    self.neighbors[x].append(c[1])
                    
    def solved(self):
        solved = True
        for i in self.variables:
            if len(self.domains[i]) > 1:
                solved = False
        return solved
    
    
    #helper functions for the constraints
    @staticmethod
    def combine(alpha, beta):
        return [a + b for a in alpha for b in beta]
    @staticmethod
    def permutate(iterable):
        result = list()

        for L in range(0, len(iterable) + 1):
            if L == 2:
                for subset in itertools.permutations(iterable, L):
                    result.append(subset)

        return result
    @staticmethod
    def constraint(xi, xj): 
        return xi != xj
    