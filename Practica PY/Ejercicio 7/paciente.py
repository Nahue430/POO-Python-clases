class Paciente():
    lista_nro_documento = []
    def __init__(self, nombre:str, tipo_documento:str, obra_social:str, nro_documento:str) -> None:
        self.__nombre = nombre
        self.__tipo_documento = tipo_documento
        self.__obra_social = obra_social
        self.__nro_documento = Paciente.validar_nro_documento(nro_documento) 
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
        
    @property
    def tipo_documento(self)->str:
        return self.__tipo_documento
    @tipo_documento.setter
    def tipo_documento(self, nuevo_tipo_documento:str):
        self.__tipo_documento = nuevo_tipo_documento 
        
    @property
    def obra_social(self)->str:
        return self.__obra_social
    @obra_social.setter
    def obra_social(self, nueva_obra_social:str):
        self.__obra_social = nueva_obra_social 
    
    @property
    def nro_documento(self)->str:
        return self.__nro_documento           
    
    
    
    
    @classmethod
    def validar_nro_documento(cls,nro_documento:str)->str:
        if nro_documento in cls.lista_nro_documento:
            raise Exception ("El numero ya se encuentra registrado")
        else:
            cls.lista_nro_documento.append(nro_documento)
            return nro_documento