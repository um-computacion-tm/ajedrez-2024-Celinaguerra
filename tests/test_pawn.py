import unittest
from game.board import Board
from game.knight import Knight
from game.pawn import Pawn

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


