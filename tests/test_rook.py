import unittest
from game.rook import Rook
from game.board import Board
from game.pawn import Pawn


class TestRook(unittest.TestCase):
    def test_str_white(self):
        board = Board()
        rook = Rook('WHITE',board)
        self.assertEqual(str(rook), '♖')

    def test_move_vertical_desc(self):
        board = Board(for_test=True)
        rook = Rook('WHITE',board)
        #param
        #lugar de la torre
        #final de la torre
        #verificar
        possibles = rook.possible_positions_vd(4,1)
        self.assertEqual(possibles, [(5,1),(6,1),(7,1)])

    def test_move_vertical_asc(self):
        board = Board(for_test=True)
        rook = Rook('WHITE',board)
        possibles = rook.possible_positions_va(4,2)
        self.assertEqual(possibles, [(3,2),(2,2),(1,2),(0,2)])

    def test_move_horizontal_right(self):
        board = Board(for_test=True)
        rook = Rook('WHITE',board)
        possibles = rook.possible_positions_hr(4,4)
        self.assertEqual(possibles, [(4,5),(4,6),(4,7)])

    def test_move_horizontal_left(self):
        board = Board(for_test=True)
        rook = Rook('WHITE',board)
        possibles = rook.possible_positions_hl(4,4)
        self.assertEqual(possibles, [(4,3),(4,2),(4,1),(4,0)])

    def test_move_general(self):
        board = Board()
        rook = Rook('WHITE',board)
        possibles = rook.valid_positions(4,4,4,0)
        self.assertEqual(possibles, True)

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_move_diagonal_desc(self):
        board = Board()
        rook = board.get_piece(col=0, row=0)
        is_possible = rook.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )

        self.assertFalse(is_possible)