from main import tictactoePuzzle


def two_row(tictactoePuzzle):

    column1 = [self.row1[0], self.row2[0], self.row3[0]]
    column2 = [self.row1[1], self.row2[1], self.row3[1]]
    column3 = [self.row1[2], self.row2[2], self.row3[2]]
    columns = [column1, column2, column3]

    diagonal1 = [self.row1[0], self.row2[1], self.row3[2]]
    diagonal2 = [self.row1[2], self.row2[1], self.row3[0]]
    diagonals = [diagonal1, diagonal2]

    for row in self.rows:
        if row[0] == i and row[1] == i and row[2] == i:
            return True

    for column in columns:
        if column[0] == i and column[1] == i and column[2] == i:
            return True

    for diagonal in diagonals:
        if diagonal[0] == i and diagonal[1] == i and diagonal[2] == i:
            return True

    return False
