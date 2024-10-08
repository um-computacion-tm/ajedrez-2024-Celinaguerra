from game.piece import Piece

class Rook(Piece):

    white_str = '♖'
    black_str = '♜'

    def __str__(self):
        """
        Returns the string representation of the Rook piece based on its color.

        If the Rook piece is white, it returns the string representation for a white Rook.
        Otherwise, it returns the string representation for a black Rook.

        Returns:
            str: The string representation of the Rook piece.
        """
        if self.__color__ == 'WHITE':
            return self.white_str
        else:
            return self.black_str 

    def get_possible_positions(self, from_row, from_col):
        """
        Calculate all possible positions for a rook from a given starting position.

        This method determines all the valid orthogonal moves (horizontal and vertical)
        that a rook can make from the specified starting position on the chessboard.

        Args:
            from_row (int): The starting row position of the rook.
            from_col (int): The starting column position of the rook.

        Returns:
            list: A list of tuples, where each tuple represents a valid position (row, col)
            that the rook can move to from the starting position.
        """
        return self.possible_orthogonal_positions(from_row, from_col)