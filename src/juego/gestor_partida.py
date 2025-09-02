from src.juego.cacho import Cacho


class GestorPartida:
    def __init__(self, num_jugadores: int):

        self.lista_cachos = [Cacho() for _ in range(num_jugadores)]
        self.cacho_actual = None
        self.direccion = None
