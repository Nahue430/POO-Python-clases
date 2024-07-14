from datetime import date
from persona import Persona

class Usuario(Persona):
    lista_user_name = []
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, edad: int, nro_documento: int, user_name:str, password:str, email:str, fecha_alta:date ) -> None:
        self.__user_name = Usuario.validar_user(user_name)
        self.__password = password
        self.__estado = True
        self.__email = email
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
        super().__init__(nombre, apellido, fecha_nacimiento, edad, nro_documento)
    
    
    @property
    def user_name(self)-> str:
        return self.__user_name
    @classmethod
    def validar_user(cls, user_name):
        if user_name in cls.__lista_user_name:
            raise Exception("El nombre de usuario ya está utilizado")
        cls.__lista_user_name.append(user_name)
        return user_name
        
    
    @property
    def password(self)-> str:
        return self.__password
    @password.setter
    def password(self, nuevo_password):
        self.__password = nuevo_password
    
    @property
    def estado(self)-> bool:
        return self.__estado    
        
    @property
    def email(self)-> str:
        return self.__email
    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email
    
    @property
    def fecha_alta(self)-> date:
        return self.__fecha_alta 
    
    @property
    def fecha_baja(self)-> date:
        return self.__fecha_baja       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def validar_credenciales(self,user_name:str, password:str)-> bool: 
        if (user_name == self.__user_name and password == self.__password):
            return True
        else:
            return False
    
    
    def baja_usuario(self)->None:
        self.__fecha_baja = date.today()
        self.__estado = False
             