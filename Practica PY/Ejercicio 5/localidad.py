



class Localidad():
    lista_cod_postal = []
    def __init__(self, nombre:str, cod_postal:int) -> None:
        self.__nombre = nombre
        self.__cod_postal: int = Localidad.validar_cod_postal(cod_postal)
    
    
    @classmethod
    def validar_cod_postal(cls, cod_postal):
        if cod_postal in Localidad.lista_cod_postal:
            raise Exception("El codigo postal se encuentra ingresado")    
        else:
            Localidad.lista_cod_postal.append(cod_postal)
            
    @property
    def nombre(self)-> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @property
    def cod_postal(self)->int:
        return self.__cod_postal
    @cod_postal.setter
    def cod_postal(self, nuevo_cod_postal):
        self.__cod_postal = nuevo_cod_postal            