# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            lista.append(matrix[i][j])
    return lista  # Remove this line and implement

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    var = 0
    lista = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            var += matrix[i][j]
        lista.append(var)
        var = 0

    return lista  # Remove this line and implement

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    lista = [0] * len(matrix[0])

    for fila in matrix:
        for j in range(len(fila)):
            lista[j] += fila[j]

    return lista
print(col_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))