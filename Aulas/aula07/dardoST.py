import streamlit as st
import time

st.title("Simulação de lançamento de Dardos")

'''
Simulação de lançamento de três dardos. O objetivo de aplicativo e mostrar o dardo com a maior distância
'''

st.header("Inserir as distâncias dos dardos lançados.")

if "num_dardos" not in st.session_state:
    st.session_state.num_dardos = 3
    
col1, col2, col3 = st.columns(3)
    
with col1:
    if st.button("➕ Adicionar Dardos"):
        st.session_state.num_dardos += 1

with col2:
    if st.button("➖ Remover Dardos"):
        st.session_state.num_dardos -= 1
    
with col3:
    if st.button("🔃 Reiniciar Dardos"):
        st.session_state.num_dardos -= st.session_state.num_dardos
        st.rerun()
    

distancia = []

for i in range(st.session_state.num_dardos):
    valor = st.number_input(f"Distância do dardo {i+1}°: ", step=0.1, min_value=0.0)
    distancia.append(valor)

if any(distancia):
    distancia.sort(reverse=True)
    st.markdown('''<h2 style="color: darkgreen;"><strong>Ranking das distâncias:</strong></h2>''', unsafe_allow_html=True)
    for pos, d in enumerate(distancia, start=1):
        st.write(f"{pos}° lugar: {d:.2f} m")
else:
    st.info("Digite uma distância para ver o ranking")