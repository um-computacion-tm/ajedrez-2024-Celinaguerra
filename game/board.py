from game.rook import Rook
from game.pawn import Pawn 
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.knight import Knight 
from game.exceptions import OutOfBoard


class Board:
    def __init__(self, for_test = False):
        """
        Initializes the chess board with pieces in their starting positions.

        Parameters:
        for_test (bool): If True, the board is initialized empty for testing purposes. 
        If False, the board is initialized with pieces in their standard starting positions.

        Attributes:
        __positions__ (list): A 2D list representing the board, where each element is either None or a chess piece object.
        """
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

    def validate_position_in_board(self, row, col):
        """
        Check if the specified position is within the bounds of the chess board.

        Args:
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if the position is within the board, False otherwise.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def move(self, from_row, from_col, to_row, to_col):
        """
        Moves a piece from one position to another on the board.

        Parameters:
        from_row (int): The row index of the piece's current position.
        from_col (int): The column index of the piece's current position.
        to_row (int): The row index of the piece's destination position.
        to_col (int): The column index of the piece's destination position.

        If the piece being moved is a Pawn and it reaches the opposite end of the board
        (row 0 for white, row 7 for black), it is promoted to a Queen.
        """
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

        if isinstance(origin, Pawn) and (to_row == 0 or to_row == 7):
            self.set_piece(to_row, to_col, Queen(origin.__color__, self))

    def get_piece(self, row, col):
        """
        Retrieve the piece at the specified board position.

        Args:
            row (int): The row index of the board (0-7).
            col (int): The column index of the board (0-7).

        Returns:
            Piece: The piece located at the specified position, or None if the position is empty.

        Raises:
            OutOfBoard: If the specified position is outside the valid board range.
        """
        if not self.validate_position_in_board(row, col):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        """
        Places a piece on the board at the specified row and column.

        Args:
            row (int): The row index where the piece will be placed.
            col (int): The column index where the piece will be placed.
            piece (Piece): The piece to be placed on the board.
        """
        self.__positions__[row][col] = piece

    def is_king_alive(self,color):
        """
        Check if the king of the specified color is still alive on the board.

        Args:
            color (str): The color of the king to check for (e.g., 'white' or 'black').

        Returns:
            bool: True if the king of the specified color is found on the board, False otherwise.
        """
        for row in self.__positions__:
            for piece in row:
                if isinstance(piece,King) and piece.__color__ == color:
                    return True
        return False

    def __str__(self):
        """
        Returns a string representation of the chess board.
        The board is displayed with column numbers at the top and bottom, and row numbers
        at the beginning and end of each row. Each cell is represented by either a piece
        or an empty space.
        Returns:
            str: The string representation of the chess board.
        """
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
