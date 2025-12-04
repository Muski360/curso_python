from calculadora import Calculadora

raio = float(input("Digite o valor do raio: "))

circ = Calculadora.circunferencia(raio)
area = Calculadora.area(raio)

print(f"Circunferência: {circ:.2f}")
print(f"Área: {area:.2f}")
print(f"PI: {Calculadora.PI}")