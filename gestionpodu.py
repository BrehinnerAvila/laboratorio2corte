class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    # funcion para aumentar el stock
    def aumentar_stock(self, cantidad):
        if cantidad > 0:                   #solo sube el srock si la cantidad es positiva
            self.cantidad += cantidad
        else:
            print("La cantidad debe ser positiva.")
                                                        # funcion para disminuir el stock 
    def disminuir_stock(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.cantidad:  
                self.cantidad -= cantidad
            else:
                print("No hay suficiente stock.")
        else:
            print("La cantidad debe ser positiva.")
                                                        # funcion para mostrar  lainfo del producto
    def mostrar(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Stock: {self.cantidad}")
                # función para mostrar el inventario completo
def mostrar_inventario(lista):
    print("Inventario actual:")
    for producto in lista:
        producto.mostrar()
#ROGRAMA PRINCIPAL 
# Creaamos una lista de productos
inventario = [
    Producto("Manzanas", 1500, 20),
    Producto("Arroz", 3000, 50),
    Producto("Leche", 2500, 15)
]
mostrar_inventario(inventario)
print("\nAumentando stock de Manzanas en 10")
inventario[0].aumentar_stock(10)
print("Vendiendo 5 bolsas de Arroz")
inventario[1].disminuir_stock(5)   #resta las unidades
mostrar_inventario(inventario)
#llamamosm ufnicones