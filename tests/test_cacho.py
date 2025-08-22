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
