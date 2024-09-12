from game.piece import Piece

class Bishop(Piece):
    white_str = '♗'
    black_str = '♝'

    def valid_positions_diagonal(self, from_row, from_col, to_row, to_col):
        possible_positions = (self.possible_positions_rd(from_row, from_col) + self.possible_positions_ru(from_row, from_col) +
                            self.possible_positions_ld(from_row, from_col) + self.possible_positions_lu(from_row, from_col))
        return (to_row, to_col) in possible_positions

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