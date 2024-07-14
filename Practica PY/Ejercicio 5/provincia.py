from localidad import Localidad


class Provincia():
    
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__localidad = [] 
    
    
    
    
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @property
    def localidad(self)->str:
        return self.__localidad
    
    def __str__(self) -> str:
        print("Provincia: {}\n Localidad: {}".format(self.nombre), (self.localidad)) 
    
    def remove_localidad(self, localidad:Localidad)->None:
        if localidad in Provincia.localidad:
            self.__localidad.remove(localidad)
        else:
            raise Exception ("La localidad no se encuentra en la lista")    
        
    def add_localidad(self, localidad:Localidad)->None:
        if localidad in Provincia.localidad:
            raise Exception ("La localidad se encuentra registrada")
        else:
            self.__localidad.append(localidad)    
         
    
    
      