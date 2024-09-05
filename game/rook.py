from game.piece import Piece

class Rook(Piece):
    # def __init__(self, color):
    #     super().__init__(color)
    white_str = '♖'
    black_str = '♜'

    def valid_positions(self,from_row, from_col, to_row, to_col):
        possible_positions = (self.possible_positions_hr(from_row, from_col) + self.possible_positions_hl(from_row, from_col) + 
                            self.possible_positions_vd(from_row, from_col) + self.possible_positions_va(from_row, from_col))
        return (to_row, to_col) in possible_positions

#### hacer que verifique si hay una pieza del mismo color enfrente
    def possible_positions_vd(self,row,col):
        #la columna es igual, recorrer filas (mayor)
        possibles = []
        for next_row in range (row + 1, 8):
            other_piece = self.__board__.get_piece(next_row,col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row,col))
                break
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