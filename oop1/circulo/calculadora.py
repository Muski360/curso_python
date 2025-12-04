class Calculadora:
    PI = 3.14
    
    @staticmethod
    def circunferencia(raio):
        return 2 * Calculadora.PI * raio
    
    @staticmethod
    def area(raio):
        return Calculadora.PI * raio ** 2
