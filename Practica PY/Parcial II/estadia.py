from hotel import Hotel
from datetime import date


class Estadia():
    def __init__(self, fecha_desde: date, fecha_hasta:date, hotel: Hotel):
      self.__fecha_desde = fecha_desde
      self.__fecha_hasta = fecha_hasta
      self.__hotel = hotel
    
    @property
    def fecha_desde(self)-> date:
        return self.__fecha_desde
    @fecha_desde.setter
    def fecha_desde(self, nueva_fecha_desde:date):
        self.__fecha_desde = nueva_fecha_desde
    @property
    def fecha_hasta(self)->date:
        return self.__fecha_hasta
    @fecha_hasta.setter
    def fecha_hasta(self, nueva_fecha_hasta:date):
        self.__fecha_hasta = nueva_fecha_hasta   
    
    @property
    def hotel(self)->Hotel:
        return self.__hotel
    @hotel.setter
    def hotel(self, nuevo_hotel:Hotel):
        self.__hotel = nuevo_hotel
    
    
    @property
    def cantidad_dias(self)-> int:
        return (self.fecha_hasta - self.fecha_desde).days
    
    
    def calcular_costo(self)-> float:
        self.hotel.calcular_costo(self.cantidad_dias)
    
          
      
     
      