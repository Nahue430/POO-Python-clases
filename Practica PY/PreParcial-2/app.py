from datos import *

def menu(): 
    return "\n1 - Nueva Inscripción\n2 - Ver carreras\n3 - Ver inscripciones\n4 - Salir\n"

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        continue
    if opt == "2":
        continue
    if opt == "3":
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")