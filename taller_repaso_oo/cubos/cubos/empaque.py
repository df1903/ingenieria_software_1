class Empaque:

    def __init__(self,largo : float, ancho : float, alto : float):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def volumen(self) -> float:
        return self.largo * self.ancho * self.alto