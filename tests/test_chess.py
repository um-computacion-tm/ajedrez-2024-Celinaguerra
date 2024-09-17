import unittest
from game.chess import Chess
from game.board import Board
from game.exceptions import InvalidMove, OutOfBoard, EmptyPosition, InvalidTurn
from game.rook import Rook

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        self.board = Board()

    def test_is_playing(self):
        chess = Chess()
        self.assertTrue(chess.is_playing())

    def test_change_turn(self):
        chess = Chess()
        self.assertEqual(chess.turn, "WHITE")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "BLACK")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "WHITE")

    def test_out_of_board_raises_error(self):
        from_row, from_col, to_row, to_col = 9,9, 8, 8  # Coordenadas inválidas
        with self.assertRaises(OutOfBoard):
            self.chess.move(from_row, from_col, to_row, to_col)

    def test_no_piece_at_start_raises_error(self):
        from_row, from_col, to_row, to_col = 3, 3, 2, 2  # No hay pieza en la posición inicial
        with self.assertRaises(EmptyPosition):
            self.chess.move(from_row, from_col, to_row, to_col)

    def test_invalid_turn(self):
        with self.assertRaises(InvalidTurn):
            self.chess.move(0,0,2,0)

    def test_invalid_move(self):
        Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, Rook("WHITE",Board(for_test=True)))
        with self.assertRaises(InvalidMove):
            self.chess.move(0,0,1,1)

    def test_change_turns_2(self):
        Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, Rook("WHITE",Board(for_test=True)))
        self.chess.move(0,0,1,0)
        self.assertEqual(self.chess.turn, "BLACK")


if __name__ == '__main__':
    unittest.main()
