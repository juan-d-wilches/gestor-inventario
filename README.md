# Sistema de Gestión de Inventario (SGI)

Programa sencillo de consola hecho en Python para gestionar el inventario de una tienda de tecnología. Permite registrar productos, actualizar el stock, buscar productos y calcular el valor total del inventario.

Proyecto realizado para la actividad **"Diseño y Elaboración de un Tipo de Prueba para la Validación de Software"** de la materia de Calidad de Software.

## Requisitos

- Python 3.8 o superior (no necesita librerías externas)

## Cómo ejecutar el programa

```bash
python inventario.py
```

Aparece un menú por consola con las opciones de agregar producto, actualizar stock, buscar, ver valor total y listar productos.

## Cómo ejecutar las pruebas unitarias

```bash
python -m unittest test_inventario.py -v
```

Se ejecutan 3 casos de prueba unitarios hechos con el módulo `unittest` de Python:

| Caso | Descripción |
|------|-------------|
| CP-01 | Registro de productos con validación de datos |
| CP-02 | Actualización de stock (entradas y salidas) |
| CP-03 | Cálculo del valor total del inventario |

## Autor

- Juan David Wilches
