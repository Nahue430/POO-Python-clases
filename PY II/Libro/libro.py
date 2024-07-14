from autor import Autor
from datetime import *
from publicacion import Publicacion

class Libro():
    def __init__(self, titulo:str, nombre:str,isbn:str, fecha_lanzamiento:date,editorial:str) -> None:
        self.__titulo = titulo
        self.__nombre = nombre
        self.__publicacion = Publicacion(isbn,fecha_lanzamiento, editorial)
    
    
    @property
    def publicacion(self)->Publicacion:
        return self.__publicacion
    @publicacion.setter
    def publicacion(self, nueva_publicacion:Publicacion):
        self.__publicacion = nueva_publicacion
            
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, nuevo_titulo:str):
        self.__titulo = nuevo_titulo
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre 
    
    
    def __str__(self) -> str:
        return (f"{self.titulo}\n {self.nombre}")              