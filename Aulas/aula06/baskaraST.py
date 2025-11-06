import streamlit as st 
import math as mt 

st.header("Calculadora de Bhaskara")
st.write("Calculadora de raízes \n de uma equação do segundo grau")
st.write("ax² + bx + c = 0")

#Entrada de dados 
a = text_input = st.number_input("Digite o valor de a:", value=1.0)
b = text_input = st.number_input("Digite o valor de b:", value=0.0)
c = text_input = st.number_input("Digite o valor de c:", value=0.0) 

#Processamento de dados 
if st.button("Calcular raízes"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b**2 - 4*a*c
        if delta < 0:
            st.warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = -b / (2*a)
            st.success(f"A equação possui uma raiz real: x = {raiz:.2f}")
        else:
            raiz1 = (-b + mt.sqrt(delta)) / (2*a)
            raiz2 = (-b - mt.sqrt(delta)) / (2*a)
            st.success(f"A equação possui duas raízes reais: x1 = {raiz1:.2f} e x2 = {raiz2:.2f}")
    except ValueError:
        st.error("Por favor, insira valores numéricos válidos para a, b e c.")