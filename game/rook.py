from game.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return '♖' if self.__color__ == 'WHITE' else '♜'

    def can_move(self, start, end, board):
        start_x, start_y = start
        end_x, end_y = end

        # Movimiento en línea recta horizontal o vertical
        if start_x != end_x and start_y != end_y:
            return False

        # Verificar que no haya piezas en el camino
        if start_x == end_x:  # Movimiento vertical
            step = 1 if start_y < end_y else -1
            for y in range(start_y + step, end_y, step):
                if board[start_x][y] is not None:
                    return False
        else:  # Movimiento horizontal
            step = 1 if start_x < end_x else -1
            for x in range(start_x + step, end_x, step):
                if board[x][start_y] is not None:
                    return False

        # Verificar que la posición final no tenga una pieza del mismo color
        if board[end_x][end_y] is not None and board[end_x][end_y].color == self.color:
            return False

        return True