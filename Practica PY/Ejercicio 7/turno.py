from datetime import datetime
from paciente import Paciente

class Turno():
    lista_token = []
    def __init__(self) -> None:
        self.__fecha = datetime.today().date()
        self.__hora = datetime.now().time()
        self.__estado = "Reservado"
        self.__autorizado = False
    
    @property
    def fecha(self)->datetime:
        return self.__fecha
    @fecha.setter
    def fecha(self, nueva_fecha:datetime):
        self.__fecha = nueva_fecha
        
    @property
    def hora(self)->datetime:
        return self.__hora
    @hora.setter
    def hora(self, nueva_hora:datetime):
        self.__hora = nueva_hora  
        
    @property
    def estado(self)->str:
        return self.__estado
    @estado.setter
    def estado(self, nuevo_estado:str):
        self.__estado = nuevo_estado    
        
    @property
    def autorizado(self)->bool:
        return self.__autorizado
    @autorizado.setter
    def autorizado(self, nuevo_autorizado:bool):
        self.__autorizado = nuevo_autorizado
    
    #Metodo STR
    def __str__(self) -> str:
        self.__autorizado = True
        return f"Fecha: {self.fecha}\n Hora: {self.hora}\n Estado: {self.estado}\n" 
    
    #Cancelamos turno cambiando el estado
    def cancelar_turno(self)->str:
        self.__estado = "Cancelado"
        
    #Primero validamos que el token no se repita    
    def validar_token(cls, token:int)->None:
        if token in cls.lista_token:
            raise Exception ("Token ya registadro")
        else:
            
            cls.lista_token.append(token)
                    
    #Cuando encontramos el token retornamos True para habilitar el registro del turno del paciente    
    def registrar_paciente(cls,token:int)->bool:
        if token in cls.lista_token:
            return True
        return False    
    
                
        
        
        