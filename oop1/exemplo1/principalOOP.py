import trianguloOOP as tl

#Instanciar a classe 
trianguloX = tl.triangulo()
trianguloY = tl.triangulo()

#Entrada de dados 
print("Digite as medidas do triângulo X")
trianguloX.a = int(input("Digite a medida A:"))
trianguloX.b = int(input("Digite a medida B:"))
trianguloX.c = int(input("Digite a medida C:"))
print("Digite as medidas do triângulo Y")
trianguloX.a = int(input("Digite a medida A:"))
trianguloX.b = int(input("Digite a medida B:"))
trianguloX.c = int(input("Digite a medida C:"))

#Processamento de dados
areax = trianguloX.area()
areay = trianguloY.area()

#Condicional
if areax > areay:
    saida = "A área do triângulo X é maior que a área do triângulo Y"
elif areay > areax:
    saida = "A área do triângulo Y é maior que a área do triângulo X"
else:
    saida = "As áreas dos triângulos são iguais"

#Saída de dados 
print(f"A área do triângulo X é igual = {areax:.1f}")
print(f"A área do triângulo Y é igual = {areay:.1f}")
print(saida)
