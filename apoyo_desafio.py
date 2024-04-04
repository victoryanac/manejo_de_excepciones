from error import DimensionError  


class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta 

#acceso y modificscion de ancho
    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho < 1 or ancho > self.MAX:
                raise DimensionError("Valor de ancho inválido", ancho, Foto.MAX)
            self.__ancho = ancho
        except DimensionError as e:
            self.__ancho = 0
            print(e)


#acceso y modificacicion de alto
    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            if alto < 1 or alto > self.MAX:
                raise DimensionError("Valor de ancho inválido", alto, Foto.MAX)
            self.__ancho = alto
        except DimensionError as h:
            self.__ancho = 0
            print(h)
