import unittest
from game.king import King
from game.board import Board  
from game.pawn import Pawn  


class TestKing(unittest.TestCase):
    def test_move_correct_position(self):
        board = Board(for_test=True)
        king = King('WHITE', board)
        possibles = king.get_possible_positions(4,4)
        self.assertEqual(possibles, [(5,4),(3,4),(4,5),(4,3),(5,5),(3,5),(5,3),(3,3)])
    
    def test_move_other_color_piece(self):
        board = Board(for_test=True)
        king = King('WHITE', board)
        pawn = Pawn('BLACK', board)
        board.set_piece(5,5, pawn)
        possibles = king.get_possible_positions(4,4)
        self.assertEqual(possibles, [(5,4),(3,4),(4,5),(4,3),(5,5),(3,5),(5,3),(3,3)])

    def test_move_same_color_piece(self):
        board = Board(for_test=True)
        king = King('WHITE', board)
        pawn = Pawn('WHITE', board)
        board.set_piece(5,5, pawn)
        possibles = king.get_possible_positions(4,4)
        self.assertEqual(possibles, [(5,4),(3,4),(4,5),(4,3),(3,5),(5,3),(3,3)])

if __name__ == '__main__':
    unittest.main()