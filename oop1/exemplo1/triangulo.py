#Problema triângulo sem OOP
import os
os.system("cls")
#Entrada de dados
#TRIANGULO X

print("Inserir as medidas do triângulo 1: \n")
ax = int(input("Digite o lado A do triângulo: "))
bx = int(input("Digite o lado B do triângulo: "))
cx = int(input("Digite o lado C do triângulo: "))

#TRIANGULO Y

print("Inserir as medidas do triângulo 2: \n")
ay = int(input("Digite o lado A do triângulo: "))
by = int(input("Digite o lado B do triângulo: "))
cy = int(input("Digite o lado C do triângulo: "))

#Processamento de dados

p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p - bx) * (p - cx)) ** 0.5
p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p - by) * (p - cy)) ** 0.5

if (areax > areay):
    text = "O maior é o **triângulo 1**"
elif (areay > areax):
    text = "O maior é o **triângulo 2**"
else:
    text = "Ou seja, as duas áreas são iguais"

print(f"Área do triângulo 1 = {areax:.3f}\nÁrea do triângulo 2 = {areay:.3f}\n{text}")