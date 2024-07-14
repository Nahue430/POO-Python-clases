from cuentaBancaria import CuentaBancaria
from datetime import date

class CajaAhorroUsd(CuentaBancaria):
    def __init__(self, CBU: str, moneda: str, monto: float, fecha_ultima_transferencia_recibida:date) -> None:
        self.__fecha_ultima_transferencia_recibida = CajaAhorroUsd.__validar_transferencia()
        
        super().__init__(CBU, moneda, monto)
    
    @property
    def fecha_ultima_transferencia_recibida(self)->date:
        return self.__fecha_ultima_transferencia_recibida
    @fecha_ultima_transferencia_recibida.setter
    def fecha_ultima_transferencia_recibida(self, nueva_fecha_ultima_transferencia_recibida:date):
        self.__fecha_ultima_transferencia_recibida = nueva_fecha_ultima_transferencia_recibida
    
    def __validar_transferencia(self, nueva_fecha:date)->date:
        if nueva_fecha.month == self.__fecha_ultima_transferencia_recibida.month:
            raise Exception ("No se puede realizar la transferencia")
        else:
            self.__fecha_ultima_transferencia_recibida = date.today()
            return self.__fecha_ultima_transferencia_recibida
                