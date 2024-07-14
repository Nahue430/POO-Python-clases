from datos import *
from datetime import datetime

def menu():
    return "\n1 - Nueva Compra\n2 - Resumen Compras\n3 - Salir\n"

def menu_compra():
    return "\n1 - Agregar Producto\n2 - Finalizar Compra\n"

def cliente_loggeado():
    '''
        dummy function
        retorna cliente loggeado
    '''
    return cliente1

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        nueva_compra = Compra(cliente_loggeado())  # se genera una nueva compra con el cliente loggeado
        while True:
            print(menu_compra())
            opt = input("Ingrese la opcion seleccionada: ")
            if opt == "1":
                # Mostrar lista de productos disponibles
                for i, producto in enumerate(productos, start=1):
                    print(f"{i}. {producto.nombre} - Precio: {producto.precio_unitario}")
                
                seleccion = int(input("Seleccione el número de producto a agregar: ")) - 1
                if 0 <= seleccion < len(productos):
                    producto_seleccionado = productos[seleccion]
                    nueva_compra.add_producto(producto_seleccionado)
                    print(f"Producto '{producto_seleccionado.nombre}' agregado a la compra.")
                else:
                    print("Opción no válida.")
                
            elif opt == "2":
                nueva_compra.facturar_compra()
                nueva_compra.calcular_monto_total()
                print(f"Compra finalizada.\nMonto total a pagar con descuento: ${nueva_compra.monto_total:.2f}")
                break
            else:
                print("Error, Ingrese una opcion valida...")
    elif opt == "2":
        # Mostrar resumen de todas las compras
        for i, compra in enumerate(compras, 1):
            print(f"\nCompra {i}:")
            print(f"Cliente: {compra.cliente.nombre} {compra.cliente.apellido}")
            print(f"Fecha y hora: {compra.fecha_hora}")
            print(f"Cantidad de productos: {len(compra.cantidad_productos)}")
            print(f"Monto facturado: ${compra.monto_facturado:.2f}")
            print(f"Monto total: ${compra.monto_total:.2f}")
    elif opt == "3":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")