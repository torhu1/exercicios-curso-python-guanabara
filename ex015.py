dias_alugado = int(input('Quantos dias alugado? '))
km_percorrido = float(input('Distancia percorrida em Km: '))
custo_total_aluguel = (dias_alugado * 60) + (km_percorrido * 0.15)

print(f'O total a pagar é de R${custo_total_aluguel:.2f}!')
