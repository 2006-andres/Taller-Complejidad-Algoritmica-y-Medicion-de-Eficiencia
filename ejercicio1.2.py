# -----------------------------------------
# Ejercicio 1.2 — Búsqueda Binaria O(log n)
# -----------------------------------------

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1  # contamos cada comparacion principal

        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, comparaciones


# -----------------------------------------
# Pruebas de mejor y peor caso
# -----------------------------------------

def probar(n):
    lista = list(range(n))  # lista ordenada [0,1,2,...,n-1]

    # Mejor caso: elemento justo en el centro
    objetivo_mejor = lista[n // 2]
    indice_mejor, comp_mejor = busqueda_binaria(lista, objetivo_mejor)

    # Peor caso: elemento que NO existe
    objetivo_peor = -1
    indice_peor, comp_peor = busqueda_binaria(lista, objetivo_peor)

    print(f"\nTamano n = {n}")
    print(f"Mejor caso -> Comparaciones: {comp_mejor}")
    print(f"Peor caso  -> Comparaciones: {comp_peor}")


# Ejecutar pruebas
probar(100)
probar(1000)
probar(10000)
