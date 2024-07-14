class TipoMovimiento():
    def __init__(self,nombre:str, parking_en_dias:int) -> None:
        self.__nombre = nombre
        self.__parking_en_dias = parking_en_dias
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
    
    @property
    def parking_en_dias(self)->int:
        return self.__parking_en_dias
    @parking_en_dias.setter
    def parking_en_dias(self, nuevo_parking_en_dias:int):
        self.__parking_en_dias = nuevo_parking_en_dias 
        
        
    
            