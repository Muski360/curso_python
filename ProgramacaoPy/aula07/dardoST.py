import streamlit as st

def grafico(distancias):
    """
    Cria um gráfico simples usando apenas listas.
    Cada valor da lista será mostrado como um ponto no gráfico.
    """
    # cada valor vira uma linha 
    dados = []
    for d in distancias:
        dados.append([d])
    st.area_chart(
        dados,
        use_container_width=True,
        height=300,
        color = '#A020F0'
    )

# ===== APP PRINCIPAL =====
st.title("🎯 Simulação de lançamento de Dardos")
st.write("O objetivo é mostrar o dardo com a maior distância.")

# estado inicial
if "num_dardos" not in st.session_state:
    st.session_state.num_dardos = 3

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➕ Adicionar Dardo"):
        st.session_state.num_dardos += 1
with col2:
    if st.button("➖ Remover Dardo") and st.session_state.num_dardos > 1:
        st.session_state.num_dardos -= 1
with col3:
    if st.button("🔃 Reiniciar Dardos"):
        st.session_state.num_dardos -= st.session_state.num_dardos
        st.rerun()

# entradas de distâncias
distancias = []
for i in range(st.session_state.num_dardos):
    valor = st.number_input(
        f"Distância do dardo {i+1}°:",
        step=0.1,
        min_value=0.0,
        key=f"dardo_{i}"
    )
    distancias.append(valor)

# ranking
if any(distancias):
    distanciaorg = sorted(distancias, reverse=True)
    st.markdown('<h2 style="color: darkgreen;">🏆 <strong>Ranking das distâncias:</strong></h2>', unsafe_allow_html=True)
    for pos, d in enumerate(distanciaorg, start=1):
        st.write(f"{pos}º lugar: {d:.2f} m")

    # gráfico
    if st.button("📈 Mostrar gráfico"):
        grafico(distancias)
else:
    st.info("Digite uma distância para ver o ranking.")
