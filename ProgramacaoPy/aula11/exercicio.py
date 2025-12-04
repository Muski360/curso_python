import streamlit as st
def main():
    st.set_page_config(page_title="Cadastro de pessoas", page_icon="👨‍👨")
    st.title("Programa de cadastro de pessoas")
   
    pessoas = []
    idades = []
    alturas = []
   
    cola, colb = st.columns(2)
    if "num_pessoas" not in st.session_state:
        st.session_state.num_pessoas = 1
    with cola:
        if st.button("🧑 Adicionar Pessoa"):
            st.session_state.num_pessoas += 1
    with colb:
        if st.button("❌ Remover Pessoa") and st.session_state.num_pessoas > 1:
            st.session_state.num_pessoas -= 1


    col1, col2, col3 = st.columns(3)


    for i in range(st.session_state.num_pessoas):
        with col1:
            nome = st.text_input(f"Nome da {i+1}° pessoa:", key=f"nome_{i}")
        with col2:
            idade = st.number_input(f"Idade da {i+1}° pessoa:", min_value=1, step=1, key=f"idade_{i}")
        with col3:
            altura = st.number_input(f"Altura da {i+1}° pessoa:", min_value=0.0, step=0.1, max_value=3.0, key=f"altura_{i}")
        pessoas.append(nome)
        idades.append(idade)
        alturas.append(altura)
   
   
    if st.button("Clique aqui para calcular!"):
        if any(nome == "" for nome in pessoas):
            st.error("Digite valores para a pessoa.")
        else:
            nomesmnr16 = []
            media = sum(alturas) / len(alturas)
            st.success(f"A média de altura das pessoas é de {media}")
            mnr16 = 0
            for i in range(len(idades)):
                if idades[i] < 16:
                    mnr16 += 1
                    nomesmnr16.append(pessoas[i])
                   
           
            porcentagem = (mnr16 / len(idades)) * 100
            texto = "\n\n".join([f"{i} - {item}" for i, item in enumerate(nomesmnr16, start=1)])
           
            st.success(f"Quantidade de pessoas que são menores de 16 anos: **{mnr16}** pessoas. "
                       f"Isso corresponde a {porcentagem:.2f}%.\n\n\n\n"
                       f"**São eles:**\n\n{texto}"
                      )
            st.balloons()
           
       
if __name__ == "__main__":
    main()