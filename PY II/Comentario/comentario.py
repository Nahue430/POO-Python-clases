
from usuario import Usuario
from datetime import *
from typing import Self


class Comentario():
    def __init__(self,comentario:str,fecha:date,autor:Usuario,comentario_padre:'Comentario'=None,cantidad_veces_reportado:int=0) -> None:
        self.__comentario = comentario
        self.__fecha = fecha
        self.__cantidad_veces_reportado = cantidad_veces_reportado
        self.__comentario_padre = comentario_padre
        self.__autor = autor
        
        
    
    
    @property
    def comentario(self)->str:
        return self.__comentario
    @comentario.setter
    def comentario(self, nuevo_comentario:str):
        self.__comentario = nuevo_comentario
        
    @property
    def fecha(self)->date:
        return self.__fecha
    @fecha.setter
    def fecha(self, nueva_fecha:date):
        self.__fecha = nueva_fecha    
    
    @property
    def cantidad_veces_reportado(self):
        return self.__cantidad_veces_reportado
    @cantidad_veces_reportado.setter
    def cantidad_veces_reportado(self,nueva_cantidad_veces_reportado:int):
        self.__cantidad_veces_reportado = nueva_cantidad_veces_reportado
        
    @property
    def comentario_padre(self)->'Comentario':
        return self.__comentario_padre
    
    @property
    def autor(self)->Usuario:
        return self.__autor
    @autor.setter
    def autor(self, nuevo_autor:Usuario):
        self.__autor = nuevo_autor
            
        
    
    
    @property
    def comentario_oculto(self)->bool:
        if self.__cantidad_veces_reportado > 12:
            return True
        else:
            return False
    
       
    def reportar_comentario(self):
        if Usuario.nivel < 5:
            self.__cantidad_veces_reportado +=1
            
            
    def __str__(self) -> str:
        return (f"Fecha:{self.fecha}\nComentario:{self.comentario}\nAutor:{Usuario.nombre_usuario}")        
        
            
            
            
 
                  
        