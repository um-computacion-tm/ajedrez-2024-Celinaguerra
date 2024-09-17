from game.piece import Piece

class Rook(Piece):
    white_str = '♖'
    black_str = '♜'

    def get_possible_positions(self,from_row, from_col):
        return self.possible_orthogonal_positions(from_row, from_col)
