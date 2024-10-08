from game.chess import Chess
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)


def play(chess):
    try:
        print("-------------------- CHESS --------------------" + "\n")
        print(chess.show_board())
        print("turn: ", chess.turn)

        draw = input(f'{chess.turn.capitalize()}, Do you wish to draw? Enter "y" to propose, else any key: ').strip().lower()
        if draw == 'y':
            opponent = 'WHITE' if chess.turn == 'BLACK' else 'BLACK'
            confirm_surrender = input(f'{opponent}, {chess.turn} wants to draw. Do you accept the draw? (y/n): ').strip().lower()
            if confirm_surrender == 'y':
                print(f'The game has ended in a draw. Thanks for playing!')
                chess.end_game()
                return
            else:
                print(f'{opponent} rejected the draw. Continue playing.')

        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        # :)
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
        if not chess.validate_opponent_king_alive():
            print(f'El jugador {chess.__turn__} ha ganado!')
            print('Muchas gracias por jugar!')
            chess.end_game()
            return
        chess.change_turn()

    except InvalidMove as e:
        print(e.message)
    except Exception as e:
        print("Ocurrió un error inesperado, por favor inténtelo de nuevo.")



if __name__ == '__main__':
    main()