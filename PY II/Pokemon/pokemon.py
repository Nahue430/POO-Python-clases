class Pokemon():
    __prox_nro =int(0)
    def __init__(self,nro:int,nombre:str) -> None:
        self.__nro = Pokemon.__validar_prox_nro()
        self.__nombre = nombre
        
    @classmethod
    def __validar_prox_nro(cls):
        cls.__prox_nro +=1
        return cls.__prox_nro
    @property
    def nro(self)->int:
        return self.__nro
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
            

    