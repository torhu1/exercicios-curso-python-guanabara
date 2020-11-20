preco = float(input('Digite o preço: '))
porcentagem_de_desconto = float(input('Digite a porcentagem de desconto: '))
preco_final = preco-preco*(porcentagem_de_desconto/100)
print('{} com {} de desconto é {}'.format(preco, porcentagem_de_desconto, preco_final))
