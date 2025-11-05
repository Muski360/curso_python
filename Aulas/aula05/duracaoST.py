import streamlit as st

TITULO = "Calculadora de Duração de Tempo"
st.set_page_config(page_title=TITULO, page_icon="⏱️")
st.title("Calculadora de duração de tempo.")

#Entrada de dados
tempo = st.number_input("Insira o tempo em segundos:", min_value=0, step=1, help="Digite o tempo total em segundos que deseja converter.")
#Processamento de dados

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60
#Saída de dados
st.markdown(f"<h2 style='text-align: center;'>Resultados:", unsafe_allow_html=True)
st.write(f"O tempo de {tempo} segundos corresponde a {horas} horas, {minutos} minutos e {segundos} segundos.")