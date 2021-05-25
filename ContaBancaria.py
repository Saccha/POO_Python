class ContaBancaria:

    def __init__(self, titular, agencia, conta, saldo,):
            self.titular = titular
            self.agencia = agencia
            self.conta = conta
            self.saldo = saldo

    def obter_saldo(self):
        return self.saldo
    
    def creditar_valor(self, valor):
        self.saldo = self.saldo + valor

    def debitar_valor(self, valor):
        self.saldo = self.saldo - valor
        
    def transferir_valor (self, conta_destino, valor):
        self.saldo -= valor
        conta_destino.saldo += valor

class ContaPoupanca(ContaBancaria):

    def __init__(self, titular, agencia, conta, saldo, dia_aniversario):
        super().__init__(titular, agencia, conta, saldo)
        self.dia_aniversario = dia_aniversario

    def render(self, dia, taxa):
        if (dia == self.dia_aniversario):
            self.saldo = self.saldo + self.saldo * (taxa/100)

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, agencia, conta, saldo, pacote_servico):
        super().__init__(titular, agencia, conta, saldo)
        self.pacote_servico = pacote_servico

    def descontar_taxa_mensal(self):
        if   (self.pacote_servico == 'Estudante'):
            self.saldo -= 10
        elif (self.pacote_servico == 'Comum'):
            self.saldo -= 20
        elif (self.pacote_servico == 'Executivo'):
            self.saldo -= 50
        else: 
            self.saldo -= 15

def programa_principal():
	poupanca = ContaPoupanca('Jose Silva', 1234, 3456, 100.0, 6)
	poupanca.render(4, 0.5) # não rende nada, pois o dia é diferente do dia de aniversário
	print('Saldo da poupança:', poupanca.obter_saldo()) # imprime 100.0
	poupanca.render(6, 0.5) # não rende nada
	print('Saldo da poupança:', poupanca.obter_saldo()) # imprime 100.5
	poupanca.debitar_valor(1) # debita 1 da poupanca
	print('Saldo da poupança:', poupanca.obter_saldo()) # imprime 99.5
	
	conta_corrente = ContaCorrente('Maria Santos', 9876, 121314, 250.0, 'Estudante')
	conta_corrente.descontar_taxa_mensal() # desconta 10 do saldo (se a conta é de 'Estudante')
	print('Saldo da conta corrente:', conta_corrente.obter_saldo()) # imprime 240.0
	conta_corrente.creditar_valor(50) # adiciona 50 na conta corrente
	print('Saldo da conta corrente:', conta_corrente.obter_saldo()) # imprime 290.0
	
	conta_corrente.transferir_valor(poupanca, 60) # transfere 60 da conta corrente para a conta poupança
	print('Saldo da poupança:', poupanca.obter_saldo()) # imprime 159.5
	print('Saldo da conta corrente:', conta_corrente.obter_saldo()) # imprime 230.0

try:
	programa_principal()
except:
	print('Erro no programa principal.')
