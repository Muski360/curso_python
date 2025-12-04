import streamlit as st

st.title("Teste de login no Streamlit")

USUARIO = "clara"
SENHA = "murilo123"

usuario_entrada = st.text_input("Nome do usuário: ")
senha_entrada = st.text_input("Senha: ", type = "password")

botao = st.button("Entrar")

max_tentativas = 3

if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0

if botao is True:
    if st.session_state.tentativas >= max_tentativas:
        st.error("Máximo de tentativas atingidos. Acesso bloqueado.")
    else:
        while st.session_state.tentativas < max_tentativas:
            if usuario_entrada == USUARIO and senha_entrada == SENHA:
                st.success("Login bem-sucedido!")
                st.session_state.tentativas = 0
                break
            else:
                st.session_state.tentativas += 1
                st.error(f"Credenciais inválidas. tentativa {st.session_state.tentativas} de {max_tentativas}")
                break
            