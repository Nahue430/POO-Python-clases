from datos import *

def menu(): 
    return "\n1 - Home\n2 - Nueva Lista\n3 - Ver listas\n4 - Salir\n"

while True:
    print(menu())
    opt = int(input("Ingrese la opcion seleccionada: "))
    if opt == 1:
        print("\nLISTA VIDEOS:")
        for video in videos:
            print(video)
    elif opt == 2:
        print("Creando una lista de reproducción ...")
        nueva_lista = input("Ingrese el nombre de la lista: ")
        listas.append(nueva_lista)
        print("Seleccione al menos un video para crear la lista...")
        for indice, video in enumerate(videos, 1):
            print(f"{indice} - {video.nombre}")
        opt = int(input("\n Seleccione el video: "))
        video_selec = videos[opt-1]
        listas[3].add_video([video_selec])
        print("Se creo la lista exitosamente...")
        #No pude hacer que se agregue, me dice AttributeError: 'str' object has no attribute 'add_video' no encuentro en que le estoy errando
        #lo intente hardcodear en la linea 22 pero tmp
    elif opt == 3:
        for lista in listas:
            print(lista)
    elif opt == 4:
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")