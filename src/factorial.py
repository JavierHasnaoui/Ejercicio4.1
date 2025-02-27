"""
Módulo para calcular el factorial de un número entero no negativo.

Contiene una única función llamada 'factorial' que calcula el factorial
de un número entero, lanzando errores si se pasa un tipo o valor incorrecto.
"""

def factorial(numero):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    numero (int): Un número entero.

    Retorna:
    int: El factorial de 'numero'.

    Excepciones:
    Lanza TypeError si el parámetro no es un entero.
    Lanza ValueError si el parámetro es negativo.
    """
    if not isinstance(numero, int):
        raise TypeError("El valor debe ser un entero")
    if numero < 0:
        raise ValueError("El valor no puede ser negativo")
    if numero in (0, 1):  # Simplificación de la comparación
        return 1
    result = 1
    for i in range(2, numero + 1):
        result *= i
    return result
