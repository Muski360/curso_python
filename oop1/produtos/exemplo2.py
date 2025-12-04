import produtoOOP as p

p1 = p.Produto()

p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreço: "))
p1.saldo = int(input("\tQuantidade: "))

print("Dados do prodto:")
print(p1.dadosDoProduto())

q = int(input("Digite o número de produtos a ser adicionado ao estoque: "))
p1.adicionarProdutos(q)

print("-- Dados atualizados --")
print(p1.dadosDoProduto())

q = int(input("Digite o número de produtos a ser removido ao estoque: "))
p1.removerProdutos(q)

print("-- Dados atualizados --")
print(p1.dadosDoProduto())