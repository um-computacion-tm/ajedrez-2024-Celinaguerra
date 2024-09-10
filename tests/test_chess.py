import unittest
from game.chess import Chess
from game.board import Board
from game.exceptions import InvalidMove, OutOfBoard, EmptyPosition

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        self.board = Board()

    def test_is_playing(self):
        chess = Chess()
        self.assertTrue(chess.is_playing())

    # def test_move(self):
    #     chess = Chess()
    #     self.assertEqual(chess.turn, "WHITE")
    #     initial_piece = chess.__board__.get_piece(7, 7)
    #     chess.move(7, 7, , 0)
    #     moved_piece = chess.__board__.get_piece(1, 0)
    #     self.assertEqual(moved_piece, initial_piece)
    #     self.assertIsNone(chess.__board__.get_piece(0, 0))
    #     self.assertEqual(chess.turn, "BLACK")

    def test_change_turn(self):
        chess = Chess()
        self.assertEqual(chess.turn, "WHITE")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "BLACK")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "WHITE")

    def test_invalid_move_raises_error(self):
        from_row, from_col, to_row, to_col = 9,9, 8, 8  # Coordenadas inválidas
        with self.assertRaises(OutOfBoard):
            self.chess.move(from_row, from_col, to_row, to_col)

    def test_no_piece_at_start_raises_error(self):
        from_row, from_col, to_row, to_col = 3, 3, 2, 2  # No hay pieza en la posición inicial
        with self.assertRaises(EmptyPosition):
            self.chess.move(from_row, from_col, to_row, to_col)

if __name__ == '__main__':
    unittest.main()
