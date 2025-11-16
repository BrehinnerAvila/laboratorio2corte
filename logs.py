archivo = open("logs.txt", "r")       # Abrimos el archivo "logs.txt" en modo lectura
linea = archivo.readline()          # Leemos la primera línea del archivov

lista_usuarios = []
# Mientras la línea no esté vacía, seguimos leyendo
while linea != "":
    linea = linea.strip()            # Quitamos espacios y saltos de línea
    if linea != "":                   # Si la línea no está vacía
        partes = linea.split(",")      # Separamos por comas
        nombre = partes[0]                # El nombre del usuario es la primera parte
        lista_usuarios.append(nombre)       # Lo agregamos a la lista
    # Leemos la siguiente línea del archivo
    linea = archivo.readline()
archivo.close() # Cerramos el archivo
# sacar nombre unicos y contras los accesos

usuarios_unicos = []         # Lista para guardar usuarios únicos

            # Sacamos los nombres que no están repetidos
for nombre in lista_usuarios: 
    if nombre not in usuarios_unicos:          #si el nmbre no esta en lista 
        usuarios_unicos.append(nombre)           # lo agrgamos a la lista

            # Lista donde guardaremos el resultado final
resultados = []
# Para cada usuario único contamos cuántas veces aparece
for nombre in usuarios_unicos:
    contador = 0
    # Recorremos la lista completa y contamos cuántas veces aparece
    for u in lista_usuarios:
        if u == nombre:
            contador = contador + 1    
    resultados.append([nombre, contador])     #guardamos el resultado en la lista resultados
#imprimimos los resuktados
print("Accesos por usuario:")
for item in resultados:
    print(item)