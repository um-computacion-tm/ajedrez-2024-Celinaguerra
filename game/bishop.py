from game.piece import Piece

class Bishop(Piece):
    white_str = '♗'
    black_str = '♝'

    def get_possible_positions(self, from_row, from_col):
        """
        Calculate all possible diagonal positions for a bishop from a given starting position.

        Args:
            from_row (int): The starting row position of the bishop.
            from_col (int): The starting column position of the bishop.

        Returns:
            list: A list of tuples representing all possible diagonal positions the bishop can move to.
        """
        return self.possible_diagonal_positions(from_row,from_col)
