from ciudad import Ciudad

class Pais():

    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__ciudades = []

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

    def add_ciudad(self, ciudad: Ciudad):
        self.__ciudades.append(ciudad)

    def remove_ciudad(self, ciudad: Ciudad):
        self.__ciudades.remove(ciudad)

    def __str__(self) -> str:
        return self.get_nombre()