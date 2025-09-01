from src.juego.cacho import Cacho
from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:
    def __init__(self):
        self.contador_pintas = ContadorPintas()

    def _contar_total(self, lista_cachos: list[Cacho], pinta: int, ronda_especial: bool = False) -> int:
        lista_valores = []
        for cacho in lista_cachos:
            for dado in cacho.dados:
                lista_valores.append(dado.valor_actual)
                        
        cantidad_total = self.contador_pintas.contar_apariciones(lista_valores, pinta, not ronda_especial)
        return cantidad_total
    
    def manejar_duda(self, lista_cachos: list[Cacho], apuesta: tuple[int, int], apostador: Cacho, dudador: Cacho, ronda_especial: bool = False) -> Cacho:
        cantidad_total = self._contar_total(lista_cachos, apuesta[1])

        if cantidad_total >= apuesta[0]:
            dudador.quitar_dado()
            return dudador
        else:
            apostador.quitar_dado()
            return apostador