import streamlit as st

#Problema lanchonete 
st.title("Lanchonete do Clodoaldo")
st.header("Menu de opções do restaurante")
st.subheader("Opções de lancher")
st.markdown(
"""
|Código|Descrição do item | Preco  |
|------|------------------|--------|
| 1001 |    X-Burger      |R$ 8,00 |
| 1002 |    X-Senai       |R$ 10,00|
| 1003 |    X-Campeão     |R$ 12,00|
| 1004 |    X-ESP32       |R$ 15,00|
| 1005 |    X-C37         |R$ 18,00|
"""
)
opcao = st.selectbox("Selecione o código do lanche desejado:",
                      options=["1001", "1002", "1003", "1004", "1005"])
codigo = int(opcao) #Converte a string selecionada em número inteiro 
quantidade = st.number_input("DIgite a quantidade desejarda:", min_value=1,step=1)

#Estrutura de controle de seleção
match codigo:
    case 1001:
        preco = 8.00
    case 1002:
        preco = 10.00
    case 1003:
        preco = 12.00
    case 1004:
        preco = 15.00
    case 1005:
        preco = 18.00

#Processamento de dados 
total = preco * quantidade 

#Saída de dados 
st.subheader("Total a pagar: R$ " + (str(total)))