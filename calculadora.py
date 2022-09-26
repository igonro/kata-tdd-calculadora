OP_TO_FUNC = {
    "suma": "suma",
    "resta": "resta",
    "mult": "multiplicacion",
    "div": "division",
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


def parse_entrada(texto):
    args = texto.strip().split(" ")
    if len(args) != 3:
        raise ValueError("Error: Número de parámetros incorrecto")
    op, n1, n2 = args
    if op not in OP_TO_FUNC:
        raise ValueError("Error: Introduce una operación válida")
    try:
        n1, n2 = float(n1), float(n2)
    except ValueError:
        raise ValueError("Error: Introduce un número válido")
    return OP_TO_FUNC[op], n1, n2


def ejecutar_operacion(operacion, n1, n2):
    func = globals()[operacion]
    return func(n1, n2)


def main():
    print("¡Hola! Introduce una operación")
    while True:
        try:
            entrada = input("> ")
            if entrada == "q":
                break
            try:
                op, n1, n2 = parse_entrada(entrada)
                resultado = ejecutar_operacion(op, n1, n2)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(e)
        except KeyboardInterrupt:
            break
    print("¡Adiós!")


if __name__ == "__main__":
    main()
