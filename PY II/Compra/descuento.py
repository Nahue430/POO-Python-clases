
from compra import Compra


class Descuento:
    __porcentaje_descuento_monto: float = 0.05  
    __porcentaje_descuento_cantidad: float = 0.10 
    

    @classmethod
    def calcular_monto_descuento(cls) -> float:
        total_monto = Compra.calcular_monto_total
        total_productos = Compra.calcular_cantidad_productos
        
        if total_monto > 10000 and total_productos > 15:
            descuento = total_monto * (cls.__porcentaje_descuento_cantidad + cls.__porcentaje_descuento_monto)
        elif total_monto > 10000:
            descuento = total_monto * cls.__porcentaje_descuento_monto
        elif total_productos > 15:
            descuento = total_monto * cls.__porcentaje_descuento_cantidad
        else:
            descuento = 0.0
        
        return descuento