#desafio031
distancia=int(input('Informe a distância da viagem em Km: '))
if distancia < 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem é R${:.2f}.'.format(preco))