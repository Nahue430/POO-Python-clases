class Producto():
    def __init__(self,descripcion:str, monto:float) -> None:
        self.__descripcion= descripcion
        self.__monto = monto
    
    @property
    def descripcion(self)->str:
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, nueva_descripcion:str):
        self.__descripcion = nueva_descripcion
    
    @property
    def monto(self)->float:
        return self.__monto
    @monto.setter
    def monto(self, nueva_monto:float):
        self.__monto = nueva_monto    
    
    def __str__(self) -> str:
        return (f"Descripcion del porducto:{self.descripcion}\nMonto:{self.monto}")         