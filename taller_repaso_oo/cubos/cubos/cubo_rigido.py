from .cubo import Cubo
from .empaque import Empaque

class CuboRigido(Cubo):

    def __init__(self,lado: float, valor_fabricacion : float):
        super().__init__(lado, valor_fabricacion)

    def cabe(self, empaque: Empaque) -> bool:
        if (empaque.alto > self._lado) and (empaque.ancho > self._lado) and (empaque.largo  > self._lado):
            self.set_empaque(empaque)
            return True
        return False