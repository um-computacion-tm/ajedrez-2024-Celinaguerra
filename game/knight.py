from game.piece import Piece

class Knight(Piece):
    white_str = '♘'
    black_str = '♞'

    def get_possible_positions(self, from_row, from_col):
        return ()