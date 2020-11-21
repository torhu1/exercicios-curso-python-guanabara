from random import shuffle


aluno1 = input('Entre com o nome do(a) aluno(a) 1: ')
aluno2 = input('Entre com o nome do(a) aluno(a) 2: ')
aluno3 = input('Entre com o nome do(a) aluno(a) 3: ')
aluno4 = input('Entre com o nome do(a) aluno(a) 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('Os alunos devem apresentar o trabalho na seguinte ordem')
print(lista)
