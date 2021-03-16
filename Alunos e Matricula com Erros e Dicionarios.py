# CONSTRUA O SEU PROGRAMA A PARTIR DAQUI:
def buscar(dicionario, matricula):
    try:
        if (type(matricula) is not int):
            raise TypeError
        elif (len(str(matricula)) != 6):
            raise ValueError
        return dicionario[matricula]
    except TypeError:
        print('O parâmetro matrícula deve ser inteiro!')
    except ValueError:
        print('O número de matrícula deve ter 6 digitos!')
    except KeyError:
        print('Não existe aluno com este número de matrícula!')
        
# Programa principal sugerido para chamar a sua função e testar o seu código
# Você pode alterá-lo se desejar, mas isso não é obrigatório.
# Lembrando que a lógica da sua atividade deve estar inteiramente na função pedida!
def programa_principal():
    dicionario = {123456: 'Joao', 202018: 'Maria', 202088:'Jose', 202015: 'Bia', 202010: 'Caio'}
    matricula = input("Informe a matrícula do aluno: ")
    try:
            matricula = int(matricula)
    except:
            pass
    nome_aluno = buscar(dicionario, matricula)
    if nome_aluno is not None:
            print(nome_aluno)
programa_principal()
