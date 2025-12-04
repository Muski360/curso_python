class triangulo:
    #Atributos
    a:int
    b:int
    c:int

    #Métodos da classe
    def area(self) ->float:
        from math import sqrt
        p = (self.a +self.b +self.c)/2
        area = sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return area