#Classe conta bancária 

class ContaBancaria:
    
    #Atributos
     
    __numero:int
    __titular:str
    __saldo:float

    #Propriedades para acessar os membros da classe
    
    @property
    def numero(self, numero):
        self.__numero = numero
    @property
    def titular(self, titular):
        self.__titular = titular
    @property
    def saldo(self, saldo):
        self.__saldo = saldo

    #Construtores
    
    def __init__(self, numero:int, titular:str, saldo:float):
        self.numero(numero)
        self.titular(titular)
        self.saldo(saldo)

    #Métodos
    
    def depositar(self, quantia, saldo):
        saldo = quantia + saldo
        
    def sacar(self, quantia, saldo):
        saldo = quantia - saldo 
        
    def mostrarDados(self):
        print("Numero da conta: ", self.__numero)
        print("Titular da conta: ", self.__titular)
        print("Saldo da conta: R$ %.2f" % self.__saldo)
#Fim classe 

#Programa principal

#Entrada de dados 
numero = int(input("Digite o número da conta: "))
titular = str(input("Digite o nome do titular: "))
adriano = str(input("Deseja fazer um depósito inicial (s/n)?"))

if adriano == 's':
    saldo = float(input("Digite o saldo inicial: "))
    conta = ContaBancaria(numero, titular, saldo)
else:
    conta = ContaBancaria(numero, titular, 0.0)
    
#Saída de dados

print("Dados da conta:")
conta.mostrarDados()

#Deposito

quantia = float(input("Digite a quan/tia a ser depositada: R$"))
conta.depositar(quantia)
print("Dados da conta atualizados:")

conta.mostrarDados()

quantia = float(input("Digite a quantia a ser sacada: R$"))
conta.sacar(quantia)
print("Dados da conta atualizados:")
conta.mostrarDados()

