from datetime import date
from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:date, edad:int, nro_documento:int) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._edad = Persona.edad()
        self._nro_documento = nro_documento
     
    @property    
    def edad(self)->int:
        today = date.today
        return (today.year - self._fecha_nacimiento.year)
    
    @property
    def nombre(self)-> str:
        return self._nombre
    @nombre.setter
    def nombre (self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
    @property
    def apellido(self)-> str:
        return self._apellido
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido
    
    @property
    def fecha_nacimiento(self)->date:
        return self._fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha_nacimiento):
        self._fecha_nacimiento = nueva_fecha_nacimiento
    
    @property
    def nro_documento(self)-> int:
        return self._nro_documento
    @nro_documento.setter
    def nro_documento(self, nuevo_nro_documento):
        self._nro_documento = nuevo_nro_documento
             
                   