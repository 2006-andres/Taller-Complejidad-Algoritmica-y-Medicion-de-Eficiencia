# -----------------------------------------
# Ejercicio 2.1 — Búsqueda Lineal
# -----------------------------------------

def busqueda_lineal(lista, objetivo):
    comparaciones = 0

    for i in range(len(lista)):
        comparaciones += 1  # contamos cada comparacion

        if lista[i] == objetivo:
            return i, comparaciones

    return -1, comparaciones


# -----------------------------------------
# Pruebas: mejor, promedio y peor caso
# -----------------------------------------

def probar(n):
    lista = list(range(n))  # [0,1,2,...,n-1]

    # Mejor caso → elemento en la primera posicion
    objetivo_mejor = lista[0]
    _, comp_mejor = busqueda_lineal(lista, objetivo_mejor)

    # Caso promedio → elemento en la mitad
    objetivo_promedio = lista[n // 2]
    _, comp_promedio = busqueda_lineal(lista, objetivo_promedio)

    # Peor caso → elemento que NO existe
    objetivo_peor = -1
    _, comp_peor = busqueda_lineal(lista, objetivo_peor)

    print(f"\nTamano n = {n}")
    print(f"Mejor caso     -> Comparaciones: {comp_mejor}  -> O(1)")
    print(f"Caso promedio  -> Comparaciones: {comp_promedio}  -> O(n)")
    print(f"Peor caso      -> Comparaciones: {comp_peor}  -> O(n)")


# Ejecutar prueba
probar(100)