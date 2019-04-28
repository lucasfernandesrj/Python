#desafio029
from random import randint
num=randint(70,130)
if num>80:
    multa=float((num-80.00)*7)
    print('Você foi multado por dirigir com velocidade de {}km/h acima do permitido que é de 80Km/h!'.format(num))
    print('A multa vai custar R${:.2f}.'.format(multa))