 
class Hotel():
    def __init__(self, nombre: str, precio_por_noche: float):
      self.__nombre = nombre
      self.__precio_por_noche = precio_por_noche
    
    @property  
    def nombre(self)->str:
      return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
      self.__nombre = nuevo_nombre
    @property
    def precio_por_noche(self)-> float:
      return self.__precio_por_noche
    @precio_por_noche.setter
    def precio_por_noche(self, nuevo_precio_por_noche:str):
      self.__precio_por_noche = nuevo_precio_por_noche
    
    def __str__(self) -> str:
      return f"{self.nombre}, {self.precio_por_noche}"
    
    def calcular_costo(self,cantidad_dias:int)-> float:
      return cantidad_dias * self.precio_por_noche
      
     
