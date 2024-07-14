from precio import Precio
from datetime import date, datetime
hora_entrada = datetime.now(). time()


class Estadia():
    lista_nro_patente = []
    def __init__(self, nro_patente:str, cant_horas:int) -> None:
        self.__fecha = date.today()
        self.__nro_patente = Estadia.validar_nro_patente(nro_patente)
        self.__hora_entrada = hora_entrada
        self.__hora_salida = None
        self.__cant_horas = Estadia.cant_horas(cant_horas)
        self.__estado:str = "Activo"
        self.__pagado = False
    
    @property
    def fecha(self)-> date:
        return self.__fecha
    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha
        
    @property
    def nro_patente(self)-> str:
        return self.__nro_patente
    @nro_patente.setter
    def nro_patente(self, nuevo_nro_patente):
        self.__nro_patente = nuevo_nro_patente
    
    @property
    def hora_entrada(self)->date:
        return self.__hora_entrada
    @hora_entrada.setter
    def fecha_entrada(self, nueva_fecha_entrada):
        self.__hora_entrada = nueva_fecha_entrada
    
    @property
    def hora_salida(self)->date:
        return self.__hora_salida
    @hora_salida.setter
    def hora_salida(self, nueva_hora_salida):
        self.__hora_salida = nueva_hora_salida
        
    @property
    def cant_horas(self)-> int:
        return self.__cant_horas  
    @property
    def estado(self)-> str:
        return self.__estado
    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado
          
    @property
    def pagado(self)-> bool:
        return self.__pagado
    @pagado.setter
    def pagado(self, nuevo_pagado):
        self.__pagado = nuevo_pagado      
    
    
    
        
    @classmethod
    def validar_nro_patente(cls, nro_patente):
        if nro_patente in cls.__lista_nro_patente:
            raise Exception("Patente ya registrada")
        else:
            cls.__lista_nro_patente.append(nro_patente)
    
    def __str__(self) -> str:
        return "Fecha: {self.__fecha}\n Patente: {self.__nro_patente}\n Hora de entrada: {self.__hora_entrada}\n Hora de salida: {self.__hora_salida}\n Pagado: {self.__pagado}"    

    @property
    def cant_horas(self)->int:
        cant_horas = self.__hora_salida.hour - self.__hora_entrada.hour  
        return cant_horas
    
    def registrar_salida(self)-> float: 
        self.__pagado = True
        self.__estado = "Inactivo"
        self.__hora_salida = datetime.time().now()
        
               