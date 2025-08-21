from src.juego.dado import Dado

class TestDado:

    def test_generar_valor_aleatorio_llama_a_generador(self, mocker):
        """
        se verifica que Dado efectivamente se comunique con servicio
        GeneradorAleatorio
        """
        mock_generador_aleatorio = mocker.patch(
                "src.servicios.generador_aleatorio.GeneradorAleatorio.generar_valor",
                return_value=4
                )
        dado = Dado()
        dado.generar_valor_aleatorio()
        mock_generador_aleatorio.assert_called_once()

    def test_generar_valor_aleatorio_devuelve_valor_de_generador(self, mocker):
        """
        se verifica que se devuelva resultado esperado
        """
        mock_generador_aleatorio = mocker.patch(
                "src.servicios.generador_aleatorio.GeneradorAleatorio.generar_valor",
                return_value=4
                )
        dado = Dado()
        valor_generado = dado.generar_valor_aleatorio()

        assert valor_generado == 4

    def test_generar_valor_aleatorio_devuelve_valor_en_dominio(self):
        """
        se verifica que valores generados pertenecen al dominio 1-6
        """
        dado = Dado()
        for _ in range(10):
            valor_generado = dado.generar_valor_aleatorio()
            assert valor_generado in range(1, 7)
