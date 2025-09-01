from src.juego.validador_apuesta import ValidadorApuesta

import pytest

class TestValidadorApuesta:

    def test_cantidad_superior_misma_pinta_valida(self):
        """
        se verifica subir cantidad y mantener pinta sea válido
        """
        validador = ValidadorApuesta()
       
        assert validador.validar_nueva_apuesta((2, 2), (3, 2)) is True
        assert validador.validar_nueva_apuesta((5, 4), (6, 4)) is True

    def test_cantidad_inferior_misma_pinta_invalida(self):
        """
        se verifica que bajar cantidad y mantener pinta sea inválido
        """
        validador = ValidadorApuesta()

        assert validador.validar_nueva_apuesta((4, 3), (3, 3)) is False
        assert validador.validar_nueva_apuesta((6, 5), (4, 5)) is False

    def test_misma_cantidad_pinta_superior_valida(self):
        """
        se verifica que mantener cantidad y subir pinta sea válido
        """
        validador = ValidadorApuesta()

        assert validador.validar_nueva_apuesta((2, 2), (2, 3)) is True
        assert validador.validar_nueva_apuesta((5, 4), (5, 5)) is True

    def test_misma_cantidad_pinta_inferior_invalida(self):
        """
        se verifica que mantener cantidad y bajar pinta sea inválido
        """
        validador = ValidadorApuesta()

        assert validador.validar_nueva_apuesta((4, 3), (4, 2)) is False
        assert validador.validar_nueva_apuesta((6, 5), (6, 3)) is False

    def test_cantidad_y_pinta_superior_valida(self):
        """
        se verifica que subir cantidad y pinta sea válido
        """
        validador = ValidadorApuesta()

        assert validador.validar_nueva_apuesta((2, 2), (3, 3)) is True
        assert validador.validar_nueva_apuesta((5, 4), (6, 5)) is True

    def test_cantidad_y_pinta_inferior_invalida(self):
        """
        se verifica que bajar cantidad y pinta sea inválido
        """
        validador = ValidadorApuesta()

        assert validador.validar_nueva_apuesta((4, 3), (3, 3)) is False
        assert validador.validar_nueva_apuesta((6, 5), (7, 4)) is False