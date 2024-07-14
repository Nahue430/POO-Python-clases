from usuario import Usuario
from datetime import date
from tag import Tag

class Video():
    def __init__(self, nombre:str, usuario:Usuario) -> None:
        self.__nombre = nombre
        self.__fecha_publicacion = date.today()
        self.__usuario = usuario
        self.__lista_tags = []
        
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
        
    @property
    def fecha_publicacion(self)-> date:
        return self.__fecha_publicacion
    
    @property
    def usuario(self)-> Usuario:
        return self.__usuario
    @usuario.setter
    def usuario(self, nuevo_usuario:Usuario):
        self.__usuario = nuevo_usuario 
    
    @property
    def lista_tags(self)-> Tag:
        return self.__lista_tags    
        
    
    def __str__(self) -> str:
        print (f"Nombre:{self.nombre}\n Fecha:{self.fecha_publicacion}\nAutor:{self.usuario}")
        
    def add_tag(self,tag:Tag):
        self.__lista_tags.append(tag)
        
    def remove_tag(self, tag:Tag):
        self.__lista_tags.remove(tag)         
        
                