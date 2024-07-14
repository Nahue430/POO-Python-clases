from abc import ABC, abstractmethod
from datetime import *

class Curso(ABC):
    _lista_nombres = []
    @abstractmethod     
    def __init__(self,nombre:str, descripcion:str, link_reunion:str,hora:time) -> None:
        self._nombre = Curso.__validar_lista_nombre(nombre)
        self._descripcion= descripcion
        self._link_reunion = link_reunion
        self.hora = hora
        
    
    @classmethod
    def __validar_lista_nombre(cls,nombre:str):
            if nombre in cls._lista_nombres:
                raise Exception("El nombre se encuentra en uso")
            else:
                cls._lista_nombres.append(nombre)
                return nombre
    
    @property
    def nombre(self)->str:
        return self._nombre
    
        
    @property
    def descripcion(self)->str:
        return self._descripcion
    @descripcion.setter
    def descripcion(self, nuevo_descripcion:str):
        self._descripcion = nuevo_descripcion 
    
    @property
    def link_reunion(self)->str:
        return self._link_reunion
    @link_reunion.setter
    def link_reunion(self, nuevo_link_reunion:str):
        self._link_reunion = nuevo_link_reunion 
    
    
    @property
    def hora(self)->time:
        return self._hora
    @hora.setter
    def hora(self, nuevo_hora:time):
        self._hora = nuevo_hora                      