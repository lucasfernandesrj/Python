from math import sqrt,floor
import math
num=int(input('Digite um número: '))
raiz = sqrt(num)
raiz2 = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,floor(raiz)))
print('A raiz2 de {} é igual a {:.2f}.'.format(num,raiz2))
