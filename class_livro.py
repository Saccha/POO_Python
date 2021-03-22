"""
1. Implemente a classe Livro, conforme o diagrama a seguir. No programa
principal, crie dois objetos da classe Livro.
obs: Não tem método
"""
class Livro():
 def __init__(self, nome_titulo, nome_autor, num_paginas):
  self.titulo = nome_titulo
  self.autor = nome_autor
  self.paginas = num_paginas
 # Programa principal
obra = Livro('O Cujo', 'Stephen King', 371)
print('Nome do Titulo:', obra.titulo)
print('Nome do autor:', obra.autor)
print('Número de páginas:', obra.paginas)
