from cliente import Cliente
from producto import Producto
from descuento import Descuento
from datetime import datetime

class Compra():
    def __init__(self,cliente:Cliente) -> None:
        self.__cliente = cliente
        self.__fecha_hora = datetime.now()
        self.__cantidad_productos = []
        self.__compra_facturada = False
        self.__monto_facturado = float(0)
        self.__monto_total = float(0)
    
    
    @property
    def cliente(self)-> Cliente:
        return self.__cliente
    @cliente.setter
    def cliente(self, nuevo_cliente:Cliente):
        self.__cliente = nuevo_cliente
        
    @property
    def fecha_hora(self)-> datetime:
        return self.__fecha_hora
    
    @property
    def cantidad_productos(self)->list:
        return self.__cantidad_productos
    
    @property
    def compra_facturada(self)->bool:
        return self.__compra_facturada
    
        
    @property
    def monto_facturado(self)->float:
        return self.__monto_facturado
    @monto_facturado.setter
    def monto_facturado(self, nuevo_monto_facturado:float):
        self.__monto_facturado = nuevo_monto_facturado
        
    @property
    def monto_total(self)->float:
        return self.__monto_total    
        
    
    
    def __str__(self) -> str:
        print(f"Cliente: {self.__cliente}\n Fecha y hora: {self.__fecha_hora}\n Cant. Porductos {self.__cantidad_productos}\n Monto facturado: {self.__monto_facturado}")  
    
    def calcular_monto_total(self) -> None:
        self.__monto_total = sum([producto.precio_unitario for producto in self.__cantidad_productos]) 
                 
    def facturar_compra(self) -> None:
        self.__monto_total = Descuento.pago_con_comunidad(self.__monto_total)
    
    def add_producto(self, producto:Producto)->None:
        self.__cantidad_productos.append(producto)        
        
    def remove_producto(self, producto:Producto)->None:
        self.__cantidad_productos.remove(producto)  
        
    
              
        
        
        