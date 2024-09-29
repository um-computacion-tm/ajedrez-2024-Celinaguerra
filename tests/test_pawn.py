import unittest
from game.board import Board
from game.knight import Knight
from game.pawn import Pawn
from game.queen import Queen

class TestPawn(unittest.TestCase):
    def test_white_random_move(self):
        board = Board(for_test=True)
        pawn = Pawn('WHITE', board)
        possibles = pawn.get_possible_positions(4, 4)
        expected_positions = [(3, 4)]
        self.assertEqual(possibles, expected_positions)

    def test_white_initial_move(self):
        board = Board(for_test=True)
        pawn = Pawn('WHITE', board)
        possibles = pawn.get_possible_positions(6, 0)
        expected_positions = [(5, 0),(4, 0)]
        self.assertEqual(possibles, expected_positions)

    def test_move_eating(self):
        board = Board(for_test=True)
        pawn = Pawn('WHITE', board)
        knight = Knight('BLACK', board)
        board.set_piece(4, 1, knight)
        possibles = pawn.get_possible_positions(5, 0)
        expected_positions = [(4, 0), (4, 1)]
        self.assertEqual(possibles, expected_positions)

    def test_black_initial_move(self):
        board = Board(for_test=True)
        pawn = Pawn('BLACK', board)
        possibles = pawn.get_possible_positions(1, 0)
        expected_positions = [(2, 0),(3, 0)]
        self.assertEqual(possibles, expected_positions)

    def test_black_not_initial_move(self):
        board = Board(for_test=True)
        pawn = Pawn('BLACK', board)
        possibles = pawn.get_possible_positions(5, 0)
        expected_positions = [(6, 0)]
        self.assertEqual(possibles, expected_positions)

    def test_move_same_color_eating(self):
        board = Board(for_test=True)
        pawn = Pawn('WHITE', board)
        knight = Knight('WHITE', board)
        board.set_piece(4, 1, knight)
        possibles = pawn.get_possible_positions(5, 0)
        expected_positions = [(4, 0)]
        self.assertEqual(possibles, expected_positions)

    def test_promotion_queen_white(self):
        board = Board(for_test=True)
        pawn = Pawn('WHITE', board)
        board.set_piece(1,0, pawn) 
        self.assertEqual(board.get_piece(1, 0), pawn)
        board.move(1, 0, 0, 0) 
        new_piece = board.get_piece(0, 0)
        self.assertIsInstance(new_piece, Queen)  
        self.assertEqual(new_piece.color, 'WHITE')

    def test_promotion_queen_black(self):
        board = Board(for_test=True)
        pawn = Pawn('BLACK', board)
        board.set_piece(6,0, pawn) 
        self.assertEqual(board.get_piece(6, 0), pawn)
        board.move(6, 0, 7, 0) 
        new_piece = board.get_piece(7, 0)
        self.assertIsInstance(new_piece, Queen) 
        self.assertEqual(new_piece.color, 'BLACK')