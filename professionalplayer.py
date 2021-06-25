from main import tictactoePuzzle


class Tree:

    def __init__(self, root, subtrees):
        self._root = root
        self._subtrees = subtrees


def game_tree(game: tictactoePuzzle):
    if game.is_board_full():
        return Tree(game, None)
    else:
        for cell in game.empty_cells():
            game.place((cell[0], cell[1]), "X")
