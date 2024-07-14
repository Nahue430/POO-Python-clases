
from datetime import date

class Publicacion():
    __lista_isbn = []
    def __init__(self, isbn:str,fecha_lanzamiento:date, editorial:str) -> None:
        self.__isbn = Publicacion.__validar_isbn(isbn)
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__editorial = editorial
    
    @classmethod
    def __validar_isbn(cls,isbn):
        if isbn in cls.__lista_isbn:
            raise Exception("El isbn se encuentra ya registrado")
        else:
            cls.__lista_isbn.append(isbn)
            return isbn
            
           
    @property
    def isbn(self)->str:
        return self.__isbn
    
    @property
    def fecha_lanzamiento(self)->date:
        return self.__fecha_lanzamiento
    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, nueva_fecha_lanzamiento:date):
        self.__fecha_lanzamiento = nueva_fecha_lanzamiento
    
    @property
    def editorial(self)->str:
        return self.__editorial
    @editorial.setter
    def editorial(self, nueva_editorial:str):
        self.__editorial = nueva_editorial 
        
    def __str__(self) -> str:
        return (f"Numero:{self.isbn}\nFecha:{self.fecha_lanzamiento}\nEditorial:{self.editorial}")                 