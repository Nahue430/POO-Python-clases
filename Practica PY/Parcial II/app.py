#from datos import *
from datetime import date

def menu(): 
    return "\n1 - Historial Viajes\n2 - Nuevo Viaje\n3 - Editar Viaje\n4 - Salir"

def menu_viaje():
    return "\n1 - Agregar Hotel\n2 - Volver"

def loggin():
    return usuario_loggeado

def historial_viaje():
    #...
    pass

def nuevo_viaje():
    #...
    print("Su viaje ha sido creado con éxito")
    pass

def editar_viaje():
    while True:

        print('''Viajes activos...''')
        #...
        ind_viaje = input("Seleccione el viaje a editar: ")
        #...
        print(menu_viaje())
        opt_sub_menu = input("Ingrese la opcion seleccionada: ")

        if opt_sub_menu == "1":
            #...
            print("Hotel agregado con éxito a su viaje...")
            pass
        elif opt_sub_menu == "2":
            break
        else:
            print("Error, Ingrese una opcion valida...")

while True:

    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")

    if opt == "1":
        historial_viaje()
    
    elif opt == "2":
        nuevo_viaje()

    elif opt == "3":
        editar_viaje()

    elif opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break

    else:
        print("Error, Ingrese una opcion valida...")