#from math import floor
import math
num1=float(5.4545)
num2=int(-23)
num3=int(12)
num4=float(-19.4)
num5=int(25)
ang=int(45)
print("O valor {} arredondado para cima como Int é {}".format(num1, math.ceil(num1))) #arredonda para cima retornando um int
print("O valor {} arredondado para baixo como Int é {}".format(num1, math.floor(num1))) #arredonda para baixo retornando um int
print("O valor {} exibido em Float e positivo é {}".format(num2, math.fabs(num2))) #mostra o valor em
print("O valor {} em fatorial é {}".format(num3,math.factorial(num3)))
print("O valor {} teve o sinal convertido para o mesmo do valor {} e exibido em Float como {}".format(num4,num3, math.copysign(num4,num3))) #retorna o valor ABSOLUTO de x com a magnetude(sinal positivo e negativo) de y
print("O valor {} e {} possuem o MMC {} ".format(num3,num5,math.gcd(num5,num3))) # encontra o MMC de dois valores
print("O valor {} é finito? {}" .format(num1,math.isfinite(num1))) #verifica se é finito
print("O valor {} é infinito? {}".format(num1,math.isinf(num1))) #verificar se é infinito
print("O valor {} é um Não-Número? {}".format(num1,math.isnan(num1))) #verifica se é um não-número
print("O valor {} dividido em parte fracionada e número é {}".format(num1, math.modf(num1)))
print("O valor de e^{} é {}".format(num3,math.exp(num3))) # retorna E elevado a um valor digitado
print("O valor de log de 13 na base 7 é {}.".format(math.log(13,7))) # log(NUM,BASE) = log de NUM na base BASE
print("O valor de log de 3 na base 2 é {}.".format(math.log2(3))) #calcula log(NUM,2)
print("O valor de log de 3 na base 10 é {}.".format(math.log10(20))) #calcula log(NUM,10)
print("A potência de  {}^{} é {}".format(num5,2,math.pow(num5,2))) # faz a potencialização de pow(num,potencia) e converte para Float
print("A raiz de {} é {}".format(num5,math.sqrt(num5)))
print("O ângulo de {} possui cosseno: {}, seno: {} e tangente: {}.".format(ang, math.cos(ang),math.sin(ang),math.tan(ang)))
print(math.pi) #constante de pi
print(math.e) #constante de e
print(math.nan) #
print(math.tau) #constante de 2pi
print(math.inf) #infinito positivo de ponto flutuante. (-math.inf para negativo)
print(math.tan(4))
print(math.atan(4))
#print(math.atanh(4))
#print(math.atan2(4,4))