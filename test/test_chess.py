import unittest
from game.chess import Chess
from game.board import Board, InvalidMoveError, InvalidCoordError

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        self.board = Board()

    def test_move_calls_board_methods(self):
        from_row, from_col, to_row, to_col = 0, 0, 1, 1
        self.board.move_piece(0, 0, 0, 0)  # Asegúrate de que haya una pieza en la posición inicial
        self.chess.move(from_row, from_col, to_row, to_col)
        
        # Verifica que la pieza se haya movido correctamente
        piece = self.board.get_piece(to_row, to_col)
        self.assertIsNotNone(piece)
        self.assertEqual(piece.__class__.__name__, 'Rook')
        self.assertIsNone(self.board.get_piece(from_row, from_col))

    def test_invalid_move_raises_error(self):
        from_row, from_col, to_row, to_col = 0, 0, 8, 8  # Coordenadas inválidas
        with self.assertRaises(InvalidCoordError):
            self.chess.move(from_row, from_col, to_row, to_col)

    def test_no_piece_at_start_raises_error(self):
        from_row, from_col, to_row, to_col = 1, 1, 2, 2  # No hay pieza en la posición inicial
        with self.assertRaises(InvalidMoveError):
            self.chess.move(from_row, from_col, to_row, to_col)

if __name__ == '__main__':
    unittest.main()
