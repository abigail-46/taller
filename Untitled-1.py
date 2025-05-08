
# Ejercicio 1: Máximo entre 3 números

def maximo_de_tres(a, b, c):
    return max(a, b, c)

# Ejercicio 2: Máximo entre 10 números usando función anterior

def maximo_de_diez(numeros):
    mayor = maximo_de_tres(numeros[0], numeros[1], numeros[2])
    for i in range(3, len(numeros)):
        mayor = max(mayor, numeros[i])
    return mayor

# Ejercicio 3: Operaciones con vectores

def suma_vector(v):
    return sum(v)

def suma_vectores(a, b):
    return [a[i] + b[i] for i in range(len(a))]

# Ejercicio 4: Contar vocales y consonantes

def contar_vocales(palabra):
    return sum(1 for c in palabra.lower() if c in 'aeiou')

def contar_consonantes(palabra):
    return sum(1 for c in palabra.lower() if c.isalpha() and c not in 'aeiou')

# Ejercicio 5: Menú con potencia, dígitos, capicúa

def potencia(x, k):
    return x ** k

def cantidad_digitos(x):
    return len(str(abs(x)))

def es_capicua(x):
    s = str(x)
    return s == s[::-1]
# Ejercicio 6: Suma o producto de matrices MxN

def cargar_matriz(m, n):
    return [[int(input(f"Elemento [{i}][{j}]: ")) for j in range(n)] for i in range(m)]

def sumar_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def producto_matrices(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def mostrar_matriz(m):
    for fila in m:
        print(fila)


# Ejercicio 7: Suma diagonal, factorial, sin repetidos y ordenado
import math

def suma_diagonal(m):
    return sum(m[i][i] for i in range(len(m)))

def filtrar_por_factorial(m, suma_diag):
    elementos = [x for fila in m for x in fila if math.factorial(x) >= suma_diag]
    return sorted(set(elementos))


# Ejercicio 8: Inventario de electrodomésticos
def cargar_electrodomesticos():
    lista = []
    while True:
        nombre = input("Nombre: ")
        proveedor = input("Proveedor: ")
        try:
            precio = str(int(input("Precio: ")))
            stock = str(int(input("Stock: ")))
            lista.append([nombre, proveedor, precio, stock])
        except ValueError:
            print("Error en precio o stock. Deben ser números.")
            continue
        if input("¿Agregar otro? (s/n): ") != 's':
            break
    return lista

def mostrar_por_proveedor(lista, proveedor):
    for item in lista:
        if item[1].lower() == proveedor.lower():
            print(item)

def menor_precio(lista):
    return min(lista, key=lambda x: int(x[2]))

def stock_positivo(lista):
    return [item for item in lista if int(item[3]) > 0]

# Ejercicio 9: Lista de espera con urgencias

from collections import deque

def agregar_paciente(lista, nombre):
    lista.append(nombre)

def atender_paciente(lista):
    return lista.popleft() if lista else "Lista vacía"

def urgencia_paciente(lista, nombre):
    lista.appendleft(nombre)

def faltan_para_atencion(lista, nombre):
    return list(lista).index(nombre) if nombre in lista else -1

# Ejercicio 10: Máquina tragamonedas

import random

def girar_rodillo(rodillo, vueltas):
    return rodillo[-vueltas % len(rodillo):] + rodillo[:-vueltas % len(rodillo)]

def jugar():
    simbolos = ['O', 'X', '7']
    rod1 = [random.choice(simbolos) for _ in range(9)]
    rod2 = [random.choice(simbolos) for _ in range(9)]
    rod3 = [random.choice(simbolos) for _ in range(9)]
    v1, v2, v3 = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
    r1 = girar_rodillo(rod1, v1)
    r2 = girar_rodillo(rod2, v2)
    r3 = girar_rodillo(rod3, v3)
    print("Rodillos:")
    print(r1[0], r2[0], r3[0])
    premio = {('X', 'X', 'X'): 10, ('O', 'O', 'O'): 100, ('7', '7', '7'): 1000}
    print("Ganó", premio.get((r1[0], r2[0], r3[0]), 0), "fichas")

