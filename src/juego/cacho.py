from src.juego.dado import Dado


class Cacho:
    def __init__(self):
        self.lista_de_dados = [Dado() for _ in range(5)]

    def obtener_dados(self):
        return self.lista_de_dados

    def agitar(self):
        for dado in self.lista_de_dados:
            dado.lanzar()
