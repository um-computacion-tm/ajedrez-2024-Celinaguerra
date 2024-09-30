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

    def possible_positions(self, from_row, from_col, directions):
        possibles = []
        for row_step, col_step in directions:
            next_row, next_col = from_row + row_step, from_col + col_step
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, next_col))
                    break
                possibles.append((next_row, next_col))
                next_row += row_step
                next_col += col_step
        return possibles

    # def possible_diagonal_positions(self, from_row, from_col):
    #     directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]  # Diagonales
    #     return self.possible_positions(from_row, from_col, directions)

    def possible_orthogonal_positions(self, from_row, from_col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Ortogonales
        return self.possible_positions(from_row, from_col, directions)

# ############################################### DIAGONAL

    def possible_diagonal_positions(self, from_row, from_col):
        return (
            self.diag_possible_positions(from_row, from_col, 1, 1) +  # diagonal descendente derecha
            self.diag_possible_positions(from_row, from_col, -1, 1) +  # diagonal ascendente derecha
            self.diag_possible_positions(from_row, from_col, 1, -1) +  # diagonal descendente izquierda
            self.diag_possible_positions(from_row, from_col, -1, -1)  # diagonal ascendente izquierda
        )

    def diag_possible_positions(self, row, col, row_step, col_step):
        possibles = []
        next_row, next_col = row + row_step, col + col_step
        while 0 <= next_row < 8 and 0 <= next_col < 8:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row += row_step
            next_col += col_step
        return possibles

# ############################################### ORTOGONAL

#     def possible_orthogonal_positions(self, from_row, from_col):
#         return (
#             self.orth_possible_positions(from_row, from_col, 1, 0) +  # vertical down
#             self.orth_possible_positions(from_row, from_col, -1, 0) +  # vertical asc
#             self.orth_possible_positions(from_row, from_col, 0, 1) +  # horizontal right
#             self.orth_possible_positions(from_row, from_col, 0, -1)  # horizontal left
#         )

#     def orth_possible_positions(self, row, col, row_step, col_step):
#         possibles = []
#         next_row, next_col = row + row_step, col + col_step
#         while 0 <= next_row < 8 and 0 <= next_col < 8:
#             other_piece = self.__board__.get_piece(next_row, next_col)
#             if other_piece is not None:
#                 if other_piece.__color__ != self.__color__:
#                     possibles.append((next_row, next_col))
#                 break
#             possibles.append((next_row, next_col))
#             next_row += row_step
#             next_col += col_step
#         return possibles