import unittest
from game.piece import Piece
from game.board import Board

class TestPiece(unittest.TestCase):
    def test_SetUp(self):
        board = Board()
        piece = Piece("WHITE",board)
        self.assertEqual(piece.__color__,"WHITE")
        self.assertEqual(piece.__board__,board)

    def test_get_color(self):
        board = Board()
        piece = Piece("WHITE",board)
        self.assertEqual(piece.get_color(),"WHITE")

if __name__ == '__main__':
    unittest.main()