'''
ATIVIDADE:
Implemente a função dobra_valores_lista(lista), que recebe uma lista de números por parâmetro e devolve (retorna) uma lista com o dobro dos respectivos valores.

Exemplo de entrada da função: [0, 1, 2, 3, 4]
Saída esperada para a lista acima: [0, 2, 4, 6, 8]
'''

def dobra_valores_lista(lista):
    resultado = []
    i = 0
    while i < len(lista):
        resultado.append(lista[i] ** 2)
        i += 1
    return resultado

# Programa principal (NÃO ALTERE O CÓDIGO ABAIXO):
impares = [1, 3, 5, 7, 9]
dobro_impares = dobra_valores_lista(impares)
pares = [2, 4, 6, 8]
dobro_pares = dobra_valores_lista(pares)
print('Dobro dos ímpares:', dobro_impares)
print('Dobro dos pares:', dobro_pares)
