from src.juego.cacho import Cacho
from src.servicios.generador_aleatorio import GeneradorAleatorio


class GestorPartida:
    def __init__(self, num_jugadores: int):
        self.lista_cachos = [Cacho() for _ in range(num_jugadores)]
        self.cacho_actual = None
        self.direccion = None
        self.apuesta_actual = (0, 0)
        self.ultimo_apostador = None
        self.iniciador_proxima_ronda = None
        self.estado_especial = False
        self.estado_especial_pendiente = False
        self.tipo_ronda_especial = None
        self.tipo_ronda_especial_pendiente = None
        self.cacho_que_obligo = None
        self.cachos_que_usaron_especial = set()

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

    def establecer_direccion(self, direccion: str) -> None:
        self.direccion = direccion

    def obtener_siguiente_cacho(self) -> Cacho:
        if self.direccion is None:
            self.direccion = "horario"
        
        indice_actual = self.lista_cachos.index(self.cacho_actual)
        num_cachos = len(self.lista_cachos)
        
        for _ in range(num_cachos):
            if self.direccion == "horario":
                indice_actual = (indice_actual + 1) % num_cachos
            else:
                indice_actual = (indice_actual - 1) % num_cachos

            siguiente_cacho = self.lista_cachos[indice_actual]
            if siguiente_cacho.get_cantidad_dados() > 0:
                return siguiente_cacho
        
        return None

    def verificar_cachos_con_un_dado(self) -> Cacho:
        for cacho in self.lista_cachos:
            if cacho.get_cantidad_dados() == 1:
                return cacho
        return None

    def iniciar_ronda(self) -> None:
        self.apuesta_actual = (0, 0)
        self.ultimo_apostador = None

        # Si hay un iniciador predefinido, lo establecemos como cacho actual
        if self.iniciador_proxima_ronda is not None:
            self.cacho_actual = self.iniciador_proxima_ronda
            self.iniciador_proxima_ronda = None

        # Agitar dados y ocultarlos
        for cacho in self.lista_cachos:
            cacho.agitar()
            cacho.ocultar_dados()

        # Activar ronda especial si estaba pendiente
        if self.estado_especial_pendiente:
            self.estado_especial = True
            self.tipo_ronda_especial = self.tipo_ronda_especial_pendiente
            self.estado_especial_pendiente = False
            self.tipo_ronda_especial_pendiente = None
        else:
            self.estado_especial = False
            self.tipo_ronda_especial = None
            self.cacho_que_obligo = None

    def verificar_ronda_especial(self, cacho: Cacho) -> None:
        if cacho.get_cantidad_dados() == 1 and cacho not in self.cachos_que_usaron_especial:
            self.cacho_que_obligo = cacho
            self.estado_especial_pendiente = True
            self.cachos_que_usaron_especial.add(cacho)
