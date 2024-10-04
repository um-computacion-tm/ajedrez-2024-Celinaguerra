import unittest
from game.chess import Chess
from game.board import Board
from game.exceptions import InvalidMove, OutOfBoard, EmptyPosition, InvalidTurn, GameAlreadyEnded
from game.rook import Rook
from game.king import King

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()
        self.board = Board()

    def test_is_playing(self):
        chess = Chess()
        self.assertTrue(chess.is_playing())

    def test_change_turn(self):
        chess = Chess()
        self.assertEqual(chess.turn, "WHITE")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "BLACK")
        
        chess.change_turn()
        self.assertEqual(chess.turn, "WHITE")

    def test_out_of_board_raises_error(self):
        from_row, from_col, to_row, to_col = 9,9, 8, 8  # Coordenadas inválidas
        with self.assertRaises(OutOfBoard):
            self.chess.move(from_row, from_col, to_row, to_col)

    def test_no_piece_at_start_raises_error(self):
        from_row, from_col, to_row, to_col = 3, 3, 2, 2  # No hay pieza en la posición inicial
        with self.assertRaises(EmptyPosition):
            self.chess.move(from_row, from_col, to_row, to_col)

    def test_invalid_turn(self):
        with self.assertRaises(InvalidTurn):
            self.chess.move(0,0,2,0)

    def test_invalid_move(self):
        Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, Rook("WHITE",Board(for_test=True)))
        with self.assertRaises(InvalidMove):
            self.chess.move(0,0,1,1)

    def test_change_turns_2(self):
        Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, Rook("WHITE",Board(for_test=True)))
        self.chess.move(0,0,1,0)
        self.assertEqual(self.chess.turn, "BLACK")

    def test_end_game(self):
        chess = Chess()
        self.assertTrue(chess.is_playing())
        chess.end_game()
        self.assertFalse(chess.is_playing())
    
    def test_game_already_ended(self):
        chess = Chess()
        chess.end_game()
        with self.assertRaises(GameAlreadyEnded):
            chess.move(0,0,1,0)

    def test_white_wins_by_capturing_black_king(self):
        Board(for_test=True)
        self.chess.__board__.set_piece(0, 0, King("BLACK", Board(for_test=True)))
        self.chess.__board__.set_piece(7, 0, Rook("WHITE", Board(for_test=True)))
        
        result = self.chess.move(7, 0, 0, 0)
        result = self.chess.change_turn()
        result = self.chess.move(0, 0, 0, 4)

        self.assertTrue(self.chess.__game_over__, "El juego debería haber terminado porque el rey negro fue capturado")

if __name__ == '__main__':
    unittest.main()
