import unittest
from game.rook import Rook

class TestRook(unittest.TestCase):
    def test_str_white(self):
        rook = Rook('WHITE')
        self.assertEqual(str(rook), '♖')

    def test_move_vertical_desc(self):
        rook = Rook('WHITE')
        #param
        #lugar de la torre
        #final de la torre
        #verificar
        possibles = rook.possible_positions_vd(4,1)
        self.assertEqual(possibles, [(5,1),(6,1),(7,1)])

    def test_move_vertical_asc(self):
        rook = Rook('WHITE')
        possibles = rook.possible_positions_va(4,1)
        self.assertEqual(possibles, [(3,1),(2,1),(1,1),(0,1)])

    def test_move_horizontal_right(self):
        rook = Rook('WHITE')
        possibles = rook.possible_positions_hr(4,4)
        self.assertEqual(possibles, [(4,5),(4,6),(4,7)])