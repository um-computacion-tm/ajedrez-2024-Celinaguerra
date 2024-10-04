class InvalidMove(Exception):
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

class GameAlreadyEnded(Exception):
    message = "El juego ya ha terminado"
    def __str__(self):
        return self.message