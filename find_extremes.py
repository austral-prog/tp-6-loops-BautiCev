# Replace the "ANSWER HERE" for your answer

def find_min(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el menor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_min([3, 1, 7, 2]) -> 1
    Ejemplo: find_min([5, 5, 5]) -> 5
    Ejemplo: find_min([-3, -1, -7]) -> -7
    """
    min_value = numbers[0]
    for i in range(len(numbers)):
        if min_value > numbers[i]:
            min_value = numbers[i]
    return min_value  # Remove this line and implement

def find_max(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el mayor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_max([3, 1, 7, 2]) -> 7
    Ejemplo: find_max([5, 5, 5]) -> 5
    Ejemplo: find_max([-3, -1, -7]) -> -1
    """
    min_value = numbers[0]
    for i in range(len(numbers)):
        if min_value < numbers[i]:
            min_value = numbers[i]
    return min_value  # Remove this line and implement

def count_negatives(numbers):
    """
    Dada una lista de numeros, retorna la cantidad de numeros negativos.
    Si la lista esta vacia, retorna 0.

    Ejemplo: count_negatives([3, -1, -7, 2]) -> 2
    Ejemplo: count_negatives([1, 2, 3]) -> 0
    Ejemplo: count_negatives([-1, -2, -3]) -> 3
    """
    contador = 0
    for i in range(len(numbers)):
        if numbers[i] < 0:
            contador += 1
    if contador == 0:
        return 0
    return contador  # Remove this line and implement