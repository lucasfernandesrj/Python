#desafio028
from random import randint
print('Descubra o valor inteiro entre 0 e 5 escolhido pelo computador')
pensador=randint(0,5)
num=int(input('Informe o valor: '))
if num == pensador:
    print('Você acertou! Parabéns!')
else:
    print('Você errou!')
    print('O valor escolhido foi {}!'.format(pensador))