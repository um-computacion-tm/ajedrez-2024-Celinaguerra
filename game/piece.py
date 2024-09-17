class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == 'WHITE':
            return self.white_str
        else:
            return self.black_str 

    def get_color(self):
        return self.__color__

    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        possible_positions = self.get_possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions

############################################### DIAGONAL

    def possible_diagonal_positions(self, from_row, from_col):
        return (
            self.possible_positions_rd(from_row, from_col) +
            self.possible_positions_ru(from_row, from_col) +
            self.possible_positions_ld(from_row, from_col) +
            self.possible_positions_lu(from_row, from_col)
        )

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

############################################### ORTOGONAL

    def possible_orthogonal_positions(self, from_row, from_col):
        return (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col) +
            self.possible_positions_hr(from_row, from_col) +
            self.possible_positions_hl(from_row, from_col)
        )

    def possible_positions_vd(self,row,col):
        #la columna es igual, recorrer filas (mayor)
        possibles = []
        for next_row in range (row + 1, 8):
            other_piece = self.__board__.get_piece(next_row,col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row,col))
                break
            possibles.append((next_row,col))
        return possibles

    def possible_positions_va(self,row,col):
        possibles = []
        for next_row in range (row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row,col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row,col))
                break
            possibles.append((next_row,col))
        return possibles

    def possible_positions_hr(self,row,col):
        possibles = []
        for next_col in range (col + 1, 8):
            other_piece = self.__board__.get_piece(row,next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row,next_col))
                break
            possibles.append((row, next_col))
        return possibles

    def possible_positions_hl(self,row,col):
        possibles = []
        for next_col in range (col - 1, -1,-1):
            other_piece = self.__board__.get_piece(row,next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row,next_col))
                break
            possibles.append((row, next_col))
        return possibles

################################