class Vehiculo():

    def __init__(self, placa: str):
        self._placa = placa
        self._autonomia = 0

    def echar_extra(self, cantidad_gasolina: float):
        self._autonomia += cantidad_gasolina * 40

    def echar_normal(self, cantidad_gasolina: float):
        self._autonomia += cantidad_gasolina * 30

    def realizar_recorrido(self, kilometros: float):
        if kilometros <= self._autonomia:
            print('Sí puede')
        else:
            print('No puede')
    