import streamlit as st

# Funções de conversão
def Celsius_Fahrenheit(c):
    return (c * 9/5) + 32

def Celsius_Kelvin(c):
    return c + 273.15

def Fahrenheit_Celsius(f):
    return (f - 32) * 5/9

def Fahrenheit_Kelvin(f):
    return (f - 32) * 5/9 + 273.15

def Kelvin_Celsius(k):
    return k - 273.15

def Kelvin_Fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


# Sidebar
opcao_selecionada = st.sidebar.radio(
    "Selecione a escala de entrada:",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

# Entrada de dados
temp = st.number_input("Valor de temperatura:", format="%.2f", step=1.0)

# Processamento
if st.button("Converter 🌡"):
    if opcao_selecionada == "Celsius":
        st.write(f"{temp}°C em Fahrenheit: {Celsius_Fahrenheit(temp):.2f} °F")
        st.write(f"{temp}°C em Kelvin: {Celsius_Kelvin(temp):.2f} K")

    elif opcao_selecionada == "Fahrenheit":
        st.write(f"{temp}°F em Celsius: {Fahrenheit_Celsius(temp):.2f} °C")
        st.write(f"{temp}°F em Kelvin: {Fahrenheit_Kelvin(temp):.2f} K")

    elif opcao_selecionada == "Kelvin":
        st.write(f"{temp} K em Celsius: {Kelvin_Celsius(temp):.2f} °C")
        st.write(f"{temp} K em Fahrenheit: {Kelvin_Fahrenheit(temp):.2f} °F")
