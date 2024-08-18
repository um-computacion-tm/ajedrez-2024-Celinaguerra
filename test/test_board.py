import unittest
from game.board import Board, InvalidMoveError, InvalidCoordError
from game.rook import Rook


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

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
                if (row, col) not in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                    self.assertIsNone(board.get_piece(row, col))

    def test_move_piece(self):
        self.board.move_piece(0, 0, 0, 1)
        self.assertIsInstance(self.board.get_piece(0, 1), Rook)
        self.assertIsNone(self.board.get_piece(0, 0))

        self.board.move_piece(0, 1, 1, 1)
        self.assertIsInstance(self.board.get_piece(1, 1), Rook)
        self.assertIsNone(self.board.get_piece(0, 1))

    def test_move_piece_no_piece(self):
        # Mover una pieza desde una posición inicial válida a otra posición válida
        try:
            self.board.move_piece(0, 0, 0, 1)
            self.assertIsInstance(self.board.get_piece(0, 1), Rook)
            self.assertIsNone(self.board.get_piece(0, 0))
        except InvalidMoveError as e:
            self.fail(f"move_piece() raised InvalidMoveError unexpectedly! {e}")

        # Mover la misma pieza a otra posición
        try:
            self.board.move_piece(0, 1, 1, 1)
            self.assertIsInstance(self.board.get_piece(1, 1), Rook)
            self.assertIsNone(self.board.get_piece(0, 1))
        except InvalidMoveError as e:
            self.fail(f"move_piece() raised InvalidMoveError unexpectedly! {e}")

    def test_invalid_move_no_piece(self):
        # Intentar mover una pieza desde una posición vacía debería lanzar InvalidMoveError
        with self.assertRaises(InvalidMoveError):
            self.board.move_piece(3, 3, 4, 4)  # No hay pieza en (3, 3)

    def test_invalid_move_out_of_bounds(self):
        # Intentar mover una pieza fuera de los límites debería lanzar InvalidMoveError
        with self.assertRaises(InvalidCoordError):
            self.board.move_piece(0, 0, -1, 0)  # Movimiento fuera de los límites
        
        with self.assertRaises(InvalidCoordError):
            self.board.move_piece(0, 0, 0, 8) 
