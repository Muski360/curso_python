class Terreno:
    __largura: float
    __comprimento:float
    
    @property
    def largura(self):
        return self.__largura
    @largura.setter
    def largura(self, largura: float):
        self.__largura = largura