from estadia import *
from estadia import Estadia
from datetime import datetime

class Precio():
    __precio_hora = float(1500) 
    
    @classmethod
    def precio_hora(cls)-> float:
        return cls.__precio_hora
    @precio_hora.setter
    def precio_hora(cls,nuevo_precio_hora):
        cls.__precio_hora = nuevo_precio_hora
    
    @classmethod
    def calcular_importe(cls,cant_horas:int)->Estadia:
        return cant_horas * cls.__precio_hora
        