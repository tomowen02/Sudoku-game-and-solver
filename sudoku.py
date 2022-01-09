board = [
    [], # Bottom section (0)
    [], # Middle section (1)
    [] # Top section (2)
]

def print_board(board):
    print(f'''

    {print_row(board[0][0])}
    {print_row(board[0][1])}
    {print_row(board[0][2])}
    ------+-------+------
    {print_row(board[0][0])}
    {print_row(board[0][1])}
    {print_row(board[0][2])}
    ------+-------+------
    {print_row(board[0][0])}
    {print_row(board[0][1])}
    {print_row(board[0][2])}

    ''')

def print_row(row):
    return (f"{row[0][0]} {row[0][1]} {row[0][2]} | {row[1][0]} {row[1][1]} {row[1][2]} | {row[2][0]} {row[2][1]} {row[2][2]}")



### Debugging
x1 = [
    ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']
]

x2 = [
    ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']
]

x3 = [
    ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']
]

y1 = [x1, x2, x3]
y2 = [x1, x2, x3]
y3 = [x1, x2, x3]

z = [y1, y2, y3]

print_board(z)

#print(x1[0][0])