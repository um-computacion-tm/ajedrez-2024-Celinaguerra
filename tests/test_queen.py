import unittest
from game.queen import Queen
from game.board import Board

class TestQueen(unittest.TestCase):
    def test_str_white(self):
        board = Board()
        queen = Queen('WHITE', board)
        self.assertEqual(str(queen), '♕')

    def test_move_general(self):
        board = Board()
        queen = Queen('WHITE', board)
        possibles = queen.valid_positions(4,4,4,0)
        self.assertEqual(possibles, True)