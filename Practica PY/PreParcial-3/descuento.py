class Descuento():

    ___descuento_comunidad: float = float(0.10)

    @staticmethod
    def pago_con_comunidad(monto: float) -> float:
        '''
            Retorna el monto total de la compra con el 
            descuento aplicado por tener comunidad.
        '''
        return monto - (monto * Descuento.___descuento_comunidad)