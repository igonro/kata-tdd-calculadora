# Kata TDD: Calculadora

En esta Kata practicaremos la metodología TDD (_Test Driven Development_) con
un ejercicio práctico: programación de una calculadora interactiva.

## Procedimiento

-   Se creará un fichero `calculadora.py` que incluirá el código necesario para
    ejecutar el programa.

-   Se creará un fichero `test_calculadora.py` que incluirá toda la batería de
    tests para probar las funcionalidades requeridas. Se ejecutará con `pytest`.

-   Para este ejercicio sólo se utilizarán funciones (no clases).

-   Hay que implementar la calculadora utilizando la metodología TDD, es decir,
    primero hay que implementar un test y luego haremos que ese test pase.

## Tarea 1

Se te ha encargado desarrollar un programa calculadora.

Los requisitos son los siguientes:

-   La calculadora debe incluir las siguientes operaciones: suma, resta,
    multiplicación y división.

-   El usuario podrá introducir números reales (positivos y negativos, enteros
    y con decimales).

-   No puede saltar ninguna excepción, sólo mensajes de error informativos.

-   La calculadora se ejecutará en modo interactivo. Al ejecutar el programa
    se pedirá al usuario que introduzca una operación matemática. El programa
    devolverá el resultado (cuando no hay errores) y no finalizará hasta que el
    usuario introduzca `q` o pulse `Ctrl+C`.

```bash
> python calculadora.py
# OUT: ¡Hola!
> suma 2 2
# OUT: Resultado: 4
> resta 5 2
# OUT: Resultado: 3
> mult 3 2
# OUT: Resultado: 6
> div 5 2
# OUT: Resultado: 2.5
> q
# OUT: ¡Adiós!
```

## Tarea 2

-   La calculadora debe incluir también la operación raíz cuadrada.

```bash
> python calculadora.py
# OUT: ¡Hola!
> sqrt 16
# OUT: Resultado: 4
> q
# OUT: ¡Adiós!
```

## Tarea 3

-   Las operaciones suma y multiplicación deben aceptar 2 o más números.

```bash
> python calculadora.py
# OUT: ¡Hola!
> suma 2 2 6 3
# OUT: Resultado: 13
> mult 3 2 1 10
# OUT: Resultado: 60
> q
# OUT: ¡Adiós!
```
