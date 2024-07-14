class Usuario():
    def __init__(self, nombre:str, apellido:str, email:str, password:str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__password = password
        
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self)-> str:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido:str):
        self.__apellido = nuevo_apellido
    
    @property
    def email(self)-> str:
        return self.__email
    @email.setter
    def email(self, nuevo_email:str):
        self.__email = nuevo_email 
        
    @property
    def password(self)-> str:
        return self.__password
    @password.setter
    def password(self, nuevo_password:str):
        self.__password = nuevo_password                         
        
    def __str__(self) -> str:
        print (f"Nombre:{self.nombre}\nApellido:{self.apellido}")
        
    def validar_credenciales(self, email:str, password:str)->bool:
        if (self.email == email) and (self.password == password):
            return True
        return False       