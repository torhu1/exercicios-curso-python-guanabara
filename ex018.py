from math import sin, cos, tan, pi


angulo = (float(input('Digite um ângulo: ')))
radiando = angulo * pi / 180

print(f'Levando o ângulo {angulo} em consideração, '
      f'seu seno é {round(sin(radiando), 2):.2f}, '
      f'seu coseno é {round(cos(radiando), 2):.2f} e '
      f'sua tangente é {round(tan(radiando), 2):.2f}!')
