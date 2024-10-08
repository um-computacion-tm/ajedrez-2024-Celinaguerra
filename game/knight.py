from game.piece import Piece

class Knight(Piece):
    white_str = '♘'
    black_str = '♞'

    def get_possible_positions(self, from_row, from_col):
        """
        Calculate all possible positions a knight can move to from a given position.
        The knight moves in an "L" shape: two squares in one direction and then one square perpendicular, 
        or one square in one direction and then two squares perpendicular.
        Args:
            from_row (int): The row index of the knight's current position.
            from_col (int): The column index of the knight's current position.
        Returns:
            list of tuple: A list of tuples where each tuple represents a valid position (row, col) 
            the knight can move to. The position is valid if it is within the bounds of the board 
            and either empty or occupied by an opponent's piece.
        """
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        possible_positions = []
        board = self.__board__
        color = self.get_color()
        
        for move in moves:
            new_row = from_row + move[0]
            new_col = from_col + move[1]
            
            # Verificar que la nueva posición esté dentro del tablero
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.get_piece(new_row, new_col)
                # Verificar que no haya una pieza del mismo color en la nueva posición
                if piece is None or piece.get_color() != color:
                    possible_positions.append((new_row, new_col))
        
        return possible_positions