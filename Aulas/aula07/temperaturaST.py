import streamlit as st 

def Celsius_Fahrenheit(t):
    return (t * 1.8) + 32
def Celsius_Kelvin(t):
    return (t + 273.15)
def Kelvin_Fahrenheit(t):
    return Celsius_Fahrenheit(Kelvin_Celsius(t))
def Fahrenheit_Celsius(t):
    return (t - 32) * 1.8
def Fahrenheit_Kelvin(t):
    return ((t - 32) * 5/9) + 273.15
def Kelvin_Celsius(t):
    return t - 273.15

#Problema temperatura
st.sidebar.title("Conversor de Temperatura")
st.title("🌡️Conversor de Temperatura")
st.sidebar.markdown("Converte temperaturas entre Celsius, Fahrenheit e Kelvin.")

# celsius_selecionado = st.sidebar.checkbox("Celsius", key="Temp_Celsius")
# fahrenheit_selecionado = st.sidebar.checkbox("Fahrenheit", key="Temp_Fahrenheit")
# kelvin_selecionado = st.sidebar.checkbox("Kelvin", key="Temp_Kelvin")

opcao_selecionada = st.sidebar.radio(options=["Celsius"], ["Fahrenheit"], ["Kelvin"])
#Entrada de dados
temp = st.number_input("Valor de temperatura",format="%.2f", step=1.0)


#Processamento de dados
if st.button("Converter", icon='🌡'):
    if celsius_selecionado:
        st.write(f"{temp}°C em Fahrenheit: {Celsius_Fahrenheit(temp):.2f}°F")
        st.write(f"{temp}°C em Kelvin: {Celsius_Kelvin(temp):.2f}°F")
    elif fahrenheit_selecionado:
        st.write(f"{temp}°F em Celsius: {Fahrenheit_Celsius(temp):.2f} °C")
        st.write(f"{temp}°F em Kelvin: {Fahrenheit_Kelvin(temp):.2f} °K")
    else:
        st.write(f"{temp}K em Celsius: {Kelvin_Celsius(temp):.2f} °C")
        st.write(f"{temp}K em Fahrenheit: {Kelvin_Fahrenheit(temp):.2f} °F") 