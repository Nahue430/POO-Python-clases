from titulo import Titulo
from inscripcion import Inscripcion
from datetime import date

class Carrera():
    
    def __init__(self, nombre:str, comienzo:date) -> None:
        self.__nombre = nombre
        self.__comienzo = date.today
        self.__titulos_grado_requeridos = []
        
    
    @property
    def nombre(self,nombre:str)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
        
    @property
    def comienzo(self, comienzo:date)-> date:
        return self.__comienzo     
    @comienzo.setter 
    def nombre(self, nuevo_comienzo:date):
        self.__comienzo = nuevo_comienzo
     
    def __str__(self) -> str:
        
       return f"{self.__nombre}, {date( self.__comienzo.month, self.__comienzo.year)}, {self.__titulos_grado_requeridos}"
    
    
    def add_titulo_requerido(self, titulo:Titulo):
        self.__titulos_grado_requeridos.append(titulo)
        return self.__titulos_grado_requeridos
    
    def remove_titulo_requerido(self, titulo:Titulo):
        self.__titulos_grado_requeridos.remove(titulo)
        return self.__titulos_grado_requeridos
    @property
    def cant_titulos_requeridos(self, titulos_grado_requeridos):
         return len(titulos_grado_requeridos)
       
        
            