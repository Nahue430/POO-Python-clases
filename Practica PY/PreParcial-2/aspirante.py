from titulo import Titulo
from inscripcion import Inscripcion


#Constructor ---> añadimos atributos y tambien lo que recibe de otra clase, por ej titulo.
class Aspirante():
    def __init__(self, nombre:str, apellido:str, email:str, num_telefono:str, titulo:Titulo) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__num_telefono = num_telefono
        self.__titulo = [] 
    
    @property
    def nombre(self)-> str:
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nuevo_nombre:str)-> None:
        self.__nombre = nuevo_nombre
        
    @property
    def apellido(self)->str:
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido:str )-> None:
        self.__apellido = nuevo_apellido
        
        
    @property
    def email(self)->str:
        return self.__email
    @email.setter
    def email(self, nuevo_email:str )-> None:
        self.__email = nuevo_email 
        
    @property
    def num_telefono(self)->str:
        return self.__num_telefono
    @num_telefono.setter
    def num_telefono(self, nuevo_num_telefono:str )-> None:
        self.__num_telefono = nuevo_num_telefono
        
    @property
    def titulo(self)-> Titulo:
        return self.__titulo
    
        
     #CUando se hacen estos metodos, se le asigna una lista vacia en el constructor. no poner en parametros.           
    def add_titulo(self, titulo:Titulo):
        self.__titulo.append(titulo)
        return self.__titulo
    
    def remove_titulo(self, titulo:Titulo):
        self.__titulo.remove(titulo)
        return self.__titulo
            
      
    
      
        
        
           
    """ metodo magico str"""
        
    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__apellido}, {self.__email}, {self.__num_telefono}, {self.__titulo}"   