import math

OP_TO_FUNC = {
    "suma": "suma",
    "resta": "resta",
    "mult": "multiplicacion",
    "div": "division",
    "sqrt": "raiz_cuadrada",
}


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Error: No se puede dividir entre cero")


def raiz_cuadrada(a):
    if a < 0:
        raise ValueError(
            "Error: No se puede obtener raíz cuadrada de un número negativo"
        )
    return math.sqrt(a)


def parsear_entrada(texto):
    args = texto.strip().split(" ")
    op, *nums = args
    if op not in OP_TO_FUNC:
        raise ValueError("Error: Introduce una operación válida")
    if (op == "sqrt" and len(nums) != 1) or (op != "sqrt" and len(nums) != 2):
        raise ValueError("Error: Número de parámetros incorrecto")
    try:
        nums = list(map(float, nums))
    except ValueError:
        raise ValueError("Error: Introduce un número válido")
    return OP_TO_FUNC[op], nums


def ejecutar_operacion(operacion, nums):
    func = globals()[operacion]
    return func(*nums)


def main():
    print("¡Hola! Introduce una operación")
    while True:
        try:
            entrada = input("> ")
            if entrada == "q":
                break
            try:
                op, nums = parsear_entrada(entrada)
                resultado = ejecutar_operacion(op, nums)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(e)
        except KeyboardInterrupt:
            break
    print("¡Adiós!")


if __name__ == "__main__":
    main()
