import streamlit as st

st.title("Problema Retângulo")

base = st.number_input("Digite a base do retângulo (em metros):")
altura = st.number_input("Digite a altura do retângulo (em metros):")
area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base**2 + altura**2) ** 0.5
st.write(f"A área do retângulo é: {area} metros quadrados")
st.write(f"O perímetro do retângulo é: {perimetro} metros")
st.write(f"A diagonal do retângulo é: {diagonal:.2f} metros")
