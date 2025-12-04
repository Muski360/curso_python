from streamlit import header, write, button, warning, success, error, text_input
from math import sqrt

header("Calculadora de Bhaskara")
write("Calculadora de raízes \n de uma equação do segundo grau")
write("ax² + bx + c = 0")

#Entrada de dados 
a = text_input("Digite o valor de a:")
b = text_input("Digite o valor de b:")
c = text_input("Digite o valor de c:")

#Processamento de dados 
if button("Calcular raízes"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b**2 - 4*a*c
        if delta < 0:
            warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -b / (2*a)
            success(f"A equação possui uma raiz real: x = {raiz:.2f}")
        else:
            raiz1 = (-b + sqrt(delta)) / (2*a)
            raiz2 = (-b - sqrt(delta)) / (2*a)
            success(f"A equação possui duas raízes reais: x1 = {raiz1:.2f} e x2 = {raiz2:.2f}")
    except ValueError:
        error("Por favor, insira valores numéricos válidos para a, b e c.")