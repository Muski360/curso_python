class Produto:
    #Atributos
    nome:str
    preco:float
    saldo:int    
    
    def valorTotalEmEstoque(self) -> float:
        return self.preco * self.saldo
    
    def adicionarProdutos(self, quantidade) -> int:
        return self.saldo
    
    def removerProdutos(self, quantidade) -> int:
        self.saldo = self.saldo - quantidade
        return self.saldo
    
    def dadosDoProduto(self) -> str:
        saida = f'''Dados do produto:
        \tNome do produto: {self.nome}
        \tValor de compra do produto: R$ {self.preco}
        \tQuantidade em estoque: {self.saldo}
        \tValor total de estoque: R$ {self.valorTotalEmEstoque():.2f}'''
        return saida
        