import streamlit as st

def verificartriangulo(l1, l2, l3):
    if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
        return False
    else:
        return True
def mostrartriangulo(l1, l2, l3):
    lmin = min(l1, l2, l3)
    lmax = max(l1, l2, l3)
    lsobra = (l1 + l2 + l3) - lmin - lmax 
    dados = [lmin, lmax, lsobra]
    st.area_chart(dados, use_container_width=True, height=300, color = '#A020F0')

def areatrap(l1, l2, l3):
    area = (l1 + l2) * l3 / 2
    return area

st.header("Programa de calcular um triângulo.")
st.set_page_config(page_title="Verificador de triângulo", page_icon="⏱️")

col1, col2, col3 = st.columns(3)

l1 = col1.number_input("Digite o 1° lado do triângulo", min_value=0.1, step=1.0)
l2 = col2.number_input("Digite o 2° lado do triângulo", min_value=0.1, step=1.0)
l3 = col3.number_input("Digite o 3° lado do triângulo", min_value=0.1, step=1.0)

if st.button("Calcular!"):
    if verificartriangulo(l1, l2, l3):
        if l1 != l2:
            st.success(f"✅ Forma um triângulo! O perímetro é {l1 + l2 + l3:.2f}")
            mostrartriangulo(l1, l2,l3)
        else:
            st.info("Essa forma aí né nada nao")
    else:
        st.error("❌ Isso não é um triângulo!")
        st.info(f"Cálculo da área do trapézio {areatrap(l1, l2, l3):.2f}")