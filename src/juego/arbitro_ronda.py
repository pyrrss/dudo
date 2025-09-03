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
        cantidad_total = self._contar_total(lista_cachos, apuesta[1], ronda_especial)

        if cantidad_total >= apuesta[0]:
            dudador.quitar_dado()
            return dudador
        else:
            apostador.quitar_dado()
            return apostador
    
    def puede_calzar(self, lista_cachos: list[Cacho], calzador: Cacho) -> bool:
        if calzador.get_cantidad_dados() == 1:
            return True

        cantidad_inicial_dados = len(lista_cachos) * 5

        dados_en_juego = 0
        for cacho in lista_cachos:
            dados_en_juego += cacho.get_cantidad_dados()

        return dados_en_juego <= cantidad_inicial_dados // 2

    def manejar_calzar(self, lista_cachos: list[Cacho], apuesta: tuple[int, int], apostador: Cacho, calzador: Cacho, ronda_especial: bool = False) -> bool:
        cantidad_total = self._contar_total(lista_cachos, apuesta[1])

        if cantidad_total == apuesta[0]:
            calzador.agregar_dado()
            return True
        else:
            calzador.quitar_dado()
            return False
