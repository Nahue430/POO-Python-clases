from datetime import date

class Cliente():
    contador = int(0)
    def __init__(self, nombre_apellido:str, direccion:str) -> None:
        self.__nombre_apellido = nombre_apellido
        Cliente.contador += 1
        self.__nro_cliente = Cliente.contador
        self.__direccion = direccion
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
        


    @property
    def nombre_apellido(self)->str:
        return self.__nombre_apellido
    @nombre_apellido.setter
    def nombre_apellido(self, nuevo_nombre_apellido):
        self.__nombre_apellido = nuevo_nombre_apellido
    
    @property
    def nro_cliente(self)->int:
        return self.__nro_cliente
    
    
    @property
    def direccion(self)->str:
        return self.__direccion
    @direccion.setter
    def direccion(self, nueva_direccion):
        self.__direccion = nueva_direccion
    
    @property
    def fecha_alta(self)->str:
        return self.__fecha_alta
    
    
    @property
    def fecha_baja(self)->str:
        return self.__fecha_baja
    @fecha_baja.setter
    def fecha_baja(self, nueva_fecha_baja):
        self.__fecha_baja = nueva_fecha_baja  
        
        
        
    def __str__(self) -> str:
        print(f"Nombre y Apellido: {self.__nombre_apellido}\n Direccion: {self.__direccion}\n Numero de cliente: {self.__nro_cliente}\n Fecha Alta: {self.__fecha_alta}\n Fecha Baja: {self.__fecha_baja}" )   
        
    def eliminar_cliente(self)->None:
        self.__fecha_baja = date.today()          
        
                