from copy import deepcopy
from random import randint


class Sudoku_Board:
    
    def __init__(self):
        self.__board = [
            [0,0,0,0,0,0,0,0,0], # Bottom row
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0] # Top row
        ]

        # Solutions variable key:
        # 0: No solution found
        # 1: One solution found
        # 2: More than one solution found
        self.__solutions = 0

        # This will act as a placholder for the unsolved state of a board
        # when a new board is created. This allows the resetting of the board
        # to default values
        self.__unsolved_state = [
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
        
        # This is experimental. It will contain every state of the board while
        # being solved. This will help with the visualisation of the solve
        self.__steps = []
    


    ### Public methods ###

    def print_board(self):
        print(f'''
        {self.__print_row(self.__board[8])}
        {self.__print_row(self.__board[7])}
        {self.__print_row(self.__board[6])}
        ------+-------+------
        {self.__print_row(self.__board[5])}
        {self.__print_row(self.__board[4])}
        {self.__print_row(self.__board[3])}
        ------+-------+------
        {self.__print_row(self.__board[2])}
        {self.__print_row(self.__board[1])}
        {self.__print_row(self.__board[0])}
        ''')


    def get_board(self):
        return self.__board
    
    def insert_digit(self, x, y, value):
        self.__board[y][x] = value
    

    def checked_insert_digit(self, x, y, value):
        if self.check(x, y, value):
            self.insert_digit(x, y, value)
            return True
        else:
            return False

    
    def get_digit(self, x, y):
        return self.__board[y][x]

    
    def check(self, x, y, value):
        if value == 0:
            self.insert_digit(x, y, value)
            return True

        #Check row
        temp = self.get_digit(x, y)
        self.insert_digit(x, y, 0)

        for i in range(0,9):
            if value == self.get_digit(i, y):
                self.insert_digit(x, y, temp)
                return False

        # Check col
        for i in range(0,9):
            if value == self.get_digit(x, i):
                self.insert_digit(x, y, temp)
                return False

        # Check box
        box_x = (x // 3) * 3
        box_y = (y // 3) * 3
        for i in range(box_y, box_y + 3): # Cycle through rows in box
            for j in range(box_x, box_x + 3): # Cycle through columns in box
                if self.get_digit(j, i) == value:
                    self.insert_digit(x, y, temp)
                    return False
        
        self.insert_digit(x, y, temp)
        return True


    def solve(self):
        self.__solutions = 0
        self.__steps = [] #!TEMP
        self.__temp_board = deepcopy(self.__board)
        self.__recur_solve()
        self.__board = deepcopy(self.__temp_board)

        return self.__solutions
    
    
    def vis_solve(self):
        self.__solutions = 0
        self.__steps = []
        self.__temp_board = deepcopy(self.__board)
        self.__vis_recur_solve()
        self.__board = deepcopy(self.__temp_board)

        return self.__solutions, self.__steps
        

    def is_complete(self):
        # Check if all spaces are filled
        for i in self.__board:
            if 0 in i:
                return False

        # Check if every number that has already been inserted is valid
        for i in range(0, 9):
            for j in range(0, 9):
                value = self.get_digit(j,i)
                if not self.check(j, i, value):
                    return False
        return True


    def new_board(self, blank_values=51):
        self.__board = [[0 for x in range(9)] for y in range(9)]

        seed_cells = [
            [0,0], [3,1], [6,2], [1,3], [4,4], [7,5], [2,6], [5,7], [8,8] # [y,x]
        ]

        # Place random value into seed cells
        for cell in seed_cells:
            x = cell[1]
            y = cell[0]
            self.insert_digit(x, y, randint(1,9))
        print()

        self.solve() # Fill the grid

        missing = 0
        while missing < blank_values:
            x = randint(0,8)
            y = randint(0,8)
            temp = self.get_digit(x, y)
            self.insert_digit(x, y, 0)
            temp_board = deepcopy(self.__board)
            if self.solve() == 1:
                self.__board = deepcopy(temp_board)
                missing += 1
                continue
            else:
                self.__board = deepcopy(temp_board)
                self.insert_digit(x, y, temp)
                continue
        
        self.__unsolved_state = deepcopy(self.__board)
        print()


    def reset_board(self):
        self.__board = deepcopy(self.__unsolved_state)
    

    def check_editable(self, x, y):
        if  self.__unsolved_state[y][x] == 0:
            return True
        else:
            return False
        
    
    def set_board(self, board):
        self.__board = board


    ### Private methods ###

    def __print_row(self, row):
        output = ''
        
        for i in range(0,3):
            output += self.__display_digit(row[i]) + ' '
        output += '| '
        for i in range(3,6):
            output += self.__display_digit(row[i]) + ' '
        output += '| '
        for i in range(6,9):
            output += self.__display_digit(row[i]) + ' '

        return output


    def __display_digit(self, digit):
        if digit == 0:
            return ' '
        else:
            return str(digit)

    
    def __next_unassigned(self):
        for y in range(0, 9):
            for x in range(0, 9):
                if self.get_digit(x, y) == 0:
                    return x, y


    def __recur_solve(self):
        if self.is_complete():
            self.__solutions += 1
            return True
        
        x, y = self.__next_unassigned()
        for i in range(1, 10):
            if self.checked_insert_digit(x, y, i) == True:
                if self.__recur_solve() == True:
                    # We now know that a solution does exist. But we need to check if multiple exist
                    if self.__solutions == 2:
                        return True
                    self.__temp_board = deepcopy(self.__board) # Save the state of the correct solution
        
        self.insert_digit(x, y, 0)
        return False
    
    
    def __vis_recur_solve(self):
        if self.is_complete():
            self.__solutions += 1
            return True
        
        x, y = self.__next_unassigned()
        for i in range(1, 10):
            if self.checked_insert_digit(x, y, i) == True:
                if self.__solutions == 0: #!TEMP
                    self.__steps.append(deepcopy(self.__board))
                if self.__vis_recur_solve() == True:
                    # We now know that a solution does exist. But we need to check if multiple exist
                    if self.__solutions == 2:
                        return True
                    self.__temp_board = deepcopy(self.__board) # Save the state of the correct solution
        
        self.insert_digit(x, y, 0)
        return False
        
