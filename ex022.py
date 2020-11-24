nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
junto = ''.join(dividido)

print('-'*40, '\n')
print(f'Nome em caixa baixa: {nome.lower()}. \n')
print(f'Nome em caixa alta: {nome.upper()}. \n')
print(f'Nome pussui {len(junto)} letras, excluindo espaços. \n')
print(f'O primeiro nome possui {len(dividido[0])} letras.')
