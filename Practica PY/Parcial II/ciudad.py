from hotel import Hotel

class Ciudad():

    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__hoteles = []

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

    def add_hotel(self, hotel: Hotel):
        self.__hoteles.append(hotel)

    def remove_hotel(self, hotel: Hotel):
        self.__hoteles.remove(hotel)

    def __str__(self) -> str:
        return self.get_nombre()