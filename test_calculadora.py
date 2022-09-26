from numpy.testing import assert_almost_equal

import calculadora as calc


def test_funcion_suma():
    assert calc.suma(2, 2) == 4


def test_funcion_suma_numeros_negativos_y_decimales():
    assert calc.suma(2.5, -6) == -3.5


def test_funcion_resta():
    assert calc.resta(3, 2) == 1


def test_funcion_resta_numeros_negativos_y_decimales():
    assert calc.resta(3.3, -1.2) == 4.5


def test_funcion_multiplicacion():
    assert calc.multiplicacion(5, 3) == 15


def test_funcion_multiplicacion_numeros_negativos_y_decimales():
    assert_almost_equal(calc.multiplicacion(5.1, -3), -15.3)


def test_funcion_division():
    assert calc.division(5, 2) == 2.5


def test_funcion_division_numeros_negativos_y_decimales():
    assert calc.division(5.5, -1.1) == -5


def test_funcion_division_entre_0_devuelve_error():
    assert calc.division(5, 0) == "Error: No se puede dividir entre cero"
