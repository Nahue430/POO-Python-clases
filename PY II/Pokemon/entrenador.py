from pokedex import Pokedex

class Entrenador():
    def __init__(self,nombre:str, es_entrenador_pokemon:bool, pokedex:Pokedex=None) -> None:
        self.__nombre = nombre
        self.__es_entrenador_pokemon = Entrenador.__calcular_es_entrenador_pokemon()
        self.__pokedex = pokedex
    
    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre
        
    def __calcular_es_entrenador_pokemon(self) -> bool:
        return self.__pokedex is not None and self.__Pokedex.cantidad_pokemones > 0  
    
    @property
    def es_entrenador_pokemon(self)->bool:
        return self.__es_entrenador_pokemon
    @es_entrenador_pokemon.setter
    def es_entrenador_pokemon(self, nuevo_es_entrenador_pokemon:bool):
        self.__es_entrenador_pokemon = nuevo_es_entrenador_pokemon
    
    
    def __str__(self) -> str:
        return (f"Nombre: {self.nombre}\n Cantidad pokemones: {Pokedex.cantidad_pokemones}")        
  
             