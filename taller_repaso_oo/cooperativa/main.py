from cooperativa.cooperativa import Cooperativa

if __name__ == '__main__':
    cooperativa = Cooperativa('df1903', '19032003')

    cooperativa.prestamo_nominal(2000000, 1.5)
    cooperativa.prestamo_efectivo(2000000, 1.5)

    cooperativa.estimado_anual()
