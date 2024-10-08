from game.piece import Piece

class Pawn(Piece):
    white_str = '♙'
    black_str = '♟'

    def get_possible_positions(self, from_row, from_col):
        """
        Calculate all possible positions a pawn can move to from a given position.

        This method combines the possible move positions and possible capture positions
        for a pawn located at the specified row and column.

        Args:
            from_row (int): The row index of the pawn's current position.
            from_col (int): The column index of the pawn's current position.

        Returns:
            list: A list of tuples representing the possible positions the pawn can move to.
        """
        possibles = self.get_possible_positions_move(
            from_row,
            from_col,
        )
        possibles.extend(
            self.get_possible_positions_eat(from_row, from_col)
        )
        return possibles

    def get_possible_positions_eat(self, from_row, from_col):
        """
        Calculate the possible positions where the pawn can move to capture an enemy piece.

        Args:
            from_row (int): The current row position of the pawn.
            from_col (int): The current column position of the pawn.

        Returns:
            list of tuple: A list of tuples representing the positions (row, column) where the pawn can capture an enemy piece.
        """
        direction = 1 if self.__color__ == "BLACK" else -1
        enemy_color = "WHITE" if self.__color__ == "BLACK" else "BLACK"
        positions = []

        for col_offset in [-1, 1]:
            new_col = from_col + col_offset
            if 0 <= new_col <= 7:  # Verificar que la nueva columna esté dentro del rango
                other_piece = self.__board__.get_piece(from_row + direction, new_col)
                if other_piece and other_piece.__color__ == enemy_color:
                    positions.append((from_row + direction, new_col))
        return positions

    def get_possible_positions_move(self, from_row, from_col):
        """
        Calculate the possible positions a pawn can move to from a given position.

        The pawn can move forward one square if the square is empty. If the pawn is 
        in its starting position, it can move forward two squares if both squares 
        are empty. If the pawn reaches the last row, it is promoted to a queen.

        Args:
            from_row (int): The row index of the pawn's current position.
            from_col (int): The column index of the pawn's current position.

        Returns:
            list of tuple: A list of tuples representing the possible positions 
            the pawn can move to. Each tuple contains the row and column indices 
            of a possible position.
        """
        direction = 1 if self.__color__ == "BLACK" else -1
        start_row = 1 if self.__color__ == "BLACK" else 6
        positions = []

        if self.__board__.get_piece(from_row + direction, from_col) is None:
            next_row = from_row + direction
            positions.append((next_row, from_col))
            if from_row == start_row and self.__board__.get_piece(from_row + 2 * direction, from_col) is None:
                positions.append((from_row + 2 * direction, from_col))
        return positions