# Escreva a funcao devolve_lista_numeros(x, y) abaixo:
def devolve_lista_numeros(x, y):
   resultado = []
   for i in range(x,y+1):
       resultado.append(i)
   return resultado

# PROGRAMA PRINCIPAL: nao altere o codigo a partir deste ponto
def programa_principal():
	a = int(input())
	b = int(input())
	resultado = devolve_lista_numeros(a, b)
	print(resultado)
programa_principal()
