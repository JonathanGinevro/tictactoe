import pygame
import sys
import random
from main import tictactoePuzzle

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 700

LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SQUARE_SIZE = 200
SPACE = 55

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
MENU_COLOR = (15, 95, 90)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minimax TicTacToe")
screen.fill(BG_COLOR)

# Font Setup
scoreboard_font = pygame.font.SysFont('Calibri Bold', 40)
button_font = pygame.font.SysFont('Calibri Bold', 30)

# Game setup
game = tictactoePuzzle()
x_score = 0
o_score = 0


# Draw bottom menu
def draw_menu():
    # Menu Background
    pygame.draw.rect(screen, LINE_COLOR, (0, 600, 600, 100))

    # Board Reset Button
    pygame.draw.rect(screen, (255, 255, 255), (10, 625, 180, 50), 2, 3)
    text = button_font.render('Reset Board', True, (255, 255, 255))
    screen.blit(text, (40, 641))

    # Computer Start Button
    pygame.draw.rect(screen, (255, 255, 255), (210, 625, 180, 50), 2, 3)
    text = button_font.render('Computer Start', True, (255, 255, 255))
    screen.blit(text, (223, 641))

    # Scoreboard
    pygame.draw.rect(screen, (255, 255, 255), (410, 625, 85, 50), 2, 3)
    pygame.draw.rect(screen, (255, 255, 255), (505, 625, 85, 50), 2, 3)


# Draw TicTacToe grid
def draw_grid():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


# Draw line to outline winner
def draw_winning_line(start_cords, end_cords):
    if game.is_winner("O"):
        colour = CIRCLE_COLOR
    else:
        colour = CROSS_COLOR

    pygame.draw.line(screen, colour,
                     (start_cords[1] * 200 + 100, start_cords[0] * 200 + 100),
                     (end_cords[1] * 200 + 100, end_cords[0] * 200 + 100),
                     LINE_WIDTH)


# Draw "X" and "O" in desired places
def draw_figures():
    for row in range(3):
        for col in range(3):

            if game.rows[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif game.rows[row][col] == "X":
                pygame.draw.line(screen, CROSS_COLOR, (
                    col * SQUARE_SIZE + SPACE,
                    row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (
                                     col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                     row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (
                    col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (
                                     col * SQUARE_SIZE + SQUARE_SIZE - SPACE,
                                     row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


# Check to find possible winner, and mark it with a line
def check_winner():
    if game.is_winner("X") or game.is_winner("O"):

        x1, y1 = game.winner_cords()[0][0], game.winner_cords()[0][1]
        x2, y2 = game.winner_cords()[1][0], game.winner_cords()[1][1]

        draw_winning_line((x1, y1), (x2, y2))


# Change the scoreboard to represent the current score
def update_scoreboard(score1, score2):
    draw_menu()
    text = scoreboard_font.render('O: ' + str(score2), True, (255, 255, 255))
    text2 = scoreboard_font.render('X: ' + str(score1), True, (255, 255, 255))
    screen.blit(text, (425, 638))
    screen.blit(text2, (522, 638))


# Clean up the board
def reset():
    screen.fill(BG_COLOR)
    draw_grid()
    draw_menu()


# Set everything into place
draw_grid()
draw_menu()
computer_start = False

# Mainloop
while True:
    for event in pygame.event.get():

        # User exits the game
        if event.type == pygame.QUIT:
            sys.exit()

        # User places their "X"
        if event.type == pygame.MOUSEBUTTONDOWN and \
                not game.game_over() and \
                not game.is_board_full() and \
                event.pos[0] <= 600 and event.pos[1] <= 600:
            computer_start = True
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            game.place((clicked_row, clicked_col), "X")
            draw_figures()
            player = 1

            if game.is_winner("X"):
                x_score += 1

            if not game.is_board_full():
                depth = len(game.empty_cells())
                mini = game.minimax(depth, 1)

                x_cord = mini[0]
                y_cord = mini[1]

                game.place((x_cord, y_cord), "O")

                draw_figures()

                if game.is_winner("O"):
                    o_score += 1

        # Computer Start
        if event.type == pygame.MOUSEBUTTONDOWN and 210 <= event.pos[0] <= 390 \
                and 625 <= event.pos[1] <= 675 and not computer_start:

            x_random = random.randrange(0, 3)
            y_random = random.randrange(0, 3)

            game.place((x_random, y_random), "O")
            draw_figures()
            computer_start = True

        # User presses reset button
        if event.type == pygame.MOUSEBUTTONDOWN and 10 <= event.pos[0] <= 190 \
                and 625 <= event.pos[1] <= 675:
            game = tictactoePuzzle()
            reset()
            computer_start = False

    update_scoreboard(x_score, o_score)
    check_winner()
    pygame.display.update()
