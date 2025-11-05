import streamlit as st

st.set_page_config(page_title="Programa de cálculo de troco", page_icon="💰")
st.title("Programa de cálculo de troco")

#Entrada de dados
numProdutos = st.number_input("Insira o número de produtos que você comprou:", min_value=1, help="Digite a quantidade de produtos que você comprou.")
preco = st.number_input("Insira o preço do produto comprado:", min_value=0.0, format="%.2f", step=0.01, help="Digite o preço único do produto comprado.")

#Processamento de dados
totalCompra = numProdutos * preco

#Entrada de dados
dinheiroRecebido = st.number_input("Insira o valor em dinheiro total: ", min_value=totalCompra, format="%.2f", help="Digite o valor total em dinheiro que você deu ao caixa.")

#Processamento de dados
troco = dinheiroRecebido - totalCompra

#Saída de dados
st.markdown(f"<h2 style='text-align: center;'>Resultados:", unsafe_allow_html=True)
st.write(f"O total da compra é: R$ {totalCompra}")
st.write(f"O troco a ser recebido é: R$ {troco}")