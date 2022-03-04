class Sudoku_Board:
    
    def __init__(self):
        self.board = [
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
    


    ### Public methods ###

    def print_board(self):
        print(f'''
        {self.__print_row(self.board[8])}
        {self.__print_row(self.board[7])}
        {self.__print_row(self.board[6])}
        ------+-------+------
        {self.__print_row(self.board[5])}
        {self.__print_row(self.board[4])}
        {self.__print_row(self.board[3])}
        ------+-------+------
        {self.__print_row(self.board[2])}
        {self.__print_row(self.board[1])}
        {self.__print_row(self.board[0])}
        ''')


    def insert_digit(self, x, y, value):
        self.board[y][x] = value


    def checked_insert_digit(self, x, y, value):
        if self.check(x, y, value):
            self.insert_digit(x, y, value)
            return True
        else:
            return False

    
    def check(self, x, y, value):
        if value == 0:
            self.insert_digit(x, y, value)
            return True

        #Check row
        temp = self.board[y][x]
        self.insert_digit(x, y, 0)

        for i in range(0,9):
            if value == self.board[y][i]:
                self.insert_digit(x, y, temp)
                return False

        # Check col
        for i in range(0,9):
            if value == self.board[i][x]:
                self.insert_digit(x, y, temp)
                return False

        # Check box
        box_x = (x // 3) * 3
        box_y = (y // 3) * 3
        for i in range(box_y, box_y + 3): # Cycle through rows in box
            for j in range(box_x, box_x + 3): # Cycle through columns in box
                if self.board[i][j] == value:
                    self.insert_digit(x, y, temp)
                    return False
        
        self.insert_digit(x, y, temp)
        return True


    def solve(self):
        if self.is_complete():
            return True
        
        x, y = self.__next_unassigned()
        for i in range(1, 10):
            if self.checked_insert_digit(x, y, i) == True:
                if self.solve() == True:
                    return True
        self.insert_digit(x, y, 0)
        return False


    def is_complete(self):
        # Check if all spaces are filled
        for i in self.board:
            if 0 in i:
                return False

        # Check if every number that has already been inserted is valid
        for i in range(0, 9):
            for j in range(0, 9):
                value = self.board[i][j]
                if not self.check(j, i, value):
                    return False
        return True


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
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[y])):
                if self.board[y][x] == 0:
                    return x, y
