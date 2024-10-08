import unittest
from game.bishop import Bishop
from game.board import Board  
from game.pawn import Pawn  

class TestBishop(unittest.TestCase):
    def test_str_white(self):
        board = Board()
        bishop = Bishop('WHITE', board)
        self.assertEqual(str(bishop), '♗')


    def test_move_all_possible_positions(self):
        board = Board(for_test=True)
        bishop = Bishop('WHITE', board)
        possibles = bishop.get_possible_positions(4,4)
        self.assertEqual = (possibles, True)


    def test_move_other_color_piece(self):
        board = Board(for_test=True)
        bishop = Bishop('WHITE', board)
        pawn = Pawn('BLACK', board)
        board.set_piece(5,5, pawn)
        board.set_piece(1,1, bishop)
        possibles = bishop.get_possible_positions(1,1)
        self.assertEqual(possibles, [(2, 2), (3, 3), (4, 4), (5, 5), (0, 2), (2, 0), (0, 0)])