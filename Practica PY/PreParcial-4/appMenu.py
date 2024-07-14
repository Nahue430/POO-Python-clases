from datos import *
import os

def menu(): 
    return "\n1 - Home\n2 - Nueva Lista\n3 - Ver listas\n4 - Salir\n"

while True:
    print(menu())
    opt = int(input(" Ingrese la opcion seleccionada: "))
    os.system("cls")

    if opt == 1:
        print("")
        for video in videos:
            print(video)
        
            
    elif opt == 2:
        print("")
        print("Creando una lista de reproduccion ...")
        nombre_lista = input(" Ingrese el nombre de la lista: ")
        print(" Seleccione al menos un video para crear la lista...")
        for indice, video in enumerate(videos,1):
            print(f"{indice} - {video.nombre}")
        video_opc = int(input("Seleccione el video: "))
        video_seleccionado = videos[video_opc-1]
        nueva_lista = ListaReproduccion(nombre_lista)
        listas.append(nueva_lista)
        nueva_lista.add_video(video_seleccionado)
        print("Se creó la lista existosamente...")
        

    elif opt == 3:
        print("")
        for lista in listas:
            if not lista.cantidad_videos:
                print(f"La lista ---{lista.nombre}--- se encuentra vacia")
            else:
                print(lista)
        

    elif opt == 4:
        print("Gracias por utilizar nuestro sistema.")
        break

    else:
        print("Error, Ingrese una opcion valida...")