from game.piece import Piece

class Bishop(Piece):
    white_str = '♗'
    black_str = '♝'

    def get_possible_positions(self,from_row, from_col, to_row, to_col):
        possible_positions = self.possible_diagonal_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions