from sudoku_board import Sudoku_Board
import pygame
import sys

# Initialise components
pygame.init()
pygame.font.init()
board = Sudoku_Board()


# Canvas dimensions
WIDTH = 594
HEIGHT = 675

# Colors
C_RED = (255, 0, 0)
C_BG = (20, 189, 172)
C_GRID = (13, 161, 146)
C_DIGIT = (6, 84, 76)
C_ACCENT = (14, 138, 125)

# Fonts
font = pygame.font.SysFont("Arial", 40)


# Variables
selected_x = 0
selected_y = 3
if WIDTH < HEIGHT:
    diff = WIDTH // 9
else:
    diff = HEIGHT // 9

# Set up canvas
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
canvas.fill(C_BG)


def display_digit(digit):
    if digit == 0:
            return ' '
    else:
        return str(digit)

def update_screen():
    canvas.fill(C_BG) # Clear the screen
    draw_grid()
    draw_box()


def draw_grid():
    # Draw grid lines
    for i in range(0, 10):
        if i % 3 == 0:
            thinkness = 3
        else:
            thinkness = 1
        # Horizontal
        pygame.draw.line(canvas, C_GRID, (0, i * diff), (diff * 9, i*diff), thinkness)
        # Vertical
        pygame.draw.line(canvas, C_GRID, (i * diff, 0), (i * diff, diff * 9), thinkness)
    
    # Draw numbers
    grid = board.get_board()
    x_font_offset = 23
    y_font_offset = 10
    for x in range(9):
        for y in range(9):
            digit_text = font.render(display_digit(board.get_digit(x, y)), 1, C_DIGIT)
            canvas.blit(digit_text, (x * diff + x_font_offset, y * diff + y_font_offset))

# Highlight selected box
def draw_box():
    for i in range(2):
        # Horizontal
        pygame.draw.line(canvas, C_ACCENT, (selected_x * diff - 1, diff*(selected_y + i)), (selected_x * diff + diff + 1, diff*(selected_y + i)), 3)
        # Vertical
        pygame.draw.line(canvas, C_ACCENT, (diff*(selected_x + i), selected_y * diff - 1), (diff*(selected_x + i), selected_y * diff + diff + 1), 3)

def select_cell(pos):
    global selected_x
    selected_x = pos[0] // diff
    global selected_y
    selected_y = pos[1]//diff
    update_screen()

def insert_digit(value):
    is_valid = board.checked_insert_digit(selected_x, selected_y, value)
    update_screen()
    if not is_valid:
        write_to_screen("You can't put that there!")

def new_board():
    board.new_board()
    update_screen()

def solve():
    is_solvable = board.solve()
    update_screen()
    if is_solvable == 0:
        write_to_screen("This cannot be solved :(")

def write_to_screen(message):
    text = font.render(str(message), 1, C_DIGIT)
    y_pos = HEIGHT - ((HEIGHT - WIDTH) / 2)
    text_rect = text.get_rect(center=(WIDTH / 2, y_pos))
    canvas.blit(text, text_rect)



update_screen()
write_to_screen("Welcome to sudoku!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            select_cell(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                solve()
            if event.key == pygame.K_n:
                new_board()
            if event.key == pygame.K_0:
                insert_digit(0)
            if event.key == pygame.K_1:
                insert_digit(1)
            if event.key == pygame.K_2:
                insert_digit(2)
            if event.key == pygame.K_3:
                insert_digit(3)
            if event.key == pygame.K_4:
                insert_digit(4)
            if event.key == pygame.K_5:
                insert_digit(5)
            if event.key == pygame.K_6:
                insert_digit(6)
            if event.key == pygame.K_7:
                insert_digit(7)
            if event.key == pygame.K_8:
                insert_digit(8)
            if event.key == pygame.K_9:
                insert_digit(9)
    
    pygame.display.update()