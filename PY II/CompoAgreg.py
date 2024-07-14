#composicion pintado
#from adress import Adress
class User():
    def __init__(self,name:str, city:str, adress:str) -> None: #aca paso los atributos de clase adress city y adress
        self.__name = name
        self.__adress = Adress = Adress(city, adress)#aca los vuelvo a pasar a los atributos
        pass
    
    @property
    def city(self)->str:
        return self.__name
    @property
    def adress(self)->Adress:
        return self.__adress    
    
    
    
#agregacion sin pintar
#from engine import Engine

class Car():
    def __init__(self, engine:Engine) -> None:#aca paso el objeto entero
        self.__engine = Engine = engine 
        
    @property
    def engine(self)->Engine:
        return self.__engine
    
    @property#paso los metodos
    def move(self):
        return self.engine.start
    @ property #paso los metodos
    def stop(self):
        return self.engine.stop      