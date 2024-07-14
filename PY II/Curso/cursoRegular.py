from datetime import time
from curso import Curso
from datetime import *

class CursoRegular(Curso):
    def __init__(self, nombre: str, descripcion: str, link_reunion: str, hora: time,monto_cuota_mensual:float,fecha_inicio:date, fecha_fin:date, dia_semana:str) -> None:
        self.__monto_cuota_mensual = monto_cuota_mensual
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__dia_semana = dia_semana
        super().__init__(nombre, descripcion, link_reunion, hora)
    
    @property
    def monto_cuota_mensual(self)->float:
        return self.__monto_cuota_mensual
    @monto_cuota_mensual.setter
    def monto_cuota_mensual(self, nuevo_monto_cuota_mensual:float):
        self.__monto_cuota_mensual = nuevo_monto_cuota_mensual
    
    @property
    def fecha_inicio(self)->date:
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, nuevo_fecha_inicio:date):
        self.__fecha_inicio = nuevo_fecha_inicio    
            
    @property
    def fecha_fin(self)->date:
        return self.__fecha_fin
    @fecha_fin.setter
    def fecha_fin(self, nuevo_fecha_fin:date):
        self.__fecha_fin = nuevo_fecha_fin        
        
    @property
    def dia_semana(self)->str:
        return self.__dia_semana
    @dia_semana.setter
    def dia_semana(self, nuevo_dia_semana:str):
        self.__dia_semana = nuevo_dia_semana 
    
    @property
    def monto_total_curso(self)->float:
        return self.__monto_cuota_mensual * 12
    @property
    def cantidad_meses(self):
        return int(self.fecha_fin.month() - self.fecha_inicio())       