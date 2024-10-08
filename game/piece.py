class Piece:
    def __init__(self, color, board):
        """
        Initializes a new instance of the Piece class.

        Args:
            color (str): The color of the piece.
            board (Board): The board on which the piece is placed.
        """
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        """
        Returns a string representation of the piece based on its color.

        If the piece's color is 'WHITE', it returns the string representation for a white piece.
        Otherwise, it returns the string representation for a black piece.

        Returns:
            str: The string representation of the piece.
        """
        if self.__color__ == 'WHITE':
            return self.white_str
        else:
            return self.black_str 

    def get_color(self):
        """
        Returns the color of the chess piece.

        Returns:
            str: The color of the piece.
        """
        return self.__color__

    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        """
        Determine if the target position is a valid move for a piece.

        Args:
            from_row (int): The starting row position of the piece.
            from_col (int): The starting column position of the piece.
            to_row (int): The target row position to move the piece to.
            to_col (int): The target column position to move the piece to.

        Returns:
            bool: True if the target position is a valid move, False otherwise.
        """
        possible_positions = self.get_possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_positions(self, from_row, from_col, directions):
        """
        Calculate possible positions for a piece based on given directions.

        Args:
            from_row (int): The starting row position of the piece.
            from_col (int): The starting column position of the piece.
            directions (list of tuple): A list of tuples where each tuple contains
                                        the row and column step directions.

        Returns:
            list: A list of possible positions (tuples) that the piece can move to.
        """
        possibles = []
        for row_step, col_step in directions:
            next_row, next_col = from_row + row_step, from_col + col_step
            self.in_board_and_color_validation(possibles, next_row, next_col, row_step, col_step)
        return possibles

    def possible_orthogonal_positions(self, from_row, from_col):
        """
        Calculate all possible orthogonal positions for a piece from a given starting position.

        This method considers the four orthogonal directions (up, down, left, right) and 
        returns all valid positions that the piece can move to from the specified starting 
        row and column.

        Args:
            from_row (int): The starting row position of the piece.
            from_col (int): The starting column position of the piece.

        Returns:
            list: A list of tuples, where each tuple represents a valid orthogonal position 
            (row, column) that the piece can move to.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Ortogonales
        return self.possible_positions(from_row, from_col, directions)

# ############################################### DIAGONAL

    def possible_diagonal_positions(self, from_row, from_col):
        """
        Calculate all possible diagonal positions from a given starting position.

        This method computes the possible diagonal moves for a piece on a chessboard
        from a specified starting row and column. It considers all four diagonal 
        directions: descending right, ascending right, descending left, and ascending left.

        Args:
            from_row (int): The starting row position of the piece.
            from_col (int): The starting column position of the piece.

        Returns:
            list: A list of tuples, where each tuple represents a possible position 
            (row, column) that the piece can move to diagonally.
        """
        return (
            self.diag_possible_positions(from_row, from_col, 1, 1) +  # diagonal descendente derecha
            self.diag_possible_positions(from_row, from_col, -1, 1) +  # diagonal ascendente derecha
            self.diag_possible_positions(from_row, from_col, 1, -1) +  # diagonal descendente izquierda
            self.diag_possible_positions(from_row, from_col, -1, -1)  # diagonal ascendente izquierda
        )

    def diag_possible_positions(self, row, col, row_step, col_step):
        """
        Calculate possible diagonal positions for a piece on the board.

        This method generates a list of possible positions a piece can move to
        diagonally from a given starting position, considering the step increments
        for rows and columns.

        Args:
            row (int): The starting row position of the piece.
            col (int): The starting column position of the piece.
            row_step (int): The step increment for the row direction.
            col_step (int): The step increment for the column direction.

        Returns:
            list: A list of possible positions (tuples) the piece can move to diagonally.
        """
        possibles = []
        next_row, next_col = row + row_step, col + col_step
        self.in_board_and_color_validation(possibles, next_row, next_col, row_step, col_step)
        return possibles

# ############################################### VERIFICACION

    def in_board_and_color_validation(self, possibles, next_row, next_col, row_step, col_step):
        """
        Validates the positions on the board and appends valid moves to the possibles list.

        This method checks if the given positions (next_row, next_col) are within the bounds of the board.
        It iterates through the board in the direction specified by row_step and col_step, and appends valid
        positions to the possibles list. A position is considered valid if it is within the board boundaries
        and either empty or occupied by an opponent's piece.

        Args:
            possibles (list): A list to which valid positions will be appended.
            next_row (int): The starting row position for validation.
            next_col (int): The starting column position for validation.
            row_step (int): The step increment for the row direction.
            col_step (int): The step increment for the column direction.
        """
        while 0 <= next_row < 8 and 0 <= next_col < 8:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row += row_step
            next_col += col_step