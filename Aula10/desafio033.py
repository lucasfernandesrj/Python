#desafio033
n1=int(input('Informe o primeiro valor: '))
n2=int(input('Informe o segundo valor: '))
n3=int(input('Informe o terceiro valor: '))

meio=n1
if n2>meio:
    maior=n2
else:
    maior=meio
    meio=n2
if n3 > maior:
    menor=meio
    meio=maior
    maior=n3
else:
    if n3 > meio:
        menor=meio
        meio=n3
    else:
        menor=n3

print('Menor valor: {} e Maior valor: {}'.format(menor,maior))