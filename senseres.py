import random
# Función para generar la matriz de temperaturas
def generar_matriz(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            temp = random.randint(0, 100)  # temperatura aleatoria
            fila.append(temp)
        matriz.append(fila)
    return matriz
# Función para detectar temperaturas críticas (> 80°C)
def detectar_criticos(matriz):
    criticos = []
    for i in range(len(matriz)):           # recorre filas
        for j in range(len(matriz[i])):    # recorre columnas
            if matriz[i][j] > 80:
                criticos.append([i, j, matriz[i][j]])  # posición y valor
    return criticos
# Programa principal
n = int(input("Ingrese numero de filas (n): "))
m = int(input("Ingrese numero de columnas (m): "))
        #  Generar matriz
matriz = generar_matriz(n, m)
        #  Mostrar matriz 
print("\nMatriz generada:")
for fila in matriz:
    print(fila)
        #  Detectar valores críticos
criticos = detectar_criticos(matriz)
print("\nSensores criticos (>80°C):")
for item in criticos:
    print(f"Fila {item[0]}, Columna {item[1]} → {item[2]}°C")
