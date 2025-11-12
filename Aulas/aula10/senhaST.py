import streamlit as st
import random
from time import perf_counter
import string

st.title("Quebrador de senhas - Teste (educacional)")

senha = st.text_input("Digite sua senha:")
max_attempts = st.number_input("Máximo de tentativas (coloque 0 para ilimitado — cuidado!)", min_value=0, value=100000, step=1000)
usar_caracteres = st.multiselect("Incluir tipos de caracteres", 
                                 ["Letras maiúsculas", "Letras minúsculas", "Dígitos", "Símbolos"], 
                                 default=["Letras maiúsculas", "Letras minúsculas", "Dígitos", "Símbolos"])

if st.button("Enviar senha para teste extremo de tentativa e erro"):
    if not senha:
        st.warning("Digite uma senha antes de iniciar.")
    else:
        # Monta o alfabeto conforme a escolha
        caracteres = ""
        if "Letras maiúsculas" in usar_caracteres:
            caracteres += string.ascii_uppercase
        if "Letras minúsculas" in usar_caracteres:
            caracteres += string.ascii_lowercase
        if "Dígitos" in usar_caracteres:
            caracteres += string.digits
        if "Símbolos" in usar_caracteres:
            caracteres += string.punctuation

        if not caracteres:
            st.error("Selecione pelo menos um tipo de caractere.")
        else:
            quantidade = len(senha)
            tentativa_set = set()
            inicio = perf_counter()
            attempts = 0
            barra = st.empty()
            status = st.empty()
            ultimo = st.empty()

            limite = None if max_attempts == 0 else int(max_attempts)

            st.info("Atenção: isso é apenas para testes. Brute-force de senhas reais é demorado e normalmente inviável.")
            found = False

            while True:
                # Gera tentativa (mais rápida: random.choices retorna lista)
                resultado = ''.join(random.choices(caracteres, k=quantidade))
                attempts += 1

                # evita armazenar duplicatas (set)
                if resultado in tentativa_set:
                    # já tentou antes — pula
                    pass
                else:
                    tentativa_set.add(resultado)
                    ultimo.text(f"Última tentativa: {resultado}")
                    barra.text(f"Tentativas: {attempts}  |  Tentativas únicas armazenadas: {len(tentativa_set)}")
                    elapsed = perf_counter() - inicio
                    status.text(f"Tempo decorrido: {elapsed:.3f} s")

                    if resultado == senha:
                        fim = perf_counter()
                        st.success(f"Senha quebrada! '{resultado}' em {attempts} tentativas — tempo: {fim - inicio:.6f} s")
                        found = True
                        break

                # checa limite de tentativas para não travar
                if limite is not None and attempts >= limite:
                    st.error(f"Limite de {limite} tentativas atingido. Parando.")
                    break

            if not found and (limite is None or attempts < limite):
                st.info("Processo finalizado sem encontrar a senha (provavelmente interrompido).")
