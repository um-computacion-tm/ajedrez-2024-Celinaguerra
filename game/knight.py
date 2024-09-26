from game.piece import Piece

class Knight(Piece):
    white_str = '♘'
    black_str = '♞'

    def get_possible_positions(self, from_row, from_col):
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



# from game.piece import Piece

# class Knight(Piece):
#     white_str = '♘'
#     black_str = '♞'

#     def get_possible_positions(self, from_row, from_col):
#         moves = [
#             (2, 1), (2, -1), (-2, 1), (-2, -1),
#             (1, 2), (1, -2), (-1, 2), (-1, -2)
#         ]
        
#         possible_positions = []
        
#         for move in moves:
#             new_row = from_row + move[0]
#             new_col = from_col + move[1]
            
#             # Verificar que la nueva posición esté dentro del tablero
#             if 0 <= new_row < 8 and 0 <= new_col < 8:
#                 possible_positions.append((new_row, new_col))
        
#         return possible_positions