from game.piece import Piece

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
            other_piece = self.__board__.get_piece(from_row + direction, from_col + col_offset)
            if other_piece and other_piece.__color__ == enemy_color:
                positions.append((from_row + direction, from_col + col_offset))
        return positions

    def get_possible_positions_move(self, from_row, from_col):
        direction = 1 if self.__color__ == "BLACK" else -1
        start_row = 1 if self.__color__ == "BLACK" else 6
        positions = []

        if self.__board__.get_piece(from_row + direction, from_col) is None:
            positions.append((from_row + direction, from_col))
            if from_row == start_row and self.__board__.get_piece(from_row + 2 * direction, from_col) is None:
                positions.append((from_row + 2 * direction, from_col))
        return positions