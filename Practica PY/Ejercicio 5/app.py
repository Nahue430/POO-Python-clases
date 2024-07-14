from cliente import Cliente
from localidad import Localidad
from provincia import Provincia
from pais import Pais





print("Bienvenido al sistema\n")
while True:
    print("1 - Registrar cliente\n")
    print("2 - Buscar un cliente\n")
    opt = input("Ingrese una opcion\n")
    if opt == "1":
        nombre_apellido = input("Ingrese el nombre y apellido\n")      
    if opt == "2":
        pass
    else:
        print("Opcion incorrecta\n")
