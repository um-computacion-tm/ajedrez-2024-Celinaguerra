from game.board import Board
from game.exceptions import EmptyPosition, InvalidMove, InvalidTurn, GameAlreadyEnded

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__game_over__ = False

    def is_playing(self):
        return not self.__game_over__

    def end_game(self):
        self.__game_over__ = True

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
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
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
