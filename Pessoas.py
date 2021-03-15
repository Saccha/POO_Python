'''
Dado o dicionário vazio "pessoas", faça o que se pede nos itens a) e b),
conforme a descrição nos comentários do código abaixo:
'''
i = 0
while i < 5:    # Lê o nome de 5 pessoas e as linguagens que as pessoas programam
	nome = input('\nNome da pessoa: ')
	linguagem = input('Linguagem que programa: ')
	# item a) insira o nome e a linguagem que a pessoa programa no dicionário "pessoas" na linha abaixo:
        # A chave será o nome, e o valor é a linguagem
	pessoas[nome] = linguagem
	i = i + 1


print("\nLista de pessoas:")
"""
# item b) Construa abaixo o código para listar os dados cadastrados no dicionário conforme o seguinte exemplo:
Exemplo:
	Maria programa em Python
	Jose programa em Ruby
	Mauro programa em PHP
	Bruna programa em Javascript
	Rai programa em Pascal
"""
for chave in pessoas:
        print(chave, 'program em', pessoas[chave])
