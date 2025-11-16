#importar libreria
import math
#Area cuadrado
def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado.
    Retorna el área calculada del cuadrado.
        Parámetros:
            lado (float): La longitud del lado del cuadrado.
              area = lado * lado
            return area
    """
    area = lado * lado
    return area
#Area Triangulo
def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado la base y la altura.
    Retorna el área calculada del triángulo.
        Parámetros:
            base (float): La longitud de la base del triángulo.
            altura (float): La altura del triángulo.
              area = (base * altura) / 2
            return area
            """
    area = (base * altura) / 2
    return area
#Area circulo
def area_circulo(radio):
    """Calcula el área de un círculo dado el radio.
    Retorna el área calculada del círculo.
        Parámetros:
            radio (float): La longitud del radio del círculo.
              area = pi * radio * radio
            return area
    """
    area = math.pi * (radio ** 2)
    return area
def area_rectangulo(base,altura):
    """
    calcula el area del rectangulo y retorna el area calculada del circulo
        parametros:
        base y altura(float):la longitud de la base del rectangulo
        area=base*altura
    """
    area = base * altura
    return area
def area_rombo (diagonalmayor,diagonalmenor):
    """
    calcula el area del rombo y retorna el area calculada del rombo 
        parametros:
        diagonalmenor y diagonalmayor(float):la longitud de la diagonal mayor y menor
        area=(diagonal mayor *diagonal menor)/2
    """
    area=(diagonalmayor*diagonalmenor)/2
    return area
def area_romboide (base,altura):
    """
    calcula el area del romboide y retorna el area calculada del romboide
        parametros:
        base y altura(float):la longitud de la base del rectangulo
        area=base*altura
    """
    area = base * altura
    return area
def trapecio (basemayor,basemenor,altura):
    """
    calcula el area del trapecio y retorna el area del trapecio
        parametro:
        basemayor , basemenor y alruta(float):la longitud de la base mayor y menor 
        area
    """
    area=((basemayor+basemenor)/2)*altura
    return area
def area_pentagono (perimetro,apotema):
    """
    calcula el area del pentagono  y retorna el area del pentagono 
    parametro:
    perimetro y apotema(float):longitud  del perimetro y la apotema 
    """
    area=(perimetro*apotema)/2
    return area