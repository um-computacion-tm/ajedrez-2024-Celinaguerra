import unittest
from game.queen import Queen

class TestQueen(unittest.TestCase):
    def test_str_white(self):
        queen = Queen('WHITE')
        self.assertEqual(str(queen), '♕')

    def test_move_vertical_desc(self):
        queen = Queen('WHITE')
        #param
        #lugar de la torre
        #final de la torre
        #verificar
        possibles = queen.possible_positions_vd(4,1)
        self.assertEqual(possibles, [(5,1),(6,1),(7,1)])

    def test_move_vertical_asc(self):
        queen = Queen('WHITE')
        possibles = queen.possible_positions_va(4,1)
        self.assertEqual(possibles, [(3,1),(2,1),(1,1),(0,1)])

    def test_move_horizontal_right(self):
        queen = Queen('WHITE')
        possibles = queen.possible_positions_hr(4,4)
        self.assertEqual(possibles, [(4,5),(4,6),(4,7)])

    def test_move_horizontal_left(self):
        queen = Queen('WHITE')
        possibles = queen.possible_positions_hl(4,4)
        self.assertEqual(possibles, [(4,3),(4,2),(4,1),(4,0)])

    def test_move_general(self):
        queen = Queen('WHITE')
        possibles = queen.valid_positions(4,4,4,0)
        self.assertEqual(possibles, True)