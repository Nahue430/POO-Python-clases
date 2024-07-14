


class Producto():
    __lista_codigos = []
    def __init__(self,nombre:str, codigo:str, precio_unitario:float) -> None:
        self.__nombre = nombre
        self.__codigo = Producto.__validar_codigo(codigo)
        self.__precio_unitario = precio_unitario
        
        
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str)-> str:
        self.__nombre = nuevo_nombre
    
    @property
    def codigo(self)-> str:
        return self.__codigo
    
    @property
    def precio_unitario(self)-> float:
        return self.__precio_unitario
    @precio_unitario.setter
    def precio_unitario(self, nuevo_precio_unitario:float)-> float:
        self.__precio_unitario = nuevo_precio_unitario
    
    
    def __str__(self) -> str:
        print(f"Nombre:{self.__nombre}\n Codigo:{self.__codigo}\n Precio:{self.__precio_unitario}")
    
    @classmethod    
    def __validar_codigo(cls,codigo:str)->str:
        if codigo in cls.__lista_codigos:
            raise Exception ("Ya existe el codigo")
        else:
            cls.__lista_codigos.append(codigo)
        return codigo        
           
        
            