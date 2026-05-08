# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """
    if n <= 0:
        return 0
    num = 0
    for i in range(n+1):
        num += i
    return num  # Remove this line and implement


def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """
    pares = 0
    if n <= 0:
        return 0
    for i in range(n+1):
        if i % 2 == 0:
            pares += i
    return pares  # Remove this line and implement

def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """
    if n <= 0:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact  # Remove this line and implement