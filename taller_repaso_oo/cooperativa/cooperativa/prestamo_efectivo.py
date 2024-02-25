from taller_repaso_oo.cooperativa.cooperativa.prestamo import Prestamo

class PrestamoEfectivo(Prestamo):

    def __init__(self, valor, tasa_mensual):
        super().__init__(valor, tasa_mensual)

    def tasa_efectiva_anual(self) -> float:
        return ((1+(self._tasa_mensual/100))**12)-1

    def interes_anual(self):
        return self._valor * self.tasa_efectiva_anual()
