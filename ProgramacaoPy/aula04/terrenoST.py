import streamlit as st

st.title("Problema Terreno")
st.write("Digite a largura do terreno em metros:")
largura = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
st.write("Digite o comprimento do terreno em metros:")
comprimento = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
st.write("Digite o valor do metro quadrado em reais:")
valor_m2 = st.number_input("Valor do metro quadrado (R$):", min_value=0.0, format="%.2f")

area = largura * comprimento
preco = area * valor_m2

st.write(f"A área do terreno é: {area:.2f} m²")
st.write(f"O preço do terreno é: R$ {preco:.2f}")