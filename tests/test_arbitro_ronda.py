from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.cacho import Cacho

import pytest

class TestArbitroRonda:

    @pytest.mark.parametrize("lista_valores",[
            [1, 4, 3, 6, 2, 4, 4, 6, 5, 5],
            [5, 5, 1, 2, 4, 3, 6, 2, 4, 4],
            [6, 6, 1, 4, 3, 2, 5, 3, 4, 6]
        ])
    def test_jugador_duda_incorrectamente_y_pierde_dado(self, lista_valores):
        """
        verificar que cuando un jugador duda incorrectamente sobre una apuesta, pierda un dado
        """
        cacho_a = Cacho()
        cacho_b = Cacho()
        cacho_a.set_valores_dados(lista_valores[:5])
        cacho_b.set_valores_dados(lista_valores[5:])

        lista_cachos = [cacho_a, cacho_b]
        apuesta = (3, 4) 

        arbitro_ronda = ArbitroRonda()
        arbitro_ronda.manejar_duda(lista_cachos, apuesta, apostador=cacho_a, dudador=cacho_b)

        assert cacho_b.get_cantidad_dados() == 4 # -> pierde un dado
        assert cacho_a.get_cantidad_dados() == 5 # -> queda igual

    @pytest.mark.parametrize("lista_valores",[
            [1, 4, 3, 6, 2, 4, 4, 6, 5, 5],
            [5, 5, 1, 2, 4, 3, 6, 2, 6, 4],
            [6, 6, 1, 4, 3, 2, 5, 3, 4, 6]
        ])
    def test_jugador_duda_correctamente_y_apostador_pierde_dado(self, lista_valores):
        """
        verificar que cuando un jugador duda correctamente sobre una apuesta,
        quien hizo la apuesta pierde un dado
        """
        cacho_a = Cacho()
        cacho_b = Cacho()
        cacho_a.set_valores_dados(lista_valores[:5])
        cacho_b.set_valores_dados(lista_valores[5:])
        lista_cachos = [cacho_a, cacho_b]

        apuesta = (5, 4) 
        arbitro_ronda = ArbitroRonda()
        arbitro_ronda.manejar_duda(lista_cachos, apuesta, apostador=cacho_a, dudador=cacho_b)

        assert cacho_a.get_cantidad_dados() == 4 # -> apostador pierde dado
        assert cacho_b.get_cantidad_dados() == 5 # -> queda igual

    def test_calzar_posible_con_jugador_con_un_dado(self):
        """
        se verifica que si calzador tiene solo un dado, puede calzar
        """
        cacho_a = Cacho()
        cacho_b = Cacho()
        lista_cachos = [cacho_a, cacho_b]
        cacho_b.dados = [cacho_b.dados[0]] # -> solo tiene un dado

        arbitro_ronda = ArbitroRonda()

        assert arbitro_ronda.puede_calzar(lista_cachos, cacho_b) is True
    
    def test_calzar_posible_con_mitad_dados_en_juego(self):
        """
        se verifica que si queda la mitad (o menos?) de dados en juego,
        se puede calzar
        """
        cacho_a = Cacho()
        cacho_b = Cacho()
        lista_cachos = [cacho_a, cacho_b]
        
        # -> se dejan 5 dados en total (mitad en juego)
        cacho_a.dados = cacho_a.dados[:2]
        cacho_b.dados = cacho_b.dados[:3]

        arbitro_ronda = ArbitroRonda()
        assert arbitro_ronda.puede_calzar(lista_cachos, cacho_b) is True
    
    def test_calzar_no_posible_por_cantidad_de_dados(self):
        """
        se verifica que si hay más de la mitad de dados en juego,
        no se puede calzar
        """
        cacho_a = Cacho()
        cacho_b = Cacho()
        lista_cachos = [cacho_a, cacho_b]

        arbitro_ronda = ArbitroRonda()
        assert arbitro_ronda.puede_calzar(lista_cachos, cacho_b) is False

