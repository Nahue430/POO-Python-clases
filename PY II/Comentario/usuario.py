class Usuario():
    __lista_nombre_usuario = []
    def __init__(self,nombre_usuario:str, nivel:int) -> None:
        self.__nombre_usuario = Usuario.__validar_nombre_usuario(nombre_usuario)
        self.__nivel = nivel
        
        
    
    @classmethod
    def __validar_nombre_usuario(cls,nombre_usuario:str):
        if nombre_usuario in cls.__lista_nombre_usuario:
            raise Exception ("El nombre de usuario se encuentra registrado")
        else:
            cls.__lista_nombre_usuario.append(nombre_usuario)
            return nombre_usuario
    
    @property
    def nombre_usuario(self)->str:
        return self.__nombre_usuario
    
    @property
    def nivel(self)->int:
        return self.__nivel
    @nivel.setter
    def nivel(self, nuevo_nivel:int):
        self.__nivel = nuevo_nivel
        
        
    def __str__(self) -> str:
        return (f"Nombre usuario:{self.nombre_usuario}\nNivel:{self.nivel}")    
                