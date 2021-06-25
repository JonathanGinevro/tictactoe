from main import tictactoePuzzle
import random
import math


def main_menu():
    print("Hello and welcome to TicTacToe!")

    choice = input("Please select 1 for Single Player and 2 for Multiplayer:")

    play_again = 1

    while play_again == 1:

        if choice == "2":
            play_game()
        else:
            computer_game()

        play_again = int(input("Please select 1 to play again, and 0 to end "
                               "the game:"))

    print("Bye :)")


def play_game():
    game = tictactoePuzzle()

    print("Hello and welcome to Multiplayer! Here is your board:")
    print(game)

    player = 1

    while not game.is_board_full() and not game.is_winner(
            "X") and not game.is_winner("O"):

        x_value = int(input("Player " + str(player) +
                            ", please choose your x value:"))
        y_value = int(input("Now choose your y value:"))

        if player == 1:
            game.place((x_value, y_value), "X")
            player = 2
        else:
            game.place((x_value, y_value), "O")
            player = 1

        print(game)

    if game.is_board_full() and not game.is_winner("X") and not game.is_winner(
            "O"):
        print("Tie Game!")
    else:
        print(
            "Congratulations, Player " + str(player - 1) + " has won the game!")


def smart_computer_game():
    game = tictactoePuzzle()

    print("Hey Bucko! Here is your board:")
    print(game)

    player = 1

    while not game.is_board_full() and not game.is_winner(
            "X") and not game.is_winner("O"):

        if player == 1:

            x_value = int(input("Player 1, please choose your x value:"))
            y_value = int(input("Now choose your y value:"))

            game.place((x_value, y_value), "X")
            player = 2

        else:
            print("It is now the computer's turn!")

            depth = len(game.empty_cells())
            mini = game.minimax(depth, 1)

            x_cord = mini[0]
            y_cord = mini[1]

            game.place((x_cord, y_cord), "O")

            player = 1

        print(game)

    if game.is_board_full() and not game.is_winner("X") and not game.is_winner(
            "O"):
        print("Tie Game!")
    elif game.is_winner("O"):
        print("The computer has won the game!")
    else:
        print("Congratulations, Player 1 has won the game!")


def computer_game():
    game = tictactoePuzzle()

    print("Hello and welcome to Single Player! Here is your board:")
    print(game)

    player = 1

    while not game.is_board_full() and not game.is_winner(
            "X") and not game.is_winner("O"):

        if player == 1:

            x_value = int(input("Player 1, please choose your x value:"))
            y_value = int(input("Now choose your y value:"))

            game.place((x_value, y_value), "X")
            player = 2

        else:
            print("It is now the computer's turn!")

            if game.check_rows("O") is not None:
                value1 = game.check_rows("O")[0]
                value2 = game.check_rows("O")[1]
                game.place((value1, value2), "O")
            elif game.check_rows("X") is not None:
                value1 = game.check_rows("X")[0]
                value2 = game.check_rows("X")[1]
                game.place((value1, value2), "O")
            else:
                value1 = random.randrange(1, 4)
                value2 = random.randrange(1, 4)

                while not game.place((value1, value2), "O"):
                    value1 = random.randrange(1, 4)
                    value2 = random.randrange(1, 4)

            player = 1

        print(game)

    if game.is_board_full() and not game.is_winner("X") and not game.is_winner(
            "O"):
        print("Tie Game!")
    elif game.is_winner("O"):
        print("The computer has won the game!")
    else:
        print("Congratulations, Player 1 has won the game!")


if __name__ == "__main__":
    main_menu()
