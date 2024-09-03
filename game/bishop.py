from game.piece import Piece

class Bishop(Piece):
    white_str = '♗'
    black_str = '♝'

    def possible_positions_rd(self, row, col):
        # Diagonal descendente (hacia abajo a la derecha)
        possibles = []
        for next_row, next_col in zip(range(row + 1, 8), range(col + 1, 8)):
            possibles.append((next_row, next_col))
        return possibles

    def possible_positions_ru(self, row, col):
        # Diagonal ascendente (hacia arriba a la derecha)
        possibles = []
        for next_row, next_col in zip(range(row - 1, -1, -1), range(col + 1, 8)):
            possibles.append((next_row, next_col))
        return possibles