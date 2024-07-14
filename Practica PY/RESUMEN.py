
## TIPO DE VARIABLE

#   +   -   ningún guión  -  pública
#   #   -   un guión      -  protegido
#   -   -   dos guiones   -  privada

####################################################################################################################

## AUTOINCREMENTAL

# NO SE RECIBE COMO PARÁMETRO
# Un atributo de clase que se inicia en 0
# Una método de clase que sirve para aumentar en 1 ese atributo de clase
# Un atributo de instancia que utiliza ese método de clase
# yo le pondría un getter

"""
class Viaje():

    __ant_nro_viaje:int = 0 -----------------------------------------------> ATRIBUTO DE CLASE

    def __init__(self, NO LO RECIBE!! ) -> None:

        self.__nro_viaje: int = Viaje.__generar_prox_nro_viaje() ----------> MÉTODO DE INSTANCIA UTILIZANDO EL MÉTODO DE CLASE

    @classmethod ----------------------------------------------------------> MÉTODO DE CLASE
    def __generar_prox_nro_viaje(cls) -> int:
        cls.__ant_nro_viaje += 1
        return cls.__ant_nro_viaje 

"""

## UNIQUE

# PUEDE RECIBIRSE O NO COMO PARÁMETRO (en este caso si pero en el caso del ISBN del libro no por ejemplo..)
# Un atributo de clase que es una lista vacía
# Un método de clase que sirve para validar lo que va a ingresar en esa lista
# Un atributo de instancia que utiliza ese método de clase
# Se le hace getter y setter (validando otra vez lo ingresado)

"""
class Usuario():

    __lista_user_name = [] -----------------------------------------------------> ATRIBUTO DE CLASE

    def __init__(self, user_name:str  ACÁ SÍ LO RECIBE! ) -> None:
        self.__user_name:str = Usuario.__validar_user_name(user_name) ----------> MÉTODO DE INSTANCIA UTILIZANDO EL MÉTODO DE CLASE
        
    @classmethod ---------------------------------------------------------------> MÉTODO DE CLASE
    def __validar_user_name(cls, user_name:str) -> str:
        if(user_name in cls.__lista_user_name):
            raise Exception("Nombre de usuario en uso! Escoja otro.")
        Usuario.__lista_user_name.append(user_name)
        return user_name

    @property
    def user_name(self) -> str:
        return self.__user_name
    @user_name.setter
    def user_name(self, nuevo_user_name): --------------------------------------> GETTER Y SETTER VALIDANDO LO INGRESADO (ojo que es readonly)
        if nuevo_user_name in Usuario.__lista_user_name:
            raise Exception("User name ya existente!")
        Usuario.__lista_user_name.append(nuevo_user_name)
        self.__user_name = nuevo_user_name
"""

## CALCULADO

# NO LO RECIBE NI SE LE HACE ATRIBUTO
# Se le hace solo un getter donde se calcula algo

""" EDAD
class Persona():
    
    @abstractmethod
    def __init__(self, NO LO RECIBE! ) -> None:
        
        NADA

    @property
    def edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if hoy.month <= self.fecha_nacimiento.month:
            if hoy.day < self.fecha_nacimiento.day:
                edad -= 1
        return edad
"""

""" CANTIDAD DE HORAS
    @property
    def cant_horas(self):
        horas = self.__hora_entrada.hour - self.__hora_salida.hour
        minuto = self.__hora_entrada.minute - self.__hora_salida.minute
        if minuto > 30:
            horas += 1
        return horas
"""


## IGUALADO A ALGO ENTRE COMILLAS (ej 3 Libro - autor = 'Unknow')

# LO RECIBIMOS COMO PARÁMETRO Y LO PONEMOS ÚLTIMO
# Le asignamos lo recibio al atributo de isntancia
# Le hacemos getter y setter

"""
class Libro():

    def __init__(self, autor:str='Unknow') -> None:
        self.__autor:str = autor

    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor
"""

## IGUALADO A FALSE (ej usuario ejercicio 3)

# No lo recibe
# Se pone el atributo de instancia igualado a false
# Ojo que en el ejercicio 3 no le hace setter.. pero porque tiene un método que le controla el estado


## SUBRAYADO

# ES UN ATRIBUTO DE CLASE
# Se iguala a algo razonable a cada caso.. no sé bien..add()
# Se le puede hacer getter y setter (?)


# #class Inscripcion():
#     __prox_nro = int(0) ----> este seria el atributo de clase
    
#     def __init__(self, aspirante:Aspirante, carrera:Carrera) -> None:
#         self.__nro = Inscripcion.get_prox_nro()
#         self.__fecha_inscripcion = date.today
#         self.__inscripcion_activa = True
#         self.__aspirante: Aspirante = aspirante
#         self.__carrera: Carrera = carrera
    
    
#     @classmethod ----> aca utilizo el atributo de clase para hacer mi metodo
#     def get_prox_nro(cls):
#         cls.__nro += 1
#         return cls.__prox_nro
#     @property -------> solo le hago el getter
#     def nro(self)-> int:
#         return self.__nro

####################################################################################################################


## ADD - REMOVE

# NO LO RECIBE COMO PARÁMETRO
# Se le asigna una lista vacía al atributo al que apuntan los métodos
# Solo se le hace el getter
# Los 2 métodos son para agregar o remover (sería el setter)
# No se pone en el método mágico (?)

"""
from titulo import Titulo

class Aspirante():

    def __init__(self, NO LO RECIBE!) -> None:

        self.__titulo = []

    @property
    def titulo(self):
        return self.__titulo                # ver si es solo getter
    
    def add_titulo(self, titulo:Titulo):
        self.__titulo.append(titulo)

    def remove_titulo(self, titulo:Titulo):
        self.__titulo.remove(titulo)
"""

####################################################################################################################

## AGREGACIÓN

# 
# 
# 

####################################################################################################################

## ABSTRACT METHOD

# Se importa desde "abc" 2 cosas: "ABC" y "abstractmethod"
# El "ABC" para poner en el paréntesis de la clase
# El "abstractmethod" para poner antes de hacer el constructor

"""
from abc import ABC,abstractmethod

class Persona(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
    
"""

####################################################################################################################

## AL IMPORTAR ALGO (ej tipodocumento)

# Recibe como parámetro (y es del tipo de la clase de la cual importa)
# Se le hace un atributo de instancia, se iguala a lo que recibe
# Se le hace getter y setter

# Si la flecha llega

####################################################################################################################

## USAR GETTERS

# Siemper que estén hechos se van a usar tanto en el método __str__ como en cualquier otro método !!!!!!!

####################################################################################################################

## READONLY 

# SE LE HACE INSTANCIA
# SOLO UN GETTER
# VER BIEN SI LO RECIBE

#################################################################################################################################
#SORTED KEY LAMBDA
#  def historial_viaje():
#    viajes_ordenados = sorted(usuario_loggeado.viajes, key=lambda x: x.nro_viaje, reverse= True) 
#    for viaje in viajes_ordenados:
#        print(viaje)
#
#    #### Otra opcion ####
#    def historial_viaje():
#        viajes_ordenados = sorted(usuario_loggeado.viajes, key=lambda x: x.nro_viaje, reverse= True) 
#        return viajes_ordenados
#SORTED KEY LAMBDA EN METODO
#def ordenar_por_clave(self, clave):
#        # Usar sorted con una función lambda para ordenar por la clave proporcionada
#        self.lista = sorted(self.lista, key=lambda x: x[clave])

#    def mostrar_lista(self):
#        for item in self.lista:
#            print(item)

#carreras_ord_fecha = sorted(carreras, key=lambda x: x.fecha_comienzo)


# ENUMERATE
#for i,titulo in enumerate(titulos,1):
#        print(f"{i} - {titulo.nombre}")

#ENUMERATE EN METODO
#def mostrar_con_indices(self):
#        for indice, valor in enumerate(self.lista):
#            print(f'Índice: {indice}, Valor: {valor}')

### DATE TIME ###
## from datetime import date
"""
Para fecha de hoy o alta
datetime.today()   ## Tira fecha unicamente
.day .moth .year

@property
def date(self) -> str:
    return f"{self.__fecha_hora.day}/{self._fecha_hora.month}/{self._fecha_hora.year}"


"""

### DATE TIME ###
## from datetime import datetime
#"""
#datetime.now()    ##Tira la fecha y hora.
#.hour .minute .second  

#@property
#def time(self) -> str:
#    return f"{self._fecha_hora.hour}:{self._fecha_hora.minute} hs." 

