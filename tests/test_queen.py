import unittest
from game.queen import Queen
from game.board import Board

class TestQueen(unittest.TestCase):
    def test_str_white(self):
        board = Board()
        queen = Queen('WHITE', board)
        self.assertEqual(str(queen), '♕')

    def test_move_vertical_desc(self):
        board = Board( for_test= True)
        queen = Queen('WHITE', board)
        possibles = queen.orth_possible_positions(4,1,1,0)
        self.assertEqual(possibles, [(5,1),(6,1),(7,1)])

    def test_move_vertical_asc(self):
        board = Board(for_test= True)
        queen = Queen('WHITE', board)
        possibles = queen.orth_possible_positions(4,1,-1,0)
        self.assertEqual(possibles, [(3,1),(2,1),(1,1),(0,1)])

    def test_move_horizontal_right(self):
        board = Board()
        queen = Queen('WHITE', board)
        possibles = queen.orth_possible_positions(4,4,0,1)
        self.assertEqual(possibles, [(4,5),(4,6),(4,7)])

    def test_move_horizontal_left(self):
        board = Board()
        queen = Queen('WHITE', board)
        possibles = queen.orth_possible_positions(4,4,0,-1)
        self.assertEqual(possibles, [(4,3),(4,2),(4,1),(4,0)])

    def test_move_general(self):
        board = Board()
        queen = Queen('WHITE', board)
        possibles = queen.valid_positions(4,4,4,0)
        self.assertEqual(possibles, True)