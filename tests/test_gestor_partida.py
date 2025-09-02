from unittest.mock import patch
from src.juego.gestor_partida import GestorPartida

class TestGestorPartida:

    def test_crear_partida_con_cachos(self):
        """
        crear una partida con cachos como jugadores
        """
        cantidad_jugadores = 3
    
        # act y asserts
        gestor = GestorPartida(cantidad_jugadores)
        assert len(gestor.lista_cachos) == 3
        for cacho in gestor.lista_cachos:
            assert cacho.get_cantidad_dados() == 5
        assert gestor.cacho_actual is None
        assert gestor.direccion is None

    def test_determinar_cacho_inicial_sin_empate(self, mocker):
        """
        el cacho con el dado mas alto inicia la partida
        """
        gestor = GestorPartida(3)
    
        # mocks para no usar testear con randoms 
        mock_dados = [3, 6, 4]  
    
        with patch('src.juego.gestor_partida.GeneradorAleatorio.generar_valor_aleatorio', side_effect=mock_dados):
            # act
            cacho_inicial = gestor.determinar_cacho_inicial()
    
        # assert
        assert cacho_inicial == gestor.cacho_actual

    def test_determinar_cacho_inicial_con_empate(self, mocker):
        """
        en caso de empate se vuelve a tirar dados solo para los empatados
        """
        # Arrange
        gestor = GestorPartida(2)
    
        # mock para randoms
        mock_dados = [5, 5, 2, 6] 
    
        with patch('src.juego.gestor_partida.GeneradorAleatorio.generar_valor_aleatorio', side_effect=mock_dados):
            # act
            cacho_inicial = gestor.determinar_cacho_inicial()
    
        # assert
        assert cacho_inicial == gestor.cacho_actual

    def test_establecer_direccion(self):
        """
        establecer la direccion de la partida
        """
        gestor = GestorPartida(2)
    
        # acts y asserts
        gestor.establecer_direccion("antihorario")
        assert gestor.direccion == "antihorario"
        gestor.establecer_direccion("horario")
        assert gestor.direccion == "horario"

    def test_siguiente_turno_horario(self):
        """
        obtener el cacho que juega en el siguiente turno, en sentido horario
        """
        gestor = GestorPartida(3)
        gestor.direccion = "horario"
        gestor.cacho_actual = gestor.lista_cachos[0]
    
        # act y assert
        siguiente = gestor.obtener_siguiente_cacho()
        assert siguiente == gestor.lista_cachos[1]

    def test_siguiente_turno_antihorario(self):
        """
        obtener el cacho que juega en el siguiente turno, en sentido antihorario
        """
        gestor = GestorPartida(3)
        gestor.direccion = "antihorario"
        gestor.cacho_actual = gestor.lista_cachos[0]
    
        # act y assert
        siguiente = gestor.obtener_siguiente_cacho()
        assert siguiente == gestor.lista_cachos[2] 

    def test_obtener_siguiente_cacho_sin_direccion(self):
        """
        cuando no se ha establecido direccion por defecto usa horario
        """
        gestor = GestorPartida(3)
        gestor.cacho_actual = gestor.lista_cachos[0]
        gestor.direccion = None
        
        siguiente = gestor.obtener_siguiente_cacho()
        assert siguiente == gestor.lista_cachos[1]
        assert gestor.direccion == "horario"

    def test_obtener_siguiente_cacho_con_cachos_sin_dados(self):
        """
        si todos los cachos no tienen dados retorna None
        """
        gestor = GestorPartida(2)
        gestor.cacho_actual = gestor.lista_cachos[0]
        for cacho in gestor.lista_cachos:
            cacho.dados = []
        
        resultado = gestor.obtener_siguiente_cacho()
        assert resultado is None

    def test_detectar_cachos_con_un_dado(self):
        """
        detectar cuando un cacho queda con un solo dado
        """
        gestor = GestorPartida(2)

        # mock cacho con un dado
        gestor.lista_cachos[1].dados = [Mock()]
    
        # act y assert
        cacho_un_dado = gestor.verificar_cachos_con_un_dado()
        assert cacho_un_dado == gestor.lista_cachos[1]

    def test_cachos_con_un_dado_retorna_none(self):
        """
        si ningun cacho tiene exactamente un dado retorna None
        """
        gestor = GestorPartida(2)
        
        # mock cachos con mas de un dado
        gestor.lista_cachos[0].dados = [Mock(), Mock()]
        gestor.lista_cachos[1].dados = [Mock(), Mock(), Mock()]
        
        # act y assert
        resultado = gestor.verificar_cachos_con_un_dado()
        assert resultado is None