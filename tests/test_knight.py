import unittest
from game.piece import Piece
from game.board import Board
from game.knight import Knight

class TestPiece(unittest.TestCase):
    def test_any_move(self):
        board = Board(for_test=True)
        knight = Knight('WHITE', board)
        possibles = knight.get_possible_positions(4,4)
        self.assertEqual = (possibles, True)

if __name__ == '__main__':
    unittest.main()