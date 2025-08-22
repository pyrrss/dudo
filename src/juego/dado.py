from src.servicios.generador_aleatorio import GeneradorAleatorio

class Dado:
    denominaciones = {
            1: "As",
            2: "Tonto",
            3: "Tren",
            4: "Cuadra",
            5: "Quina",
            6: "Sexto"
            }

    def __init__(self):
        pass

    def generar_valor_aleatorio(self):
        return GeneradorAleatorio.generar_valor_aleatorio()

    def get_nombre_pinta(self, num_pinta):
        return self.denominaciones[num_pinta]
