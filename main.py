from math import inf as infinity
HUMAN = +1
COMP = -1

class marker:

    def __init__(self, cord):
        self.value = " "
        self.connections = []
        self.cord = cord

    def __str__(self):
        return self.value

    def new_value(self, value):
        self.value = value

    def add_connections(self, connection):
        self.connections.append(connection)


class tictactoePuzzle:

    def __init__(self):
        one_one = marker((1, 1))
        one_two = marker((1, 2))
        one_three = marker((1, 3))
        two_one = marker((2, 1))
        two_two = marker((2, 2))
        two_three = marker((2, 3))
        three_one = marker((3, 1))
        three_two = marker((3, 2))
        three_three = marker((3, 3))

        one_one.connections = [one_two, two_one, two_two]

        self.row3 = [one_three, two_three, three_three]
        self.row2 = [one_two, two_two, three_two]
        self.row1 = [one_one, two_one, three_one]
        self.rows = [self.row1, self.row2, self.row3]

        column1 = [self.row1[0], self.row2[0], self.row3[0]]
        column2 = [self.row1[1], self.row2[1], self.row3[1]]
        column3 = [self.row1[2], self.row2[2], self.row3[2]]
        self.columns = [column1, column2, column3]
        diagonal1 = [self.row1[0], self.row2[1], self.row3[2]]
        diagonal2 = [self.row1[2], self.row2[1], self.row3[0]]
        self.board = [column1, column2, column3, diagonal1, diagonal2,
                      self.row1, self.row2, self.row3]

    def __str__(self):
        return " {} | {} | {} \
              \n---|---|--- \
              \n {} | {} | {} \
              \n---|---|--- \
              \n {} | {} | {} ".format(self.row3[0], self.row3[1],
                                       self.row3[2], self.row2[0],
                                       self.row2[1], self.row2[2],
                                       self.row1[0], self.row1[1],
                                       self.row1[2])

    def __getitem__(self, item):
        return self.rows[item]

    def place(self, cords: tuple, value):
        if cords[0] < 0 or cords[0] > 3:
            return False
        elif cords[1] < 0 or cords[1] > 3:
            return False
        elif self.rows[cords[1] - 1][cords[0] - 1].value != " ":
            return False
        else:
            self.rows[cords[1] - 1][cords[0] - 1].new_value(value)
            return True

    def is_board_full(self):
        for row in self.rows:
            for i in row:
                if i.value == " ":
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
        for row in self.board:
            if row[0].value == value and row[1].value == value and row[2].value == value:
                return True
        return False

    def game_over(self):
        return self.is_winner("X") or self.is_winner("O")

    def empty_cells(self):
        cell_list = []

        for x, row in enumerate(self.rows):
            for y, cell in enumerate(row):
                if cell.value == " ":
                    cell_list.append([x, y])

        return cell_list

    def valid_move(self, x, y):
        if (x, y) in self.empty_cells():
            return True
        else:
            return False

    def available_moves(self):
        counter = 0
        for row in self.rows:
            for square in row:
                if square.value == " ":
                    counter += 1

        return counter

    def check_rows(self, value):

        for row in self.board:

            c1 = 0
            c2 = 0
            return_value = None

            for item in row:
                if item.value == value:
                    c1 += 1
                elif item.value == " ":
                    c2 += 1
                    return_value = item.cord

            if c1 == 2 and c2 == 1:
                return return_value

        return None

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
                self[x][y].value = "O"
            else:
                self[x][y].value = "X"

            score = self.minimax(depth - 1, -player)
            self[x][y].value = " "
            score[0], score[1] = x, y

            if player == 1:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best





