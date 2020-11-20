from math import hypot


cateto_oposto = float(input('Digite a medida do cateto oposto: '))
cateto_adjacente = float(input('Digite a medida do cateto adjacente: '))
hypotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'Levando as suas medidas em consideração, a hypotenusa é {hypotenusa}!')
