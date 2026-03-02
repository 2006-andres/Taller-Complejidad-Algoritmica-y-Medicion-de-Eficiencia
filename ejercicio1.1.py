# -----------------------------------------
# Ejercicio 1.1 — Operaciones O(1)
# -----------------------------------------

def es_par(n):
    """
    Devuelve True si el numero es par,
    False si es impar.
    """
    # Esta operacion es O(1) en tiempo porque:
    # - Solo realiza una operación módulo (%) y una comparación.
    # - No depende del valor de n ni de su tamaño.
    # Siempre ejecuta la misma cantidad de instrucciones.
    
    # Es O(1) en espacio extra porque:
    # - No crea listas ni estructuras adicionales.
    # - Solo usa una variable simple para devolver el resultado.
    return n % 2 == 0


def ultimo_digito(n):
    """
    Devuelve el ultimo digito de un numero entero.
    """
    # Esta operacion es O(1) en tiempo porque:
    # - Solo realiza abs(n) y una operación modulo (% 10).
    # - La cantidad de operaciones es fija y no crece.
    
    # Es O(1) en espacio extra porque:
    # - No almacena datos adicionales.
    # - Solo devuelve un valor entero.
    return abs(n) % 10


def mayor(a, b):
    """
    Devuelve el numero mayor entre a y b.
    """
     # Esta operacion es O(1) en tiempo porque:
    # - Solo realiza una comparacion (a > b).
    # - No importa el valor de los numeros, siempre hace lo mismo.
    
    # Es O(1) en espacio extra porque:
    # - No crea estructuras de datos.
    # - Solo usa variables simples ya existentes.
    if a > b:
        return a
    else:
        return b


# -----------------------------------------
# Programa principal para probar funciones
# -----------------------------------------

if __name__ == "__main__":
    
    n = int(input("Ingrese un numero: "))
    a = int(input("Ingrese el primer numero para comparar: "))
    b = int(input("Ingrese el segundo numero para comparar: "))

    # Par o impar
    if es_par(n):
        print(f"{n} es par.")
    else:
        print(f"{n} es impar.")

    # Ultimo digito
    print(f"El ultimo digito de {n} es: {ultimo_digito(n)}")

    # Mayor entre dos numeros
    print(f"El mayor entre {a} y {b} es: {mayor(a, b)}")