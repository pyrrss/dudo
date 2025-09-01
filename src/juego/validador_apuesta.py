class ValidadorApuesta:
    def __init__(self):
        pass

    def validar_nueva_apuesta(self, apuesta_actual: tuple[int, int], apuesta_nueva: tuple[int, int]) -> bool:
        # -> sin ases involucrados
        if apuesta_nueva[1] != 1 and apuesta_actual[1] != 1:
            if apuesta_nueva[0] > apuesta_actual[0] and apuesta_nueva[1] == apuesta_actual[1]:
                return True
            if apuesta_nueva[1] > apuesta_actual[1] and apuesta_nueva[0] == apuesta_actual[0]:
                return True
            if apuesta_nueva[0] > apuesta_actual[0] and apuesta_nueva[1] > apuesta_actual[1]:
                return True
        return False