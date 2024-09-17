from game.rook import Rook
from game.pawn import Pawn 
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.knight import Knight 
from game.exceptions import OutOfBoard


class Board:
    def __init__(self, for_test = False):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            self.__positions__[0][0] = Rook("BLACK",self)
            self.__positions__[0][7] = Rook("BLACK",self)
            self.__positions__[7][7] = Rook("WHITE",self)
            self.__positions__[7][0] = Rook("WHITE",self)
            self.__positions__[0][1] = Knight("BLACK",self)
            self.__positions__[0][6] = Knight("BLACK",self)
            self.__positions__[7][1] = Knight("WHITE",self)
            self.__positions__[7][6] = Knight("WHITE",self)
            self.__positions__[0][2] = Bishop("BLACK",self)
            self.__positions__[0][5] = Bishop("BLACK",self)
            self.__positions__[7][2] = Bishop("WHITE",self)
            self.__positions__[7][5] = Bishop("WHITE",self)
            self.__positions__[0][3] = Queen("BLACK",self)
            self.__positions__[7][3] = Queen("WHITE",self)
            self.__positions__[0][4] = King("BLACK",self)
            self.__positions__[7][4] = King("WHITE",self)
            for col in range(8):
                self.__positions__[1][col] = Pawn("BLACK",self)
                self.__positions__[6][col] = Pawn("WHITE",self)


    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def __str__(self):
        board_str = "  " + " ".join(str(i) for i in range(8)) + "\n"
        for i, row in enumerate(self.__positions__):
            board_str += str(i) + " "
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "
                else:
                    board_str += ". "
            board_str += str(i) + "\n"
        board_str += "  " + " ".join(str(i) for i in range(8)) + "\n"
        return board_str
