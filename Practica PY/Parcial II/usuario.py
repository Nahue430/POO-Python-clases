from viaje import Viaje

class Usuario:

    def _init_(self, nombre_usuario:str, password:str) -> None:
        self.__nombre_usuario:str = nombre_usuario
        self.__password:str = password
        self.__viajes = []


    @property
    def nombre_usuario(self)->str:
        return self.__nombre_usuario
    @nombre_usuario.setter
    def nombre_usuario(self, nuevo_nombre_usuario):
        self.__nombre_usuario = nuevo_nombre_usuario

    @property
    def password(self)->str:
        return self.__password
    @password.setter
    def password(self, nueva_password):
        self.__password = nueva_password

    
    @property
    def viajes(self)->list:
        return self.__viajes
    
    
    def add_viaje(self, viaje:Viaje):
        self.__viajes.append(viaje)

    def remove_viaje(self, viaje:Viaje):
        self.__viajes.remove(viaje)

    def _str_(self) -> str:
        return f"{self.nombre_usuario}, {self.password}"