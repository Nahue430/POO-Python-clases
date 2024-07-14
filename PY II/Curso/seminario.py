from datetime import time
from curso import Curso
from datetime import *

class Seminario(Curso):
    def __init__(self, nombre: str, descripcion: str, link_reunion: str, hora: time, fecha:date) -> None:
        self.__fecha = fecha
        super().__init__(nombre, descripcion, link_reunion, hora)
    
    @property
    def fecha(self)->date:
        return self.__fecha
    @fecha.setter
    def fecha(self, nueva_fecha:date):
        self.__fecha = nueva_fecha
        
    def __str__(self) -> str:
        return f"Seminario: {self.nombre}\nFecha: {self.fecha}\nHora: {self.hora}"
          