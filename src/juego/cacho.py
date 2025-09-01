from src.juego.dado import Dado


class Cacho:
    def __init__(self):
        self.dados = [Dado() for _ in range(5)]
        self.dados_en_espera = 0

    def obtener_dados(self):
        return self.dados

    def get_cantidad_dados(self) -> int:
        return len(self.dados)   

    def agitar(self):
        for dado in self.dados:
            dado.lanzar()

    def quitar_dado(self) -> None:
        if self.dados_en_espera > 0:
            self.dados_en_espera -= 1
            return

        if len(self.dados) > 0:
            self.dados.pop()

    def agregar_dado(self) -> None:
        if len(self.dados) < 5:
            nuevo_dado = Dado()
            nuevo_dado.lanzar()
            self.dados.append(nuevo_dado)
        else:
            self.dados_en_espera += 1
