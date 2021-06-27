from math import inf as infinity

HUMAN = +1
COMP = -1


class tictactoePuzzle:

    def __init__(self):

        self.rows = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]

    def __str__(self):

        return " {} | {} | {} \
              \n---|---|--- \
              \n {} | {} | {} \
              \n---|---|--- \
              \n {} | {} | {} ".format(self.rows[0][0], self.rows[0][1],
                                       self.rows[0][2], self.rows[1][0],
                                       self.rows[1][1], self.rows[1][2],
                                       self.rows[2][0], self.rows[2][1],
                                       self.rows[2][2])

    def __getitem__(self, item):
        return self.rows[item]

    def create_board(self):
        column1 = [self.rows[0][0], self.rows[1][0], self.rows[2][0]]
        column2 = [self.rows[0][1], self.rows[1][1], self.rows[2][1]]
        column3 = [self.rows[0][2], self.rows[1][2], self.rows[2][2]]

        diagonal1 = [self.rows[0][0], self.rows[1][1], self.rows[2][2]]
        diagonal2 = [self.rows[2][0], self.rows[1][1], self.rows[0][2]]

        board = [column1, column2, column3, diagonal1, diagonal2,
                 self.rows[0], self.rows[1], self.rows[2]]

        return board

    def place(self, cords: tuple, value):
        self[cords[0]][cords[1]] = value

    def is_board_full(self):
        for row in self.rows:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def evaluate(self):
        if self.is_winner("O"):
            score = 1
        elif self.is_winner("X"):
            score = -1
        else:
            score = 0

        return score

    def is_winner(self, value):
        board = self.create_board()

        for three in board:
            if three[0] == value and three[1] == value and three[2] == value:
                return True
        return False

    def winner_cords(self):
        winner = ["X", "O"]

        for option in winner:

            for col in range(3):
                if self.rows[0][col] == option and self.rows[1][
                    col] == option and self.rows[2][col] == option:
                    return (0, col), (2, col)

            for row in range(3):
                if self.rows[row][0] == option and self.rows[row][
                    1] == option and self.rows[row][2] == option:
                    return (row, 0), (row, 2)

            if self.rows[2][0] == option and self.rows[1][1] == option and \
                    self.rows[0][2] == option:
                return (2, 0), (0, 2)

            if self.rows[0][0] == option and self.rows[1][1] == option and \
                    self.rows[2][2] == option:
                return (0, 0), (2, 2)

    def game_over(self):
        return self.is_winner("X") or self.is_winner("O")

    def empty_cells(self):
        cell_list = []

        for x, row in enumerate(self.rows):
            for y, cell in enumerate(row):
                if cell == " ":
                    cell_list.append([x, y])

        return cell_list

    def valid_move(self, x, y):
        if (x, y) in self.empty_cells():
            return True
        return False

    def num_empty_spaces(self):
        return len(self.empty_cells())

    # def check_rows(self, value):
    #     board = self.create_board()
    #     row_counter = 0
    #
    #     for row in board:
    #         c1 = 0
    #         c2 = 0
    #         return_value = None
    #
    #         cell_counter = 0
    #
    #         for cell in row:
    #             if cell == value:
    #                 c1 += 1
    #             elif cell == " ":
    #                 c2 += 1
    #                 return_value = (row_counter, cell_counter)
    #
    #             cell_counter += 1
    #
    #         if c1 == 2 and c2 == 1:
    #             return return_value
    #
    #         row_counter += 1
    #
    #     return None

    def minimax(self, depth, player):
        if player == 1:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, infinity]

        if depth == 0 or self.game_over():
            score = self.evaluate()
            return [-1, -1, score]

        for cell in self.empty_cells():
            x, y = cell[0], cell[1]

            if player == 1:
                self[x][y] = "O"
            else:
                self[x][y] = "X"

            score = self.minimax(depth - 1, -player)

            self[x][y] = " "
            score[0], score[1] = x, y

            if player == 1:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best
