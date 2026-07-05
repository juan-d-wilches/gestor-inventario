# -*- coding: utf-8 -*-
"""
Pruebas unitarias del Sistema de Gestion de Inventario (SGI)
Se usa el modulo unittest que viene incluido en Python.

Para ejecutar las pruebas:
    python -m unittest test_inventario.py -v
"""

import unittest
from inventario import Inventario, ProductoInvalidoError


class TestInventario(unittest.TestCase):

    def setUp(self):
        # Antes de cada prueba se crea un inventario nuevo y vacio
        self.inv = Inventario()

    # ==========================================================
    # CASO DE PRUEBA CP-01: Registro de productos con validacion
    # ==========================================================
    def test_cp01_agregar_producto(self):
        # Un producto con datos correctos se debe agregar sin problema
        resultado = self.inv.agregar_producto("P001", "Teclado mecanico", 150000, 10)
        self.assertTrue(resultado)
        self.assertIsNotNone(self.inv.buscar_producto("P001"))

        # Un producto con precio negativo debe ser rechazado
        with self.assertRaises(ProductoInvalidoError):
            self.inv.agregar_producto("P002", "Mouse gamer", -50000, 5)

        # Un producto con nombre vacio debe ser rechazado
        with self.assertRaises(ProductoInvalidoError):
            self.inv.agregar_producto("P003", "   ", 20000, 3)

        # No se puede repetir el mismo codigo dos veces
        with self.assertRaises(ProductoInvalidoError):
            self.inv.agregar_producto("P001", "Otro teclado", 90000, 2)

    # ==========================================================
    # CASO DE PRUEBA CP-02: Actualizacion de stock
    # ==========================================================
    def test_cp02_actualizar_stock(self):
        self.inv.agregar_producto("P001", "Monitor 24 pulgadas", 800000, 8)

        # Entrada de mercancia: el stock debe aumentar
        nuevo = self.inv.actualizar_stock("P001", 5)
        self.assertEqual(nuevo, 13)

        # Salida de mercancia: el stock debe disminuir
        nuevo = self.inv.actualizar_stock("P001", -3)
        self.assertEqual(nuevo, 10)

        # No se puede sacar mas stock del que existe
        with self.assertRaises(ProductoInvalidoError):
            self.inv.actualizar_stock("P001", -50)

        # No se puede actualizar un producto que no existe
        with self.assertRaises(ProductoInvalidoError):
            self.inv.actualizar_stock("P999", 10)

    # ==========================================================
    # CASO DE PRUEBA CP-03: Calculo del valor total del inventario
    # ==========================================================
    def test_cp03_valor_total(self):
        # Con el inventario vacio el total debe ser cero
        self.assertEqual(self.inv.valor_total(), 0.0)

        # Se agregan productos y se verifica el calculo:
        # (100000 x 2) + (50000 x 4) = 200000 + 200000 = 400000
        self.inv.agregar_producto("P001", "Disco duro 1TB", 100000, 2)
        self.inv.agregar_producto("P002", "Memoria RAM 8GB", 50000, 4)
        self.assertEqual(self.inv.valor_total(), 400000.0)

        # Si cambia el stock, el total tambien debe cambiar:
        # (100000 x 5) + (50000 x 4) = 500000 + 200000 = 700000
        self.inv.actualizar_stock("P001", 3)
        self.assertEqual(self.inv.valor_total(), 700000.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
