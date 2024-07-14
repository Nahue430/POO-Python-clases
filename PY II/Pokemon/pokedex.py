from pokemon import Pokemon
class Pokedex():
    __lista_nro:int = []
    __lista_pokemones:int =[]
    def __init__(self,nro:int, cantidad_pokemones:int=0) -> None:
        self.__nro = Pokedex.__validar_nro(nro)
        self.__cantidad_pokemones = cantidad_pokemones
        
        
    @classmethod
    def __validar_nro(cls, nro:int):
        if nro in cls.__lista_nro:
            raise Exception("El nro se encuentra en uso")
        else:
            cls.__lista_nro.append(nro)
            return nro
    @property
    def nro(self)->int:
        return self.__nro
    
    @classmethod
    def __cantidad_pokemones(self)->int:
        return len (Pokedex.__lista_pokemones)
    
    @property
    def cantidad_pokemones(self)->int:
        return self.__cantidad_pokemones 
    @cantidad_pokemones.setter
    def cantidad_pokemones(self, nueva_cantidad_pokemones:int):
        self.__cantidad_pokemones = nueva_cantidad_pokemones
        
    def capturar_pokemon(self, pokemon:Pokemon):
        if pokemon not in self.__lista_pokemones:
            self.__lista_pokemones.append(pokemon)
            
    
    def liberar_pokemon(self, pokemon:Pokemon):
        if pokemon in self.__lista_pokemones:
            self.__lista_pokemones.remove(pokemon)
                           
    
           
    
            