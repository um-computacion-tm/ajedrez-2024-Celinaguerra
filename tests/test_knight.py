import unittest
from game.piece import Piece
from game.board import Board
from game.knight import Knight
from game.pawn import Pawn

class TestKnight(unittest.TestCase):
    def test_any_move(self):
        board = Board(for_test=True)
        knight = Knight('WHITE', board)
        possibles = knight.get_possible_positions(4, 4)
        
        # Lista de posiciones posibles esperadas
        expected_positions = [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
        
        # Ahora compara la lista de posiciones con la esperada
        self.assertEqual(possibles, expected_positions)

    def test_any_move_other_piece(self):
        board = Board(for_test=True)
        knight = Knight('WHITE', board)
        pawn = Pawn('BLACK', board)
        board.set_piece(3, 6, pawn)
        possibles = knight.get_possible_positions(4, 4)
        
        # La lista debería incluir (3, 6) porque el peón es de otro color
        expected_positions = [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
        self.assertEqual(possibles, expected_positions)

    def test_any_move_same_piece(self):
        board = Board(for_test=True)
        knight = Knight('WHITE', board)
        pawn = Pawn('WHITE', board)
        board.set_piece(3, 6, pawn)
        possibles = knight.get_possible_positions(4, 4)
        
        # (3, 6) no debería estar en la lista porque el peón es del mismo color
        expected_positions = [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2), (3, 2)]
        self.assertEqual(possibles, expected_positions)

    def test_any_move_jump(self):
        board = Board(for_test=True)
        knight = Knight('WHITE', board)
        pawn = Pawn('WHITE', board)
        board.set_piece(3, 4, pawn)
        possibles = knight.get_possible_positions(4, 4)

        expected_positions = [(6, 5), (6, 3), (2, 5), (2, 3), (5, 6), (5, 2),(3,6), (3, 2)]
        self.assertEqual(possibles, expected_positions)

if __name__ == '__main__':
    unittest.main()
