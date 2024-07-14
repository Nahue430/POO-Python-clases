from estadia import Estadia
from datetime import date



class Viaje():
    
    __nro= 0
    def __init__(self, nombre:str, fecha_desde:date, fecha_hasta:date):
        self.__nombre = nombre
        self.__fecha_desde = fecha_desde
        self.__fecha_hasta = fecha_hasta
        self.__lista_estadias = []
        self.__nro_viaje = Viaje.nro()
        
    
    @classmethod
    def nro(cls):
        cls.__nro += 1
        return cls.__nro
    
    
    @property
    def lista_estadias(self)-> list:
        return self.__lista_estadias
        
    
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
        
    @property
    def fecha_desde(self)-> date:
        return self.__fecha_desde
    
    @fecha_desde.setter
    def fecha_desde(self, nueva_fecha_desde):
        self.__fecha_desde = nueva_fecha_desde
    
    @property
    def fecha_hasta(self)-> date:
        return self.__fecha_hasta
    
    @fecha_hasta.setter
    def fecha_hasta(self, nueva_fecha_hasta):
        self.__fecha_hasta = nueva_fecha_hasta  
        
    
    @property
    def cantidad_dias(self)-> int:
        """ 
        acum = 0
        for estadia in self.lista_estadias:
           acum += estadia.cantidad_dias
           
        return acum
         """ 
        return sum([estadia.cantidad_dias for estadia in self.lista_estadias]) 
   
   
    def add_estadia(self, estadia:Estadia):
        self.__lista_estadias.append(estadia)
    
    def remove_estadia(self, estadia:Estadia):
        self.__lista_estadias.remove(estadia)
        