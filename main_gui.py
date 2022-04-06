from turtle import width
from sudoku_board import Sudoku_Board
import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 900

# Colors
BG_COLOR = (20, 189, 172)

canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
canvas.fill(BG_COLOR)

# Draw grid

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()