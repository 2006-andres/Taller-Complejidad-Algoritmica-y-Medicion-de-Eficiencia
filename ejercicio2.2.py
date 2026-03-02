# -----------------------------------------
# Ejercicio 2.2 — Insercion en orden
# -----------------------------------------

def insertar_en_orden(lista, valor):
    desplazamientos = 0
    i = len(lista) - 1

    # Agregamos espacio al final
    lista.append(0)

    # Movemos los elementos mayores hacia la derecha
    while i >= 0 and lista[i] > valor:
        lista[i + 1] = lista[i]
        desplazamientos += 1
        i -= 1

    # Insertamos el valor en la posicion correcta
    lista[i + 1] = valor

    return lista, desplazamientos


# -----------------------------------------
# Pruebas
# -----------------------------------------

def probar():
    lista = [10, 20, 30, 40, 50]

    # Mejor caso → insertar al final
    nueva_lista, desp_mejor = insertar_en_orden(lista.copy(), 60)
    print("Mejor caso (al final):")
    print("Lista:", nueva_lista)
    print("Desplazamientos:", desp_mejor)
    print("Complejidad: O(1)\n")

    # Peor caso → insertar al inicio
    nueva_lista, desp_peor = insertar_en_orden(lista.copy(), 5)
    print("Peor caso (al inicio):")
    print("Lista:", nueva_lista)
    print("Desplazamientos:", desp_peor)
    print("Complejidad: O(n)")


probar()