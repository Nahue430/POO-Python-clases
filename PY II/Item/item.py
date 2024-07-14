from typing import self 

class Item():
    
    __ingredientes_receta = []
    def __init__(self, nombre:str, descripcion:str, cantidad_items_generado_receta:int, ingredientes_receta:'Item') -> None:
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__cantidad_items_generado_receta = cantidad_items_generado_receta
        self.__cantidad_ingredientes_distintos = Item.__ingredientes_distintos()
        self.__ingredientes_receta = ingredientes_receta
    
    
    @classmethod
    def __ingredientes_distintos(cls,ingrediente:'Item')->int:
        if  ingrediente in cls.__ingredientes_receta:
            raise Exception ("El ingrediente ya se encuentra en la lista")
        else:
            cls.__ingredientes_receta.append(ingrediente)
          
            return len(cls.__ingredientes_receta)
       
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
    
    @property
    def descripcion(self)->str:
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, nuevo_descripcion:str):
        self.__descripcion = nuevo_descripcion
    
    @property
    def cantidad_items_generado_receta(self)->str:
        return self.__cantidad_items_generado_receta
    @cantidad_items_generado_receta.setter
    def cantidad_items_generado_receta(self, nuevo_cantidad_items_generado_receta:str):
        self.__cantidad_items_generado_receta = nuevo_cantidad_items_generado_receta
    
    @property
    def cantidad_ingredientes_distintos(self)->int:
        return self.__cantidad_ingredientes_distintos    
        
    def __str__(self) -> str:
        return (f"Nombre:{self.nombre}\nDescripcion:{self.descripcion}\nCantidad receta:{self.__cantidad_items_generado_receta}\nCantidad de ingredientes:{self.cantidad_ingredientes_distintos}")  
    
    def add_ingrediente(cls, ingrediente:'Item')->'Item':
        if ingrediente in cls.__ingredientes_receta:
            cls.__ingredientes_receta.append(ingrediente)
        else:
            raise Exception("El ingrediente no se encuentra en la lista")
    
    def remove_ingrediente(cls, ingrediente:'Item')->'Item':
        if ingrediente in cls.__ingredientes_receta:
            cls.__ingredientes_receta.remove(ingrediente)
        else:
            raise Exception("El ingrediente no se encuentra en la lista")          
        