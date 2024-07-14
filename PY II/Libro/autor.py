class Autor():
    def __init__(self, apellido:str, nombre:str) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
    
    @property
    def apellido(self)->None:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido:str):
        self.__apellido = nuevo_apellido
    
    @property
    def nombre(self)->None:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre  
        
    
    def __str__(self) -> str:
        return (f"{self.apellido}\n {self.apellido}")              