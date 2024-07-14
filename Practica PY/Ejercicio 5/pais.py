from provincia import Provincia


class Pais():
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__provincia = []
        
    
    
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @property
    def provincia(self)-> str:
        return self.__provincia
   
        
    
    
    def __str__(self) -> str:
        print ("Pais: {}\n".format(self.nombre))  
        
    def remove_provincia(self, provincia:Provincia)->None:
        self.__provincia.remove(provincia)
        
    def add_provincia(self, provincia:Provincia)-> None:
        self.__provincia.append(provincia)              