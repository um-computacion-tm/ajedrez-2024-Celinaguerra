import unittest
from game.board import Board
from game.rook import Rook


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_positions_rook(self):
        board = Board()
        self.assertIsInstance(board.get_piece(0, 0), Rook)        
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertIsInstance(board.get_piece(7, 7), Rook)

    def test_empty_positions(self):   ### luego de añadir otras piezas va a dar error
        board = Board()
        for row in range(8):
            for col in range(8):
                if (row, col) not in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                    self.assertIsNone(board.get_piece(row, col))

    def test_move_piece(self):
        self.board.move_piece(0, 0, 0, 1)
        self.assertIsInstance(self.board.get_piece(0, 1), Rook)
        self.assertIsNone(self.board.get_piece(0, 0))

        self.board.move_piece(0, 1, 1, 1)
        self.assertIsInstance(self.board.get_piece(1, 1), Rook)
        self.assertIsNone(self.board.get_piece(0, 1))

if __name__ == '__main__':
    unittest.main()