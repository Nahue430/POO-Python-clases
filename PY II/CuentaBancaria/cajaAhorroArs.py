from cuentaBancaria import CuentaBancaria

class CajaAhorroArs(CuentaBancaria):
    tasa_interes = 0.001
    def depositar_intereses(self):
        intereses = self._monto * CajaAhorroArs.tasa_interes
        self.depositar(intereses)
        return intereses
    
        