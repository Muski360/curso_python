import streamlit as st

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: purple;
        color: white;
        border: none;
        border-radius: 8px;
        height: 3em;
        width: 12em;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #8000ff;
        color: #fff;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Calculadora de Glicose")
st.title("Calculadora de Glicose no Sangue!")

st.markdown("<table><th>Nível de glicose</th><th>Status</th><tr><td>70 mg/dL</td><td>Hipoglicemia</td></tr><tr><td>100 mg/dL</td><td>Normal</td></tr><tr><td>140 mg/dL</td><td>Elevado</td></tr><tr><td>Acima de 140 mg/dL</td><td>Diabetes</td></tr></table>", unsafe_allow_html=True)

# Entrada de dados
qntdGlicose = st.number_input("Insira a quantidade de glicose no sangue (mg/dL):", min_value=0.0, format="%.2f", step=0.1, help="Digite a quantidade de glicose medida no sangue em mg/dL.")
if st.button("Classificar!"):
    # Condição
    if qntdGlicose < 70:
        status = "hipoglicemia"
    elif 70 <= qntdGlicose < 100:
        status = "normal"
    elif 100 <= qntdGlicose <= 140:
        status = "elevado"
    else:
        status = "diabetes"
    
    # Saída de dados
    command = "error" if status == "diabetes" else "warning" if status == "elevado" else "info"
    getattr(st, command)(f"O nível de glicose ({qntdGlicose} mg/dL) é considerado: {status}.")
    if status == "normal":
        st.balloons()