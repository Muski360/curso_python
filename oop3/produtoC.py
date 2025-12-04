import produtoOOP as p

print("Entre com os dados dos produtos: ")
nome = input("Nome: ")
preco = float(input("Preço: R$"))
saldo = int(input("Quantidade: "))

ps = p.Produto(nome, preco, saldo)

print(ps.dadosDoProduto())