from cubos.cubo_rigido import CuboRigido
from cubos.cubo_flexible import CuboFlexible
from cubos.empaque import Empaque



if __name__ == '__main__':
    # pruebas
    empaque1 = Empaque(5, 5, 100)
    cubo1 = CuboRigido(10, 2000)
    cubo2 = CuboFlexible(10, 2000, 20)

    cubo1.__str__()
    cubo2.__str__()

    print(cubo1.cabe(empaque1))
    print(cubo1.esta_empacado())
    print(cubo2.cabe(empaque1))
    print(cubo2.esta_empacado())
