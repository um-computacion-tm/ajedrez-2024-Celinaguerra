from game.board import Board
from game.exceptions import EmptyPosition, InvalidMove, InvalidTurn, GameAlreadyEnded

class Chess:
    def __init__(self):
        """
        Initializes a new chess game.

        Attributes:
            __board__ (Board): The chess board for the game.
            __turn__ (str): The current turn, either "WHITE" or "BLACK".
            __game_over__ (bool): A flag indicating if the game is over.
        """
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__game_over__ = False

    def is_playing(self):
        """
        Check if the game is currently in progress.

        Returns:
            bool: True if the game is not over, False otherwise.
        """
        return not self.__game_over__

    def end_game(self):
        """
        Ends the current game by setting the game over flag to True.
        
        This method updates the internal state of the game to indicate that
        the game has ended. Once this method is called, the game is considered
        over and no further moves should be processed.
        """
        self.__game_over__ = True

    def move(self, from_row, from_col, to_row, to_col):
        """
        Moves a piece from one position to another on the chessboard.
        Args:
            from_row (int): The row index of the piece's current position.
            from_col (int): The column index of the piece's current position.
            to_row (int): The row index of the target position.
            to_col (int): The column index of the target position.
        Raises:
            GameAlreadyEnded: If the game has already ended.
            EmptyPosition: If there is no piece at the source position.
            InvalidTurn: If the piece at the source position does not belong to the current player.
            InvalidMove: If the move is not valid for the piece.
        """
        if self.__game_over__:
            raise GameAlreadyEnded()

        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        
        opponent_color = 'BLACK' if self.__turn__ == 'WHITE' else 'WHITE'
        if not self.__board__.is_king_alive(opponent_color):
            print(f'El jugador {self.__turn__} ha ganado!')
            print('Muchas gracias por jugar!')
            self.end_game()
        self.change_turn()

    @property
    def turn(self):
        """
        Returns the current turn of the chess game.

        Returns:
            str: The current turn color.
        """
        return self.__turn__

    def show_board(self):
        """
        Returns a string representation of the current state of the chess board.

        Returns:
            str: The string representation of the chess board.
        """
        return str(self.__board__)

    def change_turn(self):
        """
        Switches the current turn between "WHITE" and "BLACK".

        This method changes the value of the `__turn__` attribute. If the current
        turn is "WHITE", it sets it to "BLACK". If the current turn is "BLACK",
        it sets it to "WHITE".
        """
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def offer_draw(self):
        draw = input(f'{self.turn.capitalize()}, Do you wish to draw? Enter "y" to propose, else any key: ').strip().lower()
        if draw == 'y':
            opponent = 'WHITE' if self.turn == 'BLACK' else 'BLACK'
            confirm_surrender = input(f'{opponent}, {self.turn} wants to draw. Do you accept the draw? (y/n): ').strip().lower()
            if confirm_surrender == 'y':
                print(f'The game has ended in a draw. Thanks for playing!')
                self.end_game()
                return
            else:
                print(f'{opponent} rejected the draw. Continue playing.')