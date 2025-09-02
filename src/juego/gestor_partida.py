from src.juego.cacho import Cacho
from src.servicios.generador_aleatorio import GeneradorAleatorio


class GestorPartida:
    def __init__(self, num_jugadores: int):

        self.lista_cachos = [Cacho() for _ in range(num_jugadores)]
        self.cacho_actual = None
        self.direccion = None

    def determinar_cacho_inicial(self) -> Cacho:
        cachos_participantes = self.lista_cachos.copy()

        while True:  # hasta que no haya un ganador
            valores = [(cacho, GeneradorAleatorio.generar_valor_aleatorio()) for cacho in cachos_participantes]

            max_valor = max(valores, key=lambda x: x[1])[1]
            ganadores = [cacho for cacho, valor in valores if valor == max_valor]

            # si no hay empate
            if len(ganadores) == 1:
                self.cacho_actual = ganadores[0]
                return ganadores[0]

            # si hay empate (solo empatados siguen participando)
            cachos_participantes = ganadores
