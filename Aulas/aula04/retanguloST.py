import streamlit as st  #Framework
import math as mt       #biblioteca

#Problema Retângulo
TITULO = "Problema Retângulo"
st.title(TITULO)

#Entrada de dados 
base = st.number_input("Digite a base do retângulo: ",min_value=0.0,format="%.1f")
altura = st.number_input("Digite a altura do retângulo: ",min_value=0.0,format="%.1f")

#Processamento de dados 
area = base * altura 
perimetro = 2 * base + altura * 2
#diagonal = (base**2 + altura**2)**0.5
x = mt.pow(base,2) + mt.pow(altura,2)
diagonal = mt.sqrt(x)

#Saída de dados
st.write(f"A área do retângulo é: {area}")
st.write(f"O perímetro do retângulo é: {perimetro}")
st.write(f"A diagonal do retângulo é: {diagonal:.2f}")