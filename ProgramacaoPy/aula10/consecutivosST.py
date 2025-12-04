import streamlit as st
#Problema de numeros consecutivos
st.title("Calculadora pares consecutivos")
#Entrada de dados
numero = st.number_input("Digite um numero inteiro", step=1)
botao = st.button("Calcular")
contagem  = 1

if botao:
    if (numero%2) != 0:
        numero += 1
    soma = numero
    while contagem < 5:
        numero += 2
        contagem += 1
        soma += numero
    st.write(soma)
