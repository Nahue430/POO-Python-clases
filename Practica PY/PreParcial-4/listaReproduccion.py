from video import Video

class ListaReproduccion():
    
    __prox_nro = 1
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__nro = ListaReproduccion.__prox_nro() 
        self.__lista_videos = []
    
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
        
    @property
    def nro(self)->int:
        return self.__nro

    
    @property
    def lista_videos(self)->list:
        return self.__lista_videos
    @lista_videos.setter
    def lista_videos(self, nueva_lista_videos:list):
        self.__lista_videos = nueva_lista_videos    
        
    
    @classmethod
    def __prox_nro(cls)-> int:
        cls.__prox_nro += 1
        return cls.__prox_nro   
        
    @property
    def cantidad_videos(self)->int:
        return len(self.__lista_videos)
        
    
    def add_video(self, video:Video):
        self.__lista_videos.append(video)
        
    def remove_video(self, video:Video):
        self.__lista_videos.remove(video)    
        
    def __str__(self) -> str:
        print(f"Nombre:{self.nombre}\nVideo:{self.__lista_videos}\n Cantidad de videos:{self.cantidad_videos}")    
    
    
    
            