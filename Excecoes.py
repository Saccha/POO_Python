"""
Identifique as partes problemáticas no código
a seguir e reescreva-o tratando as possı́veis exceções.
"""

try:
	x = int(input('Primeiro valor: '))
	y = int(input('Segundo valor: '))
	z = x / y
	print('O resultado da divisão é:', z)
except ValueError:
	print('Erro: os valores de x e y devem ser inteiros!')
except ZeroDivisionError:
	print('Erro: o valor de y não pode ser zero!')
except:
	print('Um erro inesperado ocorreu!')
