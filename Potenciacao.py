"""
Escreva a função potenciacao_em_lista(lista) que recebe uma lista de números inteiros por parâmetro. A função deve retornar (devolver) 
uma lista de mesmo tamanho que a lista recebida por parâmetro, na qual os elementos pares devem ser elevados ao quadrado e os elementos 
ímpares elevados ao cubo, com exceção do primeiro e do último elemento (os de índice 0 e len(lista)-1), que deverão ser mantidos intactos.

OBS: preste bastante atenção aos casos especiais quando a lista for vazia ou tiver um único elemento (neste último caso, os índices de início e 
fim são iguais, então o valor deve ser mantido intacto).

Formato de entrada
Uma lista de números inteiros enviada por parâmetro para a função.

Formato de saída
Uma lista que deve ser devolvida pela função (isto é, use o comando return) e possui o mesmo tamanho da lista enviada por parâmetro.

OBS: a função não deve imprimir nenhum valor. Não use a instrução print().
"""

# Escreva a funcao potenciacao_em_lista(lista) abaixo:
def potenciacao_em_lista(lista):
    resultado = []
    posicao = 0
    for c in lista:
      if not (posicao == 0 or posicao == len(lista)-1):
          if c % 2 == 0:
            resultado.append(c**2)
          else:
            resultado.append(c**3)
      else:
        resultado.append(c)
      posicao += 1
    return resultado


# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista = eval(input())
resultado = potenciacao_em_lista(lista)
print(resultado)
