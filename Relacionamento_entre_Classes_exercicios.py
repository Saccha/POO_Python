"""
1.A associação entre classes ocorre quando uma classe possui atributos que são objetos de outra classe. 
De acordo com esse conceito, observe o diagrama de classes abaixo, que representa uma associação onde 
uma Pessoa possui um Carro.
Implemente as classes Pessoa e Carro.

Classe Pessoa:
  Atributos:
    nome: nome da pessoa (valor inicial definido no construtor)
    idade: idade da pessoa (valor inicial definido no construtor)
    carro: objeto da classe Carro (valor inicial None)
  Métodos:
    comprar_carro: recebe um objeto Carro e associa esse objeto ao atributo carro.
Classe Carro:
  Atributos:
    marca: marca do carro (valor inicial definido no construtor)
    modelo: modelo do carro (valor inicial definido no construtor)
    placa: placa do carro (valor inicial definido no construtor)
    ano: ano de fabricação do carro (valor inicial definido no construtor)
  Métodos: 
    Não possui
"""
class Pessoa:
  def __init__(self,nome,idade):
    self.nome = nome
    self.idade = idade
    self.carro = None

  def comprar_carro(self,carro):
    self.carro = carro

class Carro:
  def __init__(self,marca,modelo,placa,ano):
    self.marca = marca
    self.modelo = modelo
    self.placa = placa
    self.ano = ano

meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)                            # imprime João
print('Modelo do meu carro: ', eu.carro.modelo)         # imprime Gol
print('Placa do meu carro: ', eu.carro.placa)           # imprime AAA-1111

#-------------------------------------------------------------------------------------------------------------------------
"""
2.Observe o diagrama de classes abaixo, que representa uma associação onde um Pedido possui uma lista de Produtos.
Implemente as classes Produto e Pedido.
Classe Pedido:
  Atributos:
    produtos: Lista de objetos do classe Produto (iniciar com uma lista vazia)
  Métodos:
    adicionar_produto: recebe um objeto Produto e o adiciona na lista de produtos.
    calcular_valor: deve retornar o valor total do pedido (soma dos valores de todos os produtos do pedido)
Classe Produto:
  Atributos:
    nome: nome do produto
    preco: preço do produto
    quantidade: quantidade de itens do produto
  Métodos: 
    Não possui
"""

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        soma = 0
        for prod in self.produtos:
            preco = prod.preco * prod.quantidade
            soma += preco
        return soma


cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())	    #Irá imprimir 20.9

#-------------------------------------------------------------------------------------------------------------------------
"""
3.Observe o diagrama de classes abaixo e implemente as classes Carro e Pneu. O diagrama representa uma associação onde 
um Carro possui quatro Pneus.
    Classe Carro:
        Atributos:
            ligado: valor booleano que indica se o carro está ligado ou desligado (deve iniciar com o valor False)
            pneu1, pneu2, pneu3, pneu4: objetos do tipo Pneu que representa cada um dos pneus do carro (devem receber os valores 
                                        iniciais no construtor).
        Métodos:
            ligar: altera o valor do atributo ligado para True
            desligar: altera o valor do atributo ligado para False
            verificar_pneu: se o carro estiver ligado, esse método deve exibir a pressão de cada um dos pneus. Se o carro estiver 
            desligado, o método deve exibir a mensagem ‘Carro Desligado'
    Classe Pneu:
        Atributos:
            pressao: valor inteiro que indica a pressão de ar do pneu (inicializado no construtor)
        Métodos:
            furar(): simula um pneu furado, alterando o valor do atributo pressao para zero.
"""

class Pneu:
    def __init__(self, pressao):
        self.pressao = pressao

    def furar(self):
        self.pressao = 0

class Carro:
    def __init__(self, pneu1, pneu2, pneu3, pneu4):
        self.ligado = False
        self.pneu1 = pneu1
        self.pneu2 = pneu2
        self.pneu3 = pneu3
        self.pneu4 = pneu4

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def verificar_pneu(self):
        if self.ligado is True:
            print("Pressão do pneu 1: ", self.pneu1.pressao)
            print("Pressão do pneu 2: ", self.pneu2.pressao)
            print("Pressão do pneu 3: ", self.pneu3.pressao)
            print("Pressão do pneu 4: ", self.pneu4.pressao)
        else:
            print("O carro está desligado")


p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro(p1, p2, p3, p4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()       # exibir a pressão de cada pneu.
meucarro.desligar()
meucarro.verificar_pneu()       # exibir mensagem que o carro está desligado

#-------------------------------------------------------------------------------------------------------------------------
"""
4.Implemente o diagrama de classes abaixo.
Classe Emprego
    Atributos:
        cargo
        area
        salario
        bonus: percentual de bonificação a ser acrescentado ao salário do funcionário, de acordo com a quantidade de dependentes. 
        Por exemplo, se o bônus for de 2%, e o funcionário tiver 3 dependentes, ele receberá 6% de acréscimo sobre o salário.
    Métodos:
        não possui
Classe Pessoa
    Atributos:
        nome
        fone
        email
        emprego: objeto do tipo Emprego
        dependentes: lista de objetos do tipo Pessoa
    Métodos:
        calcular_salario: retorna o valor do salário do funcionário, de acordo com o percentual de bonificação e quantidade de dependentes.
"""
class Emprego:
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus


class Pessoa:
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        quantidade = len(self.dependentes)
        porcentagem = quantidade * self.emprego.bonus
        salario = self.emprego.salario + (self.emprego.salario*porcentagem/100)
        return salario


emprego = Emprego("Programador", "TI", 2000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)
dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)
pessoa1.dependentes.append(dep1)
print("Salario: ", pessoa1.calcular_salario())
print("Salario: ", pessoa1.calcular_salario()) # imprime 1100.0

#-------------------------------------------------------------------------------------------------------------------------
"""
5.Implemente o diagrama de classes abaixo.
"""
class Paciente:
    def __init__(self,nome,cpf,idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico:
    def __init__(self,nome,crm,especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao
class Exame:
    def __init__(self,medico,paciente,descricao,resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado
        
    def imprimir_resultado(self):
        print("Nome do Médico: ",self.medico.nome)
        print("CRM do Médico: ",self.medico.crm)
        print("Especialidade: ",self.medico.especializacao)
        print("Nome do Paciente: ",self.paciente.nome)
        print("CPF do paciente: ",self.paciente.cpf)
        print("Idade do paciente: ",self.paciente.idade)
        print("Descrição do exame: ",self.descricao)
        print("Resultado: ",self.resultado)
        
paciente = Paciente("Marcelo Silva" , "033444555-22", 26)
medico = Medico('Ana Beatriz' , 333431, 'Clínico Geral')
exame01 = Exame(medico,paciente,'COVID-19','Negativo')
exame01.imprimir_resultado()
        
