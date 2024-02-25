from taller_repaso_oo.cooperativa.cooperativa.prestamo import Prestamo

class PrestamoNominal(Prestamo):

    def __init__(self, valor: float, tasa_mensual: float ):
        super().__init__(valor, tasa_mensual)

    def interes_anual(self) -> float :
        return ((self._valor) * (self._tasa_mensual % 100) * 12)
