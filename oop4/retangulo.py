class Retangulo:
    __base = float
    __altura = float

    @property
    def base(self):
        pass
    
    @base.setter
    def base(self, base:float):
        self.__base = base
    
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura:float):
        self.__altura = altura
        
    def __init__(self, base:float, altura:float):
        self.altura(altura)
        self.base(base)
        
        
    def area(self) -> float:
        return self.altura() * self.base()
    
    def perimetro(self) -> float:
        return (self.altura() * 2) + (self.base() * 2)
    
    def diagonal(self) -> float:
        from math import sqrt
        
        return sqrt(pow(self.base()), 2) + pow(self.altura())
    
    
    def dadosRetangulo(self) -> str:
        saida = f"Area = {self.area()}\n Perimetro = {self.perimetro()}\n Diagonal = {self.diagonal}"
        return saida
    
#Entrada de dados
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retangulo: "))

#Instanciar o objeto do tipo retangulo

retangulo = Retangulo(base, altura)

print(retangulo.dadosRetangulo())
