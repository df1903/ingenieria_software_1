from .prestamo_nominal import PrestamoNominal
from .prestamo_efectivo import PrestamoEfectivo

class Cooperativa():

    def __init__(self, nombre: str, nit: str):
        self._nombre = nombre
        self._nit = nit
        self._prestamos = []

    def prestamo_nominal(self, valor: float, tasa_mensual: float):
        self._prestamos.append(PrestamoNominal(valor, tasa_mensual))

    def prestamo_efectivo(self, valor: float, tasa_mensual: float):
        self._prestamos.append(PrestamoEfectivo(valor, tasa_mensual))

    def estimado_anual(self):
        total: float = 0
        for i in self._prestamos:
            total += i.interes_anual()
        print(f"Valor anual de los intereses: {total}")
        return total