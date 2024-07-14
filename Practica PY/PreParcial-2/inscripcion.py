from datetime import date
from carrera import Carrera
from aspirante import Aspirante
class Inscripcion():
    __prox_nro = int(0)
    
    def __init__(self, aspirante:Aspirante, carrera:Carrera) -> None:
        self.__nro = Inscripcion.get_prox_nro()
        self.__fecha_inscripcion = date.today
        self.__inscripcion_activa = True
        self.__aspirante: Aspirante = aspirante
        self.__carrera: Carrera = carrera
    
    
    @classmethod
    def get_prox_nro(cls):
        cls.__nro += 1
        return cls.__prox_nro
    @property
    def nro(self)-> int:
        return self.__nro
    
    
    
    @property
    def fecha_inscripcion(self) -> date:
        return self.__fecha_inscripcion
    
    @property
    def inscripcion_activa(self) -> bool:
        return self.__inscripcion_activa
    
   
    @property
    def aspirante(self)->Aspirante:
        return self.__aspirante
    
    @property
    def carrera(self)-> Carrera:
        return self.__carrera
    
    def __str__(self) -> str:
        return f"{self.__prox_nro}, {self.__nro}, {self.__fecha_inscripcion}, {self.__inscripcion_activa}"
    
    
      