# -*- coding: utf-8 -*-
"""
Sistema de Gestion de Inventario (SGI)
Programa sencillo de consola para registrar productos, actualizar stock
y calcular el valor total del inventario.

Materia: Calidad de Software
Actividad: Diseño y Elaboracion de un Tipo de Prueba para la Validacion de Software
"""


class ProductoInvalidoError(Exception):
    """Error personalizado para cuando los datos de un producto no son validos."""
    pass


class Inventario:
    """Clase principal que maneja la logica del inventario."""

    def __init__(self):
        # Los productos se guardan en un diccionario usando el codigo como llave
        self.productos = {}

    def agregar_producto(self, codigo, nombre, precio, cantidad):
        """
        Agrega un producto nuevo al inventario.
        Valida que los datos sean correctos antes de guardarlo.
        """
        if not codigo or not str(codigo).strip():
            raise ProductoInvalidoError("El codigo del producto no puede estar vacio")

        if not nombre or not str(nombre).strip():
            raise ProductoInvalidoError("El nombre del producto no puede estar vacio")

        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ProductoInvalidoError("El precio debe ser un numero mayor a cero")

        if not isinstance(cantidad, int) or cantidad < 0:
            raise ProductoInvalidoError("La cantidad debe ser un numero entero mayor o igual a cero")

        if codigo in self.productos:
            raise ProductoInvalidoError("Ya existe un producto con el codigo " + str(codigo))

        self.productos[codigo] = {
            "nombre": nombre.strip(),
            "precio": float(precio),
            "cantidad": cantidad
        }
        return True

    def actualizar_stock(self, codigo, cantidad):
        """
        Suma o resta unidades al stock de un producto.
        La cantidad puede ser positiva (entrada) o negativa (salida).
        El stock nunca puede quedar negativo.
        """
        if codigo not in self.productos:
            raise ProductoInvalidoError("El producto con codigo " + str(codigo) + " no existe")

        nuevo_stock = self.productos[codigo]["cantidad"] + cantidad

        if nuevo_stock < 0:
            raise ProductoInvalidoError(
                "No hay stock suficiente. Stock actual: "
                + str(self.productos[codigo]["cantidad"])
            )

        self.productos[codigo]["cantidad"] = nuevo_stock
        return nuevo_stock

    def buscar_producto(self, codigo):
        """Busca un producto por su codigo. Devuelve None si no existe."""
        return self.productos.get(codigo)

    def valor_total(self):
        """Calcula el valor total del inventario (precio x cantidad de cada producto)."""
        total = 0.0
        for codigo in self.productos:
            producto = self.productos[codigo]
            total += producto["precio"] * producto["cantidad"]
        return round(total, 2)

    def listar_productos(self):
        """Devuelve una lista con todos los productos registrados."""
        lista = []
        for codigo, datos in self.productos.items():
            lista.append({
                "codigo": codigo,
                "nombre": datos["nombre"],
                "precio": datos["precio"],
                "cantidad": datos["cantidad"]
            })
        return lista


def menu():
    """Menu principal del programa por consola."""
    inv = Inventario()
    while True:
        print("\n===== SISTEMA DE GESTION DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Buscar producto")
        print("4. Ver valor total del inventario")
        print("5. Listar productos")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                inv.agregar_producto(codigo, nombre, precio, cantidad)
                print(">> Producto agregado correctamente")

            elif opcion == "2":
                codigo = input("Codigo del producto: ")
                cantidad = int(input("Cantidad (+entrada / -salida): "))
                nuevo = inv.actualizar_stock(codigo, cantidad)
                print(">> Stock actualizado. Nuevo stock:", nuevo)

            elif opcion == "3":
                codigo = input("Codigo del producto: ")
                producto = inv.buscar_producto(codigo)
                if producto:
                    print(">> Encontrado:", producto)
                else:
                    print(">> El producto no existe")

            elif opcion == "4":
                print(">> Valor total del inventario: $", inv.valor_total())

            elif opcion == "5":
                for p in inv.listar_productos():
                    print(p)

            elif opcion == "6":
                print("Hasta luego!")
                break

            else:
                print(">> Opcion no valida")

        except ProductoInvalidoError as e:
            print(">> ERROR:", e)
        except ValueError:
            print(">> ERROR: Debe ingresar un valor numerico valido")


if __name__ == "__main__":
    menu()
