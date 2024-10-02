from game.piece import Piece

class Rook(Piece):


    white_str = '♖'
    black_str = '♜'

    def __str__(self):
        if self.__color__ == 'WHITE':
            return self.white_str
        else:
            return self.black_str 

    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(from_row, from_col)