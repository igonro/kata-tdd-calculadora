import pytest
from numpy.testing import assert_almost_equal

import calculadora as calc


@pytest.mark.parametrize("n1,n2,expected", [(2, 2, 4), (2.5, -6, -3.5)])
def test_suma_devuelve_resultado_correcto(n1, n2, expected):
    assert calc.suma(n1, n2) == expected


@pytest.mark.parametrize("n1,n2,expected", [(3, 2, 1), (3.3, -1.2, 4.5)])
def test_resta_devuelve_resultado_correcto(n1, n2, expected):
    assert calc.resta(n1, n2) == expected


@pytest.mark.parametrize("n1,n2,expected", [(5, 3, 15), (5.1, -3, -15.3)])
def test_multiplicacion_devuelve_resultado_correcto(n1, n2, expected):
    assert_almost_equal(calc.multiplicacion(n1, n2), expected)


@pytest.mark.parametrize("n1,n2,expected", [(5, 2, 2.5), (5.5, -1.1, -5)])
def test_division_devuelve_resultado_correcto(n1, n2, expected):
    assert calc.division(n1, n2) == expected


def test_division_entre_0_devuelve_error():
    with pytest.raises(ValueError, match="Error: No se puede dividir entre cero"):
        calc.division(5, 0)


@pytest.mark.parametrize("n,expected", [(16, 4), (6.25, 2.5)])
def test_raiz_cuadrada_devuelve_resultado_correcto(n, expected):
    assert calc.raiz_cuadrada(n) == expected


def test_raiz_cuadrada_negativa_devuelve_error():
    with pytest.raises(
        ValueError,
        match="Error: No se puede obtener raíz cuadrada de un número negativo",
    ):
        calc.raiz_cuadrada(-16)


@pytest.mark.parametrize(
    "input,expected",
    [
        ("suma 2 4.4", ("suma", [2, 4.4])),
        ("div -3.1 0", ("division", [-3.1, 0])),
        ("mult -3.33 1.0", ("multiplicacion", [-3.33, 1.0])),
        ("sqrt 1.0", ("raiz_cuadrada", [1.0])),
    ],
)
def test_parsear_entrada_devuelve_resultado_correcto(input, expected):
    assert calc.parsear_entrada(input) == expected


@pytest.mark.parametrize(
    "input,exception",
    [
        ("suma 2 4.4 5", "Error: Número de parámetros incorrecto"),
        ("suma", "Error: Número de parámetros incorrecto"),
        ("asdf 2 4.4", "Error: Introduce una operación válida"),
        ("suma 2 qwer", "Error: Introduce un número válido"),
    ],
)
def test_parsear_entrada_devuelve_error_con_argumentos_incorrectos(input, exception):
    with pytest.raises(ValueError, match=exception):
        calc.parsear_entrada(input)


@pytest.mark.parametrize(
    "op,nums,expected",
    [
        ("suma", [2, 4.4], 6.4),
        ("division", [-3.1, 2], -1.55),
        ("multiplicacion", [-3.33, 10], -33.3),
        ("raiz_cuadrada", [6.25], 2.5),
    ],
)
def test_ejecutar_operacion_devuelve_resultado_correcto(op, nums, expected):
    assert calc.ejecutar_operacion(op, nums) == expected
