from game.piece import Piece
from game.queen import Queen

class Pawn(Piece):
    white_str = '♙'
    black_str = '♟'

    def get_possible_positions(self, from_row, from_col):
        possibles = self.get_possible_positions_move(
            from_row,
            from_col,
        )
        possibles.extend(
            self.get_possible_positions_eat(from_row, from_col)
        )
        return possibles

    def get_possible_positions_eat(self, from_row, from_col):
        direction = 1 if self.__color__ == "BLACK" else -1
        enemy_color = "WHITE" if self.__color__ == "BLACK" else "BLACK"
        positions = []

        for col_offset in [-1, 1]:
            new_col = from_col + col_offset
            if 0 <= new_col <= 7:  # Verificar que la nueva columna esté dentro del rango
                other_piece = self.__board__.get_piece(from_row + direction, new_col)
                if other_piece and other_piece.__color__ == enemy_color:
                    positions.append((from_row + direction, new_col))

        return positions

    def get_possible_positions_move(self, from_row, from_col):
        direction = 1 if self.__color__ == "BLACK" else -1
        start_row = 1 if self.__color__ == "BLACK" else 6
        end_row = 7 if self.__color__ == "BLACK" else 0
        positions = []

        if self.__board__.get_piece(from_row + direction, from_col) is None:
            next_row = from_row + direction
            positions.append((next_row, from_col))
            if from_row == start_row and self.__board__.get_piece(from_row + 2 * direction, from_col) is None:
                positions.append((from_row + 2 * direction, from_col))
            # Promoción a reina
            if next_row == end_row:
                self.__board__.set_piece(next_row, from_col, Queen(self.__color__, self.__board__))

        return positions