#Entrada de dados
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
valor = float(input("Digite o valor do metro quadrado do terreno: "))

#Processamento
area = largura * comprimento
preco = area * valor

#Saída de dados
print(f"A área do terreno é de {area} metros quadrados. O preço do terreno é de R$ {preco:.2f}.")