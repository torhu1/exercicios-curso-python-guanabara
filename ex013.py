salario = float(input('Insira o salário atual: '))
porcentagem_aumento = float(
    input('Insira a porcentagem de aumento de salário: ')
)
salario_final = salario + salario * porcentagem_aumento / 100

print(
    f'{salario} com aumento de {porcentagem_aumento}% é igual {salario_final}'
)