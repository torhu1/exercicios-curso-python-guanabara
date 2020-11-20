import math


altura_parede = float(input('Qual a altura da parede em Metros? '))
largura_parede = float(input('Qual a largura da parede em Metros? '))
area_parede = altura_parede * largura_parede
litros = math.ceil(area_parede/2)

print(f'Para pintar uma parede de {area_parede} m² '
      f'será necessario {litros} litros de tinta!')
