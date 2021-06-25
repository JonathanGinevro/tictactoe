import pygame
import sys
from main import tictactoePuzzle


def cord_convertor(x_cord, y_cord):
    if x_cord == 0 and y_cord == 0:
        x_cord = 1
        y_cord = 3
    elif x_cord == 0 and y_cord == 1:
        x_cord = 1
        y_cord = 2
    elif x_cord == 0 and y_cord == 2:
        x_cord = 1
        y_cord = 1
    elif x_cord == 1 and y_cord == 0:
        x_cord = 2
        y_cord = 3
    elif x_cord == 1 and y_cord == 1:
        x_cord = 2
        y_cord = 2
    elif x_cord == 1 and y_cord == 2:
        x_cord = 2
        y_cord = 1
    elif x_cord == 2 and y_cord == 0:
        x_cord = 3
        y_cord = 3
    elif x_cord == 2 and y_cord == 1:
        x_cord = 3
        y_cord = 2
    elif x_cord == 2 and y_cord == 2:
        x_cord = 3
        y_cord = 1

    return x_cord, y_cord


def cord_convertor2(x_cord, y_cord):
    if x_cord == 1 and y_cord == 3:
        x_cord = 0
        y_cord = 0
    elif x_cord == 1 and y_cord == 2:
        x_cord = 0
        y_cord = 1
    elif x_cord == 1 and y_cord == 1:
        x_cord = 0
        y_cord = 2
    elif x_cord == 2 and y_cord == 3:
        x_cord = 1
        y_cord = 0
    elif x_cord == 2 and y_cord == 2:
        x_cord = 1
        y_cord = 1
    elif x_cord == 2 and y_cord == 1:
        x_cord = 1
        y_cord = 2
    elif x_cord == 3 and y_cord == 3:
        x_cord = 2
        y_cord = 0
    elif x_cord == 3 and y_cord == 2:
        x_cord = 2
        y_cord = 1
    elif x_cord == 3 and y_cord == 1:
        x_cord = 2
        y_cord = 2

    return x_cord, y_cord


pygame.init()

WIDTH = 600
HEIGHT = 600

LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SQUARE_SIZE = 200
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")
screen.fill(BG_COLOR)

game = tictactoePuzzle()


def game_over():
    # (x coordinate, y coordinate, base, height)
    pygame.draw.rect(screen, RED, (1, 1, 100, 50))

game_over()

def draw_lines():
    # (screen, colour, starting point, ending point, width)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def draw_figures():
    for row in game.rows:
        for cell in row:
            x_value, y_value = cord_convertor2(cell.cord[0], cell.cord[1])
            if cell.value == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                    int(x_value * 200 + 100), int(y_value * 200 + 100)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif cell.value == "X":
                pygame.draw.line(screen, CROSS_COLOR, (
                    x_value * SQUARE_SIZE + SPACE,
                    y_value * SQUARE_SIZE + SQUARE_SIZE - SPACE), (
                                     x_value * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                     y_value * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (
                    x_value * SQUARE_SIZE + SPACE,
                    y_value * SQUARE_SIZE + SPACE), (
                                     x_value * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                     y_value * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


draw_lines()

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        player = 1

        if game.is_board_full():
            game = tictactoePuzzle()
            screen.fill(BG_COLOR)
            draw_lines()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_col = int(mouseX // 200)
            clicked_row = int(mouseY // 200)

            clicked_col_1, clicked_row_1 = cord_convertor(clicked_col,
                                                          clicked_row)
            game.place((clicked_col_1, clicked_row_1), "X")
            draw_figures()

            # Computer's Turn
            depth = len(game.empty_cells())
            mini = game.minimax(depth, 1)

            x_cord = mini[0]
            y_cord = mini[1]

            if x_cord == 0 and y_cord == 0:
                x_cord = 1
                y_cord = 1
            elif x_cord == 0 and y_cord == 1:
                x_cord = 2
                y_cord = 1
            elif x_cord == 0 and y_cord == 2:
                x_cord = 3
                y_cord = 1
            elif x_cord == 1 and y_cord == 0:
                x_cord = 1
                y_cord = 2
            elif x_cord == 1 and y_cord == 1:
                x_cord = 2
                y_cord = 2
            elif x_cord == 1 and y_cord == 2:
                x_cord = 3
                y_cord = 2
            elif x_cord == 2 and y_cord == 0:
                x_cord = 1
                y_cord = 3
            elif x_cord == 2 and y_cord == 1:
                x_cord = 2
                y_cord = 3
            elif x_cord == 2 and y_cord == 2:
                x_cord = 3
                y_cord = 3

            game.place((x_cord, y_cord), "O")

            draw_figures()

    pygame.display.update()
