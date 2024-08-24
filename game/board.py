from game.rook import Rook
from game.pawn import Pawn 

class InvalidMoveError(Exception):
    pass

class InvalidCoordError(Exception):
    pass

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
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK")
            self.__positions__[6][col] = Pawn("WHITE")


    def get_piece(self,row,col):
        return self.__positions__[row][col]


    def move_piece(self, from_row, from_col, to_row, to_col):
        if not self._are_valid_coords(from_row, from_col, to_row, to_col):
            raise InvalidCoordError("Invalid coordinates")
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise InvalidMoveError("No piece at given coordinates")
        self.__positions__[from_row][from_col] = None
        self.__positions__[to_row][to_col] = piece

    def _are_valid_coords(self, from_row, from_col, to_row, to_col):
        return all(0 <= x < 8 for x in [from_row, from_col, to_row, to_col])

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__[row][col]