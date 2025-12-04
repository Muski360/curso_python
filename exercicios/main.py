import streamlit as st
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @staticmethod
    def mais_velho(p1, p2):
        if p1.idade > p2.idade:
            return p1
        elif p2.idade > p1.idade:
            return p2
        else:
            return None  
        
class funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    @staticmethod
    def salario_medio(f1, f2):
        return (f1.salario + f2.salario) / 2

st.set_page_config(page_title="Programa com duas funções", page_icon="👨‍👨")
st.title("Programa com duas funções")

col1, col2 = st.columns(2)

with col1:
    st.header("Função 1: Pessoa mais velha")
    n1 = st.text_input("Nome da primeira pessoa:", key="nome1")
    i1 = st.number_input("Idade da primeira pessoa:", min_value=1, max_value=120, step=1, key="idade1")
    n2 = st.text_input("Nome da segunda pessoa:", key="nome2")
    i2 = st.number_input("Idade da segunda pessoa:", min_value=1, max_value=120, step=1, key="idade2")
    if st.button("Enviar!", key="enviar1"):
            p1 = Pessoa(n1, i1)
            p2 = Pessoa(n2, i2)
            resultado = Pessoa.mais_velho(p1, p2)
            if resultado is None:
                st.info("As duas pessoas têm a mesma idade!")
            else:
                st.success(f"A pessoa mais velha é {resultado.nome}")
with col2:
    st.header("Função 2: Calcular Salário Médio")
    n1 = st.text_input("Nome da primeira pessoa:", key="nome3")
    i1 = st.number_input("Salário do funcionário 1:", min_value=0.1, key="salario1")
    n2 = st.text_input("Nome da segunda pessoa:", key="nome4")
    i2 = st.number_input("Salário do funcionário 2:", min_value=0.1, key="salario2")
    if st.button("Enviar!", key="enviar2"):
            p1 = funcionarios(n1, i1)
            p2 = funcionarios(n2, i2)
            st.success(f"O salário médio é: {funcionarios.salario_medio(p1, p2)}")