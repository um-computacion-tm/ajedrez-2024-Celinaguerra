from game.piece import Piece

class Rook(Piece):
    # def __init__(self, color):
    #     super().__init__(color)
    white_str = '♖'
    black_str = '♜'

    def possible_positions_vd(self,row,col):
        #la columna es igual, recorrer filas (mayor)
        possibles = []
        for next_row in range (row + 1, 8):
            possibles.append((next_row,col))
        return possibles

    def possible_positions_va(self,row,col):
        possibles = []
        for next_row in range (row - 1, -1, -1):
            possibles.append((next_row,col))
        return possibles

    def possible_positions_hr(self,row,col):
        possibles = []
        for next_col in range (col + 1, 8):
            possibles.append((row, next_col))
        return possibles

    def possible_positions_hl(self,row,col):
        possibles = []
        for next_col in range (col - 1, -1,-1):
            possibles.append((row, next_col))
        return possibles