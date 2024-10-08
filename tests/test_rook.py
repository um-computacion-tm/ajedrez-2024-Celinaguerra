import unittest
from game.rook import Rook
from game.board import Board
from game.pawn import Pawn


class TestRook(unittest.TestCase):
    def test_str_white(self):
        board = Board()
        rook = Rook('WHITE',board)
        self.assertEqual(str(rook), '♖')

    def test_move_general(self):
        board = Board(for_test=True)
        rook = Rook('WHITE',board)
        possibles = rook.get_possible_positions(4,4)
        self.assertEqual(possibles, [(5,4),(6,4),(7,4),(3,4),(2,4),(1,4),(0,4),(4,5),(4,6),(4,7),(4,3),(4,2),(4,1),(4,0)])

    def test_move_diagonal_desc(self):
        board = Board()
        rook = board.get_piece(col=0, row=0)
        is_possible = rook.get_possible_positions(
            from_row=0,
            from_col=0,
        )

        self.assertFalse(is_possible)