from game.piece import Piece

class Rook(Piece):
    # def __init__(self, color):
    #     super().__init__(color)
    white_str = '♖'
    black_str = '♜'

    def get_possible_positions(self,from_row, from_col, to_row, to_col):
        possible_positions = self.possible_orthogonal_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions
