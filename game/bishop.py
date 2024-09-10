from game.piece import Piece

class Bishop(Piece):
    white_str = '♗'
    black_str = '♝'

    def possible_positions_rd(self, row, col):
        # Diagonal descendente (hacia abajo a la derecha)
        possibles = []
        for next_row, next_col in zip(range(row + 1, 8), range(col + 1, 8)):
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
        return possibles

    def possible_positions_ru(self, row, col):
        # Diagonal ascendente (hacia arriba a la derecha)
        possibles = []
        for next_row, next_col in zip(range(row - 1, -1, -1), range(col + 1, 8)):
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
        return possibles

    def possible_positions_ld(self, row, col):
        # Diagonal descendente (hacia abajo a la izquierda)
        possibles = []
        for next_row, next_col in zip(range(row + 1, 8), range(col - 1, -1, -1)):
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
        return possibles

    def possible_positions_lu(self, row, col):
        # Diagonal ascendente (hacia arriba a la izquierda)
        possibles = []
        for next_row, next_col in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
        return possibles