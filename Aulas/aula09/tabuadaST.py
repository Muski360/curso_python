import streamlit as st

TITULO = "Tabuada"
st.title(TITULO)
st.set_page_config(TITULO)
n = None
try:
    n = int(st.text_input("Deseja a tabuada de qual número?"))
    for i in range(1,11):
        saida = f"{n} X {i} = {n*i}"
        st.write(f"{saida}")
except ValueError:
    if n is None:
        st.warning("Digite algum valor")
    else:
        st.error("Digite somente numero inteiros")