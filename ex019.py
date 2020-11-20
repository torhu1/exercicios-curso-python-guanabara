import random


aluno1 = input('Digite o nome do(a) aluno(a) 1: ')
aluno2 = input('Digite o nome do(a) aluno(a) 2: ')
aluno3 = input('Digite o nome do(a) aluno(a) 3: ')
aluno4 = input('Digite o nome do(a) aluno(a) 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)

print(f'Aluno(a) sorteado(a) foi {sorteio}!')
