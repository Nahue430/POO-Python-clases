from datetime import date

class Usuario():
    def __init__(self,user_name:str, email:str, password:str, nombre:str, apellido:str) -> None:
        self.__user_name: user_name
        self.__estado = True
        self.__email = email
        self.__password = password
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_alta = date.today()
        self._fecha_baja = Usuario.baja_usuario()
        
        
    @property
    def user_name(self)-> str:
        return self.__user_name
    @user_name.setter
    def user_name(self, nuevo_user_name):
        self.__user_name = nuevo_user_name
    
    @property
    def email(self)-> str:
        return self.__email
    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email
        
    @property
    def password(self)-> str:
        return self.__password
    @password.setter
    def password(self, nuevo_password):
        self.__password = nuevo_password  
        
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre 
        
    @property
    def apellido(self)-> str:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido 
        
    @property
    def fecha_alta(self)-> str:
        return None                 
    
    @property
    def estado(self)-> bool:
        return self.__estado
    
    def validar_credenciales(self,user_name:str, password:str)-> bool: 
        if (user_name == self.__user_name and password == self.__password):
            return True
        else:
            return False
        
        
    def baja_usuario(self)->bool:
        self.__estado = False
        self.__fecha_baja = date.today()
        return self.__estado    
