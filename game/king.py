from game.piece import Piece

class King(Piece):
    white_str = '♔'
    black_str = '♚'

    def get_possible_positions(self, from_row, from_col):
        """
        Calculate all possible positions a king can move to from a given position.

        The king can move one square in any direction: horizontally, vertically, or diagonally.

        Args:
            from_row (int): The row index of the king's current position.
            from_col (int): The column index of the king's current position.

        Returns:
            list of tuple: A list of tuples where each tuple represents a possible position 
            (row, col) the king can move to.
        """
        possibles = self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )
        possible_king = []
        for (possible_row, possible_col) in possibles:
            if (
                abs(from_row - possible_row) <= 1 and
                abs(from_col - possible_col) <= 1
            ):
                possible_king.append((possible_row, possible_col))
        return possible_king

