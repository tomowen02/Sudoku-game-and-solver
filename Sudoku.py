from Sudoku_Board import Sudoku_Board


def get_input():
    while True:
        try:
            x = input("Insert the x coordinate: ")
            y = input("Insert the y coordinate: ")
            value = input("Insert the value to insert: ")
            
            if not(check_input(x, True) and check_input(y, True) and check_input(value, False)):
                raise # One of the values is not valid

            return int(x) - 1, int(y) - 1, int(value)
        except:
            print("An input was invalid!")

def check_input(value, is_cord):
    if not (value.isdigit and len(value) == 1): return False
    if is_cord and value == '0': return False
    return True



board = Sudoku_Board()

# Get game mode
while True:
    try:
        game_mode = int(input('''
    Please chose a game mode:
    1) Assisted
    2) Solver

    Your choice: '''))

        if game_mode != 1 and game_mode != 2: raise
        break
    except:
        print("Invalid input!")


board.print_board()
if game_mode == 1:
    while not board.is_complete():
        x, y, value = get_input()
        if not board.checked_insert_digit(x, y, value):
            print("This number can't go there!")
            continue
        board.print_board()
    
    print("Congratulations!!")
if game_mode == 2:
    if board.solve() != 0:
        print("Solution: ")
        board.print_board()
    else:
        print("This has not valid solutions :(")

print()