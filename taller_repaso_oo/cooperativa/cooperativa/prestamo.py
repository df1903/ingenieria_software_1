from abc import ABC, abstractmethod

class Prestamo(ABC):
    """
    Prestamos de una cooperativa
    """

    def __init__(self, valor: float, tasa_mensual: float):
        self._valor = valor
        self._tasa_mensual = tasa_mensual

    @abstractmethod
    def interes_anual(self) -> float:
        """
        Calcula el interes anual de un prestamo
        :return: el interes anual de un prestamo
        """