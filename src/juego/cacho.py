from src.juego.dado import Dado


class Cacho:
    def __init__(self):
        self.dados = [Dado() for _ in range(5)]
        self.dados_en_espera = 0
        self.dados_ocultos = False

    def obtener_dados(self):
        return self.dados

    def get_valores(self) -> list[int]:
        if self.dados_ocultos:
            return ["?" for _ in self.dados]
        return [dado.valor_actual for dado in self.dados]

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

    def set_valores_dados(self, valores: list[int]) -> None:
        if len(valores) != len(self.dados):
            print("ERROR: número de valores no coincide con número de dados")
            return

        for valor in valores:
            if valor not in range(1, 7) or not isinstance(valor, int):
                print("ERROR: lista de valores inválida")
                return

        for i, dado in enumerate(self.dados):
            dado.valor_actual = valores[i]

    def ocultar_dados(self) -> None:
        self.dados_ocultos = True

    def mostrar_dados(self) -> None:
        self.dados_ocultos = False
