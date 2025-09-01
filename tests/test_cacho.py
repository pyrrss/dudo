from src.juego.cacho import Cacho
from src.juego.dado import Dado


class TestCacho:
    def test_dados_son_objetos_dados(self):
        """
        se verifica que la lista de dados del cacho efectivamente
        son objetos tipo Dado
        """
        cacho = Cacho()
        lista_de_dados = cacho.obtener_dados()
        assert all(isinstance(i, Dado) for i in lista_de_dados)

    def test_dados_agitados_en_el_rango(self):
        """
        se verifica que luego de agitar los dados
        esten en el rango
        """
        cacho = Cacho()
        cacho.agitar()
        lista_dados = cacho.obtener_dados()
        for i in range (len(lista_dados)):
            assert lista_dados[i].valor_actual in range (1,7)

    def test_cacho_tiene_cinco_dados_al_inicio(self):
        """
        se verifica que Cacho tiene cinco dados al instanciar
        """
        cacho = Cacho()

        assert len(cacho.dados) == 5

    def test_agregar_dado_a_cacho_con_maximo_de_dados_deja_el_dado_en_espera(self):
        """
        se verifica que al agregar un dado a un cacho y este ya tiene 5 dados,
        se deja el nuevo dado en espera
        """
        cacho = Cacho() # -> inicia con 5 dados
        cacho.agregar_dado()

        assert cacho.dados_en_espera == 1

    def test_agregar_dado_a_cacho_con_menos_de_cinco_dados(self):
        """
        se verifica que al agregar un dado a un cacho que no tiene el máximo
        de dados, este se agrega correctamente (sin quedar en espera)
        """
        cacho = Cacho()
        cacho.quitar_dado()
        cacho.agregar_dado()

        assert cacho.get_cantidad_dados() == 5
        assert cacho.dados_en_espera == 0

    def test_quitar_dado_resta_dados_en_espera(self):
        """
        se verifica que al quitar un dado a un jugador que tenía dados en espera,
        se disminuye la cantidad de dados en espera
        """
        cacho = Cacho()
        cacho.agregar_dado() # -> se agrega un dado, queda en espera
        cacho.quitar_dado() # -> debe quedar sin dados en espera

    def test_quitar_dado_disminuye_cantidad_de_dados(self):
        """
        se verifica que al quitar un dado a un jugador sin dados en espera,
        se disminuye su cantidad de dados
        """
        cacho = Cacho()
        cacho.quitar_dado()
        cacho.quitar_dado()

        assert cacho.get_cantidad_dados() == 3

    def test_no_quitar_dado_a_jugador_sin_dados(self):
        """
        se verifica que se maneja caso en donde se intenta quitar un dado a un
        cacho con 0 dados
        """
        cacho = Cacho()
        for _ in range(5):
            cacho.quitar_dado()

        # -> cacho sin dados, se intenta quitar uno más
        cacho.quitar_dado()

        assert cacho.get_cantidad_dados() == 0

