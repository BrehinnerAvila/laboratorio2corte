#Solicitud de datos
#Solicitud datos cuadrado
def solicitar_datos_cuadrado():
    """
    Solicita al usuario la longitud del lado del cuadrado.
    Retorna la longitud del lado como un número flotante.
    """
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    return lado
#Solicitud datos triangulo
def solicitar_datos_triangulo():
    """
    Solicita al usuario la base y la altura del triángulo.
    Retorna la base y la altura como números flotantes.
    """
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura
#Solicitud datos circulo
def solicitar_datos_circulo():
    """
    Solicita al usuario el radio del círculo.
    Retorna el radio como un número flotante.
    """
    radio = float(input("Ingrese el radio del círculo: "))
    return radio
#Solicitud datos cuadrado
def solicitar_datos_rectangulo():
    """
    Solicita al usuario la longitud del lado y la altura del rectangulo.
    Retorna la longitud  y la altura del lado como un número flotante.
    """
    lado = float(input("Ingrese la longitud del lado del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    return lado, altura
#Solicitud datos triangulo
def solicitar_datos_rombo():
    """
    Solicita al usuario la diagonal mayor y la diagonal menor del rombo.
    Retorna la base y la altura como números flotantes.
    """
    Diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
    Diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
    return Diagonal_mayor, Diagonal_menor
#Solicitud datos circulo
def solicitar_datos_romboide():
    """
    Solicita al usuario la base y la altura del romboide.
    Retorna el radio como un número flotante.
    """
    base = float(input("Ingrese la bse del romboide: "))
    altura = float(input("Ingrese la altura del romboide: "))
    return base, altura
def solicitar_datos_trapecio():
    """
    Solicita al usuario la base mayor, base mayor y la altura del trapecio.
    Retorna el radio como un número flotante.
    """
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    altura = float(input("Ingrese la altura del círculo: "))
    return base_menor, base_mayor, altura
def solicitar_datos_pentagono():
    """
    Solicita al usuario el perimetro y el apotema del pentagono.
    Retorna el radio como un número flotante.
    """
    perimetro = float(input("Ingrese el perimetro del pentagono: "))
    apotema = float(input("Ingrese la apotema del pentagono: "))
    return perimetro, apotema
#Mostrar datos
#Mostrar area cuadrado
def mostrar_area_cuadrado(area):
    """
    Muestra el área del cuadrado al usuario.
    Parámetros:
        area (float): El área del cuadrado a mostrar.
    """
    print(f"El área del cuadrado es: {area}")
#Mostrar area triangulo
def mostrar_area_triangulo(area):    
    """
    Muestra el área del triángulo al usuario.
    Parámetros:
        area (float): El área del triángulo a mostrar.
    """
    print(f"El área del triángulo es: {area}")
#Mostrar area circulo
def mostrar_area_circulo(area):
    """
    Muestra el área del círculo al usuario.
    Parámetros:
        area (float): El área del círculo a mostrar.
    """
    print(f"El área del círculo es: {area}")
#Mostrar area rectangulo
def mostrar_area_rectangulo(area):
    """
    Muestra el área del recatangulo al usuario.
    Parámetros:
        area (float): El área del rectangulo a mostrar.
    """
    print(f"El área del rectangulo es: {area}")
#Mostrar area rombo
def mostrar_area_rombo(area):    
    """
    Muestra el área del rombo al usuario.
    Parámetros:
        area (float): El área del rombo a mostrar.
    """
    print(f"El área del rombo es: {area}")
#Mostrar area romboide 
def mostrar_area_romboide(area):
    """
    Muestra el área del romboide al usuario.
    Parámetros:
        area (float): El área del romboide a mostrar.
    """
    print(f"El área del romboide es: {area}")
#Mostrar area trapecio
def mostrar_area_trapecio(area):
    """
    Muestra el área del trapecio al usuario.
    Parámetros:
        area (float): El área del trapecio a mostrar.
    """
    print(f"El área del trapecio es: {area}")
    #Mostrar area trapecio
def mostrar_area_pentagono(area):
    """
    Muestra el área del pentagono al usuario.
    Parámetros:
        area (float): El área del pentagono a mostrar.
    """
    print(f"El área del pentagano es: {area}")
#Menu calculadora
def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    Retorna la opción seleccionada por el usuario como un entero.
    """
    print("Calculadora de Áreas de Figuras Geométricas")
    print("1. Calcular área del circulo")
    print("2. Calcular área del triangulo")
    print("3. Calcular área del cuadrado")
    print("4. Calcular área del rectángulo")
    print("5. Cacular área del rombo")
    print("6. Cacular área del romboide")
    print("7. Cacular área del trapecio")
    print("8. Cacular área del pentágono")
    print("9. Salir")
    opcion = int(input("Seleccione una opción (1-4): "))
    return opcion