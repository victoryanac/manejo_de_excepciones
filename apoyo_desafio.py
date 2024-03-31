from error import DimensionError  


class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta 

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        if not (1 <= ancho <= Foto.MAX):
            raise DimensionError("Valor de ancho inválido", ancho, Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        if not (1 <= alto <= Foto.MAX):
            raise DimensionError("Valor de alto inválido", alto, Foto.MAX)
        self.__alto = alto
