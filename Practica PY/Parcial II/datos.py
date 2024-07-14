from ciudad import Ciudad
from hotel import Hotel
from pais import Pais
from usuario import Usuario
from viaje import Viaje
from estadia import Estadia

from datetime import date

#creo hoteles...
hoteles = [Hotel('Grand Hotel De La Ville', 140.0), 
            Hotel('Hotel Miramare', 120.0), 
            Hotel('The Gate Hotel', 100.0), 
            Hotel('Martis Palace Hotel Rome', 150.0)]

#creo ciudades y le agrego hoteles...
sorrento = Ciudad('Sorrento')
sorrento.add_hotel(hoteles[0])
sorrento.add_hotel(hoteles[1])

roma = Ciudad('Roma')
sorrento.add_hotel(hoteles[3])

londres = Ciudad('Londres')
sorrento.add_hotel(hoteles[2])

#creo paises y le agrego ciudades...
italia = Pais('Italia')
italia.add_ciudad(sorrento)
italia.add_ciudad(roma)

inglaterra = Pais('Inglaterra')
inglaterra.add_ciudad(londres)

paises = [italia, inglaterra]

#creo un usuario...
usuario_loggeado = Usuario('ppaez', 'ads123')

#creo un viaje...
italia_2019 = Viaje('Italia 2019', date(2019,7,6), date(2019,7,20))
#agrego estadias al viaje...
italia_2019.add_estadia(Estadia(date(2019,6,7), date(2019,7,14), hoteles[1]))
italia_2019.add_estadia(Estadia(date(2019,7,14), date(2019,7,20), hoteles[2]))
#agrego viaje al usuario...
usuario_loggeado.add_viaje(italia_2019)