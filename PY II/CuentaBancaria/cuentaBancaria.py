from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    __lista_CBU = []
    @abstractmethod
    def __init__(self,CBU:str, moneda:str, monto:float) -> None:
        self._CBU = CuentaBancaria.__validar_CBU(CBU)
        self._moneda = moneda
        self._monto = monto
    
    @classmethod
    def __validar_CBU(cls, CBU:str)->str:
        if CBU in cls.__lista_CBU:
            raise Exception("El CBU se encuetra registrado")
        else:
            cls.__lista_CBU.append(CBU)
            return CBU
    
    @property
    def CBU(self)->str:
        return self._CBU
    
    @property
    def moneda(self)->str:
        return self._moneda
    @moneda.setter
    def moneda(self, nueva_moneda:str):
        self._moneda = nueva_moneda
    
    @property
    def monto(self)->float:
        return self._monto
    @monto.setter
    def monto(self, nuevo_monto:float):
        self._monto = nuevo_monto
        
    def depositar(self, monto:float)->float:
        resultado = self.monto + monto
        return resultado
    
    def retirar(self, monto:float)->float:
        if monto > self._monto:
            raise Exception("Dinero insuficiente para retirar")
        else:
            resultado = self.monto - monto
            return resultado
        
           
                            
        
        