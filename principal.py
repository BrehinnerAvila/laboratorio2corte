# Llamar funciones del archivo figuras.py
from figuras import *

# Llamar funciones del archivo interfaz.py
from interfaz import *

# Función principal
# Variables del menú
opcion = 0
CUADRADO = 1
TRIANGULO = 2
CIRCULO = 3
RECTANGULO = 4
ROMBO = 5
ROMBOIDE = 6
TRAPECIO = 7
PENTAGONO = 8
SALIR = 9

while opcion != SALIR:
    opcion = mostrar_menu()

    if opcion == CUADRADO:
        lado = solicitar_datos_cuadrado()
        area = area_cuadrado(lado)
        mostrar_area_cuadrado(area)

    elif opcion == TRIANGULO:
        base, altura = solicitar_datos_triangulo()
        area = area_triangulo(base, altura)
        mostrar_area_triangulo(area)

    elif opcion == CIRCULO:
        radio = solicitar_datos_circulo()
        area = area_circulo(radio)
        mostrar_area_circulo(area)

    elif opcion == RECTANGULO:
        base, altura = solicitar_datos_rectangulo()
        area = area_rectangulo(base, altura)
        mostrar_area_rectangulo(area)

    elif opcion == ROMBO:
        diagonal_mayor, diagonal_menor = solicitar_datos_rombo()
        area = area_rombo(diagonal_mayor, diagonal_menor)
        mostrar_area_rombo(area)

    elif opcion == ROMBOIDE:
        base, altura = solicitar_datos_romboide()
        area = area_romboide(base, altura)
        mostrar_area_romboide(area)

    elif opcion == TRAPECIO:
        base_menor, base_mayor, altura = solicitar_datos_trapecio()
        area = trapecio(base_menor, base_mayor, altura)
        mostrar_area_trapecio(area)

    elif opcion == PENTAGONO:
        lado, apotema = solicitar_datos_pentagono()
        area = area_pentagono(lado, apotema)
        mostrar_area_pentagono(area)

    elif opcion == SALIR:
        print("Saliendo de la calculadora. ¡Hasta luego!")

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")