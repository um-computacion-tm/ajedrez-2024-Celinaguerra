from game.rook import Rook

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][7] = Rook("WHITE")
        self.__positions__[7][0] = Rook("WHITE")

    def get_piece(self,row,col):
        return self.__positions__[row][col]

##hacer excepcion de lugar incorrecto
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        self.__positions__[from_row][from_col] = None
        self.__positions__[to_row][to_col] = piece