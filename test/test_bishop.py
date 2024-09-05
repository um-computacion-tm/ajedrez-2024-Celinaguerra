import unittest
from game.bishop import Bishop
from game.board import Board    

class TestBishop(unittest.TestCase):
    def test_str_white(self):
        board = Board()
        bishop = Bishop('WHITE', board)
        self.assertEqual(str(bishop), '♗')

    def test_move_diag_right_up(self):
        board = Board()
        bishop = Bishop('WHITE', board)
        possibles = bishop.possible_positions_ru(4,4)
        self.assertEqual(possibles, [(3,5),(2,6),(1,7)])

    def test_move_diag_right_down(self):
        board = Board()
        bishop = Bishop('WHITE', board)
        possibles = bishop.possible_positions_rd(4,4)
        self.assertEqual(possibles, [(5,5),(6,6),(7,7)])