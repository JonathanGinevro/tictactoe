import pygame
import sys
from main import tictactoePuzzle

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
pygame.display.set_caption("Impossible TicTacToe")
screen.fill(BG_COLOR)

game = tictactoePuzzle()


def game_over():
    # (x coordinate, y coordinate, base, height)
    pygame.draw.rect(screen, RED, (1, 1, 200, 100))


def draw_lines():
    # (screen, colour, starting point, ending point, width)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def draw_winning_line(start_cords, end_cords):

    if game.is_winner("O"):
        colour = CIRCLE_COLOR
    else:
        colour = CROSS_COLOR

    pygame.draw.line(screen, colour,
                     (start_cords[0] * 200 + 100, start_cords[1] * 200 + 100),
                     (end_cords[0] * 200 + 100, end_cords[1] * 200 + 100),
                     LINE_WIDTH)


def draw_figures():
    for row in range(len(game.rows)):
        for cell in range(len(game.rows[row])):
            x_value = row
            y_value = cell

            if game.rows[row][cell] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                int(x_value * 200 + 100), int(y_value * 200 + 100)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif game.rows[row][cell] == "X":
                pygame.draw.line(screen, CROSS_COLOR, (
                x_value * SQUARE_SIZE + SPACE,
                y_value * SQUARE_SIZE + SQUARE_SIZE - SPACE), (
                                 x_value * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                 y_value * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (
                x_value * SQUARE_SIZE + SPACE, y_value * SQUARE_SIZE + SPACE), (
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game = tictactoePuzzle()
                screen.fill(BG_COLOR)
                draw_lines()

        if game.is_winner("X") or game.is_winner("O"):
            x1, y1 = game.winner_cords()[0][0], game.winner_cords()[0][1]
            x2, y2 = game.winner_cords()[1][0], game.winner_cords()[1][1]

            draw_winning_line((x1, y1), (x2, y2))

        if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over() and not game.is_board_full():

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_col = int(mouseX // 200)
            clicked_row = int(mouseY // 200)

            game.place((clicked_col, clicked_row), "X")
            draw_figures()

            # Computer's Turn
            if not game.is_board_full():
                depth = len(game.empty_cells())
                mini = game.minimax(depth, 1)

                x_cord = mini[0]
                y_cord = mini[1]

                game.place((x_cord, y_cord), "O")

                draw_figures()

    pygame.display.update()
