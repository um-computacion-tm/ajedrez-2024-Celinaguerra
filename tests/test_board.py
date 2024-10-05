import unittest
from game.board import Board
from game.rook import Rook
from game.bishop import Bishop
from game.king import King
from game.knight import Knight
from game.queen import Queen
from game.pawn import Pawn
from game.exceptions import *

class TestBoard(unittest.TestCase):
    def test_initial_positions_rook(self):
        board = Board()
        self.assertIsInstance(board.get_piece(0, 0), Rook)        
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertIsInstance(board.get_piece(7, 7), Rook)

    def test_empty_positions(self):   ### luego de añadir otras piezas va a dar error
        board = Board()
        for row in range(8):
            for col in range(8):
                if (row, col) not in [(0, 0), (0, 7), (7, 0), (7, 7), (1, 0), (1, 1), (1, 2), (1, 3), 
                                    (1, 4), (1, 5), (1, 6), (1, 7), (6, 0), (6, 1), (6, 2), 
                                    (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 1), (7, 2),
                                    (7, 3), (7, 4), (7, 5), (7, 6), (0, 1), (0, 2), (0, 3), 
                                    (0, 4), (0, 5), (0, 6)]:
                    self.assertIsNone(board.get_piece(row, col))

    def test_move_piece(self):
        board = Board()
        board.move(0, 0, 0, 1)
        self.assertIsInstance(board.get_piece(0, 1), Rook)
        self.assertIsNone(board.get_piece(0, 0))

        board.move(0, 1, 1, 1)
        self.assertIsInstance(board.get_piece(1, 1), Rook)
        self.assertIsNone(board.get_piece(0, 1))

    def test_move_piece_no_piece(self):
        board = Board()
        # Mover una pieza desde una posición inicial válida a otra posición válida
        try:
            board.move(0, 0, 0, 1)
            self.assertIsInstance(board.get_piece(0, 1), Rook)
            self.assertIsNone(board.get_piece(0, 0))
        except InvalidMove as e:
            self.fail(f"move_piece() raised InvalidMoveError unexpectedly! {e}")

    # def test_str_board(self):
    #     board = Board()
    #     self.assertEqual(
    #         str(board),
    #         (
    #             "  0 1 2 3 4 5 6 7\n"
    #             "0 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 0\n"
    #             "1 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 1\n"
    #             "2 . . . . . . . . 2\n"
    #             "3 . . . . . . . . 3\n"
    #             "4 . . . . . . . . 4\n"
    #             "5 . . . . . . . . 5\n"
    #             "6 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 6\n"
    #             "7 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 7\n"
    #             "  0 1 2 3 4 5 6 7\n"
    #         )
    #     )

    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "    0   1   2   3   4   5   6   7\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "0 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ | 0\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "1 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | 1\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "2 |   |   |   |   |   |   |   |   | 2\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "3 |   |   |   |   |   |   |   |   | 3\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "4 |   |   |   |   |   |   |   |   | 4\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "5 |   |   |   |   |   |   |   |   | 5\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "6 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | 6\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "7 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ | 7\n"
                "  +---+---+---+---+---+---+---+---+\n"
                "    0   1   2   3   4   5   6   7\n"
            )
        )



    def test_promotion_queen_white(self):
        board = Board(for_test=True)
        pawn = Pawn('WHITE', board)
        board.set_piece(1, 0, pawn)  # Coloca el peón en la fila 1
        self.assertEqual(board.get_piece(1, 0), pawn)
        board.move(1, 0, 0, 0)  # Mueve el peón a la fila 0
        new_piece = board.get_piece(0, 0)
        self.assertIsInstance(new_piece, Queen)  # Verifica que la nueva pieza sea una reina
        self.assertEqual(new_piece.__color__, 'WHITE')  # Verifica que la reina sea blanca

    def test_promotion_queen_black(self):
        board = Board(for_test=True)
        pawn = Pawn('BLACK', board)
        board.set_piece(6, 0, pawn)  # Coloca el peón en la fila 6
        self.assertEqual(board.get_piece(6, 0), pawn)
        board.move(6, 0, 7, 0)  # Mueve el peón a la fila 7
        new_piece = board.get_piece(7, 0)
        self.assertIsInstance(new_piece, Queen)  # Verifica que la nueva pieza sea una reina
        self.assertEqual(new_piece.__color__, 'BLACK')  # Verifica que la reina sea negra

    def test_is_king_alive(self):
        board = Board()
        self.assertTrue(board.is_king_alive('WHITE'))
        self.assertTrue(board.is_king_alive('BLACK'))

        board = Board(for_test=False)
        self.assertTrue(board.is_king_alive('WHITE'))
        self.assertTrue(board.is_king_alive('BLACK'))

        board = Board(for_test=True)
        self.assertFalse(board.is_king_alive('WHITE'))
        self.assertFalse(board.is_king_alive('BLACK'))

if __name__ == "__main__":
    unittest.main()