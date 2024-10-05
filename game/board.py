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

        if isinstance(origin, Pawn) and (to_row == 0 or to_row == 7):
            self.set_piece(to_row, to_col, Queen(origin.__color__, self))

    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def is_king_alive(self,color):
        for row in self.__positions__:
            for piece in row:
                if isinstance(piece,King) and piece.__color__ == color:
                    return True
        return False

    def __str__(self):
        # Encabezado y pie con los números de las columnas espaciados
        header_footer = "    " + "   ".join(str(i) for i in range(8)) + "\n"
        board_str = header_footer
        board_str += "  +" + "---+" * 8 + "\n"  # Línea superior del tablero
        
        # Construir el tablero con las piezas y las casillas vacías
        for i, row in enumerate(self.__positions__):
            board_str += f"{i} |"  # Añadir el número de fila al inicio
            for cell in row:
                if cell is None:
                    board_str += "   |"  # Representación de casilla vacía
                else:
                    board_str += f" {str(cell)} |"  # Representación de la pieza
            board_str += f" {i}\n"  # Añadir el número de fila al final
            board_str += "  +" + "---+" * 8 + "\n"  # Añadir la línea divisoria entre filas
        
        board_str += header_footer  # Añadir el pie con los números de las columnas
        return board_str


    # def __str__(self):
    #     header_footer = "  " + " ".join(str(i) for i in range(8)) + "\n"
    #     board_str = header_footer
    #     for i, row in enumerate(self.__positions__):
    #         board_str += str(i) + " "
    #         for cell in row:
    #             board_str += str(cell) + " " if cell is not None else ". "
    #         board_str += str(i) + "\n"
    #     board_str += header_footer
    #     return board_str