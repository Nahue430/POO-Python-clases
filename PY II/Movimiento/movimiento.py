from tipoMovimiento import TipoMovimiento
from datetime import *

class Movimiento():
    __prox_nro= int(0)
    __iva = 0.21
    __comision = 0.001
    def __init__(self,en_proceso:bool,cantidad_titulos:int,monto:float, fecha:date=date.today(), hora:time=datetime.now()) -> None:
        self.__nro = Movimiento.__prox_nro()
        self.__fecha = fecha
        self.__hora = hora
        self.__en_proceso = True
        self.__cantidad_titulos = cantidad_titulos
        self.__monto = monto
        
    @classmethod
    def __prox_nro(cls):
        cls.__prox_nro +=1
        return cls.__prox_nro
    @property
    def nro(self):
        return self.__nro
    
    @property
    def fecha(self)->date:
        return self.__fecha
    @fecha.setter
    def fecha(self, nueva_fecha:date):
        self.__fecha = nueva_fecha
    
    @property
    def hora(self)->time:
        return self.__hora
    @hora.setter
    def hora(self, nueva_hora:time):
        self.__hora = nueva_hora  
        
    @property
    def en_proceso(self)->bool:
        return self.__en_proceso
    @en_proceso.setter
    def en_proceso(self, nueva_en_proceso:bool):
        self.__en_proceso = nueva_en_proceso 
    
    @property
    def cantidad_titulos(self)->int:
        return self.__cantidad_titulos
    @cantidad_titulos.setter
    def cantidad_titulos(self, nueva_cantidad_titulos:int):
        self.__cantidad_titulos = nueva_cantidad_titulos 
        
    @property
    def monto(self)->float:
        return self.__monto
    @monto.setter
    def monto(self, nueva_monto:float):
        self.__monto = nueva_monto 
        
    @property
    def fecha_liquidacion(self):
        fecha_liquidacion = datetime.now().date() + timedelta(days=self.__parking_en_dias)
        return fecha_liquidacion  
        
    @property
    def iva(self):
        return self.monto * Movimiento.__iva
    
    @property
    def comision(self):
        return self.monto * Movimiento.__comision               
        
    def __str__(self) -> str:
        return (f"Nro:{self.nro}\nFecha:{self.fecha}\nHora:{self.hora}\nMonto:{self.monto}")         
        