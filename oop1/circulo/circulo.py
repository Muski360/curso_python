import os
os.system("cls")

PI = 3.14

raio = float(input("Digite o valor do raio: "))

#Processamento de dados
circuferencia = 2 * PI * raio
volume = (4/3) * PI * raio**3
area = PI * raio ** 2

#Saída de dados
print(f"Circuferencia: {circuferencia:.2f}\nÁrea: {area}\nPI: {PI}")