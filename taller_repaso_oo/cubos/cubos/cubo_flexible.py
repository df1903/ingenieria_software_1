from .cubo import Cubo
from .empaque import Empaque

class CuboFlexible(Cubo):

    def __init__(self, lado: float, valor_fabricacion: float, elasticidad: int):
        super().__init__(lado, valor_fabricacion)
        self._elasticidad = elasticidad

    def cabe(self, empaque: Empaque) -> bool:
        if self.volumen() < empaque.volumen():
            self.set_empaque(empaque)
            return True
        return False

    def precio(self) -> float:
        precio: float = super().precio()
        if self._elasticidad < 50:
            return '{:.2f}'.format(precio * 1.04)
        return '{:.2f}'.format(self.precio * 1.06)