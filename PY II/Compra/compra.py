from prodcuto import Producto
from descuento import Descuento
from datetime import *


class Compra():
    
    def __init__(self) -> None:
        self.__hora = datetime.now()
        self.__fecha = date.today()
        self.__lista_productos =[]
        
    
    @property
    def monto_con_descuento(self)->float:
        monto_total_con_descuento = self.calcular_monto_total - (self.calcular_monto_total - Descuento.calcular_monto_descuento(self.__lista_productos))
        return monto_total_con_descuento
    
    
    @property
    def hora(self)->time:
        return self.__hora
    @hora.setter
    def hora(self,nueva_hora:time):
        self.__hora = nueva_hora
        
    @property
    def fecha(self)->date:
        return self.__fecha
    @fecha.setter
    def fecha(self,nueva_fecha:date):
        self.__fecha = nueva_fecha
    
   
    #Atributo calculado para sumar los montos de la lista en base el monto del producto en class Producto
    @property
    def calcular_monto_total(self)->float:
        return sum(producto.monto for producto in self.__lista_productos)
            
    
    #Metodo calculado para contabilizar la cantidad de productos en la lista
    @property
    def calcular_cantidad_productos(self)->int:
        return len(self.__lista_productos)
    
    
    #Metodo agregar producto
    def add_producto(self,porducto:Producto):
        self.__lista_productos.append(porducto)
    
    #Metodo remover producto de la lista
    def remove_producto(self,producto:Producto):
        if producto in self.__lista_productos:
            self.__lista_productos.remove(producto)        
        
        
    
    
    

