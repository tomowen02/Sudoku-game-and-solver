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
        #Check row
        for i in range(0,9):
            if value == self.board[y][i]:
                return False

        # Check col
        for i in range(0,9):
            if value == self.board[i][x]:
                return False

        # Check box
        box_x = (x // 3) * 3
        box_y = (y // 3) * 3
        for i in range(box_y, box_y + 3): # Cycle through rows in box
            for j in range(box_x, box_x + 3): # Cycle through columns in box
                if self.board[i][j] == value:
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