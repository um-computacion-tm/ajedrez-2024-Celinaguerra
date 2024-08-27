from game.piece import Piece

class Rook(Piece):
    # def __init__(self, color):
    #     super().__init__(color)
    white_str = 'torre blanca'
    black_str = 'torre negra'

    def __str__(self):
        return '♖' if self.__color__ == 'WHITE' else '♜'

    def possible_positions_vd(self,row,col):
        #la columna es igual, recorrer filas (mayor)
        possibles = []
        for next_row in range (row + 1, 8):
            possibles.append((next_row,col))
        return possibles