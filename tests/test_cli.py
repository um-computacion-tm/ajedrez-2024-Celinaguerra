import unittest
from unittest.mock import patch, MagicMock
from game.chess import Chess
from game.cli import play
from game.exceptions import *


class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['y', 'y'])  # Simulamos propuesta de empate y aceptación
    @patch('game.chess.Chess.end_game')
    def test_draw_accepted(self, mock_end_game, mock_input):
        chess = Chess()
        chess.is_playing = MagicMock(return_value=True)
        chess.__turn__ = 'BLACK'
        chess.show_board = MagicMock(return_value="board")
        
        with patch('builtins.print') as mock_print:
            play(chess)
        mock_end_game.assert_called_once()
        mock_print.assert_any_call('The game has ended in a draw. Thanks for playing!')

    @patch('builtins.input', side_effect=['y', 'n'])  # Simulamos propuesta de empate y rechazo
    def test_draw_rejected(self, mock_input):
        chess = Chess()
        chess.is_playing = MagicMock(return_value=True)
        chess.__turn__ = 'WHITE'
        chess.show_board = MagicMock(return_value="board")
        
        with patch('builtins.print') as mock_print:
            play(chess)
        mock_print.assert_any_call('BLACK rejected the draw. Continue playing.')


    # @patch('builtins.input', side_effect=['6', '0', '4', '0'])  # Simulamos movimiento válido
    # @patch('game.chess.Chess.move')
    # def test_move_called_with_correct_arguments(self, mock_move, mock_input):
    #     chess = Chess()
    #     chess.is_playing = MagicMock(return_value=True)
    #     chess.__turn__ = 'WHITE'
    #     chess.show_board = MagicMock(return_value="board")
        
    #     with patch('builtins.print'):
    #         play(chess)
    #     mock_move.assert_called_with(6, 0, 4, 0)


if __name__ == '__main__':
    unittest.main()



# class TestCli(unittest.TestCase):
#     @patch(  # este patch controla lo que hace el input
#         'builtins.input',
#         side_effect=['1', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
#     )
#     @patch('builtins.print') # este patch controla lo que hace el print
#     @patch.object(Chess, 'move')
#     def test_happy_path(
#         self,
#         mock_chess_move,
#         mock_print,
#         mock_input,
#     ): #
#         chess = Chess()
#         play(chess)
#         self.assertEqual(mock_input.call_count, 4)
#         self.assertEqual(mock_print.call_count, 2)
#         self.assertEqual(mock_chess_move.call_count, 1)




    # @patch(  # este patch controla lo que hace el input
    #     'builtins.input',
    #     side_effect=['hola', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    # )
    # @patch('builtins.print') # este patch controla lo que hace el print
    # @patch.object(Chess, 'move')
    # def test_not_happy_path(
    #     self,
    #     mock_chess_move,
    #     mock_print,
    #     mock_input,
    # ): #
    #     chess = Chess()
    #     play(chess)
    #     self.assertEqual(mock_input.call_count, 1)
    #     self.assertEqual(mock_print.call_count, 3)
    #     self.assertEqual(mock_chess_move.call_count, 0)

    # @patch(  # este patch controla lo que hace el input
    #     'builtins.input',
    #     side_effect=['1', '1', '2', 'hola'], # estos son los valores que simula lo que ingresaria el usuario
    # )
    # @patch('builtins.print') # este patch controla lo que hace el print
    # @patch.object(Chess, 'move')
    # def test_more_not_happy_path(
    #     self,
    #     mock_chess_move,
    #     mock_print,
    #     mock_input,
    # ): #
    #     chess = Chess()
    #     play(chess)
    #     self.assertEqual(mock_input.call_count, 4)
    #     self.assertEqual(mock_print.call_count, 3)
    #     self.assertEqual(mock_chess_move.call_count, 0)