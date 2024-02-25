from abc import ABC, abstractmethod
from cubos.empaque import Empaque

class Cubo(ABC):
    """
    Producto de una fábrica de cubos con varios tipos y precios
    """

    IVA = 0,19

    def __init__(self, lado: float, valor_fabricacion: float):
        self._lado = lado
        self._valor_fabricacion = valor_fabricacion
        self.__empaque = None

    def set_empaque(self, empaque):
        self.__empaque = empaque

    def esta_empacado(self) -> bool:
        if self.__empaque:
            return True
        return False

    def volumen(self) -> float:
        return self._lado ** 3

    def precio(self) -> float:
        return self._valor_fabricacion * 1.19

    def __str__(self):
        print(f"Lado {self._lado} cm. Precio ${self.precio()}")

    @abstractmethod
    def cabe(self, empaque: Empaque) -> bool:
        """
        Verifica si un cubo cabe en un empaque
        :param empaque: Eleemnto donde se espera guardar
        :return: boolean si el elemento cabe o no
        """