"""
4. Faça um programa para criar dois objetos da classe Aluno e utilize os métodos estudar
e dormir. Ao final exiba quanto tempo os alunos estão sem dormir. Veja abaixo um
trecho de programa que utiliza a classe:
"""

class Aluno():
    # atributos
    def __init__(self, nome=None, tempo_sem_dormir=0):
        self.nome = nome
        self.tempo_sem_dormir = tempo_sem_dormir

    def estudar(self, horas):
        self.tempo_sem_dormir += horas

    def dormir(self, horas):
        self.tempo_sem_dormir -= horas


aluno1 = Aluno()
aluno1.nome = ('Renato')
aluno1.estudar(3)
aluno1.dormir(2)
aluno1.estudar(4)
aluno1.dormir(2)
print(f'O aluno {aluno1.nome} está {aluno1.tempo_sem_dormir} horas sem dormir')
