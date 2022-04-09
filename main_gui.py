from sudoku_board import Sudoku_Board
import pygame
import sys

pygame.init()
pygame.font.init()


# Canvas dimensions
WIDTH = 594
HEIGHT = 700

# Colors
C_BG = (20, 189, 172)
C_RED = (255, 0, 0)
C_GRID = (13, 161, 146)
C_ACCENT = (84, 84, 84)


# Variables
x = 4
y = 4
if WIDTH < HEIGHT:
    diff = WIDTH // 9
else:
    diff = HEIGHT // 9

# Set up canvas
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
canvas.fill(C_BG)

def get_cords(pos):
    global x
    x = pos[0] // diff
    global y
    y = pos[1]//diff

    return (x, y)

# Highlight selected box
def draw_box():
    for i in range(2):
        # Horizontal
        pygame.draw.line(canvas, C_ACCENT, (x * diff - 2, diff*(y + i)), (x * diff + diff + 2, diff*(y + i)), 5)
        # Vertical
        pygame.draw.line(canvas, C_ACCENT, (diff*(x + i), y * diff - 2), (diff*(x + i), y * diff + diff + 2), 5)


# Draw grid
for i in range(1, 9):
    # Horizontal
    pygame.draw.line(canvas, C_GRID, (0, i * diff), (diff * 9, i*diff), 3)
    pygame.draw.line(canvas, C_GRID, (i * diff, 0), (i * diff, diff * 9), 3)

draw_box()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()