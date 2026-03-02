# ================= ejercicio 1.1 =================
# Complejidad:
# Este algoritmo tiene complejidad O(1) (tiempo constante),
# porque el número de operaciones no depende del tamaño de la entrada.

# Resultado:
# El tiempo de ejecución permanece constante sin importar n.

# Conclusión:
# Los algoritmos O(1) son los más eficientes porque
# su rendimiento no cambia al crecer el tamaño del problema.
# ====================================================

# ================= ejercicio 1.2 =================
# Complejidad:
# Mejor caso: O(1) (cuando el elemento está en el centro).
# Peor caso: O(log n) (porque divide la lista a la mitad en cada paso).

# Resultados observados:
# n = 100    → ~6 comparaciones
# n = 1000   → ~9 comparaciones
# n = 10000  → ~13 comparaciones

# Conclusión:
# El número de comparaciones crece logarítmicamente.
# La búsqueda binaria es muy eficiente para listas grandes.
# ====================================================

# ================= ejercicio 2.1 =================
# Complejidad:
# Mejor caso: O(1) (si el elemento está al inicio).
# Caso promedio: O(n).
# Peor caso: O(n) (si está al final o no existe).

# Resultados observados:
# El número de comparaciones aumenta proporcionalmente a n.

# Conclusión:
# La búsqueda lineal es menos eficiente que la binaria,
# porque puede recorrer toda la lista.
# ====================================================

# ================= ejercicio 2.2 =================
# Complejidad:
# Mejor caso: O(1) (insertar al final).
# Peor caso: O(n) (insertar al inicio y desplazar todos los elementos).

# Resultados observados:
# El número de desplazamientos aumenta según la posición de inserción.

# Conclusión:
# Insertar al inicio es costoso porque se deben mover
# todos los elementos de la lista.
# ====================================================