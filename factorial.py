def factorial(numero):
    if not isinstance(numero, int):
        raise TypeError("El valor debe ser un entero")
    if numero < 0:
        raise ValueError("El valor no puede ser negativo")
    if numero == 0 or numero == 1:
        return 1
    result = 1
    for i in range(2, numero + 1):
        result *= i
    return result