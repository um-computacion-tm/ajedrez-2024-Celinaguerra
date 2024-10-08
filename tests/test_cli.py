import unittest
from unittest.mock import patch, MagicMock
from game.chess import Chess
from game.board import Board
from game.king import King
from game.rook import Rook
from game.cli import play
from game.exceptions import *


class TestCli(unittest.TestCase):


    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['n','0', '1', '0', '0'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    @patch.object(Chess, 'validate_opponent_king_alive', return_value=False)
    def test_game_ends_by_eating_king(
        self,
        mock_validate_opponent_king_alive,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertTrue(chess.__game_over__)        
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 5)
        self.assertEqual(mock_chess_move.call_count, 1)
        self.assertEqual(mock_validate_opponent_king_alive.call_count, 1)


    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['n','6', '0', '4', '0'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)

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

if __name__ == '__main__':
    unittest.main()