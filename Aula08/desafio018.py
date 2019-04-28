from math import radians,cos,tan,sin
import math
angulo=float(input("Informe um angulo: "))
seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))

print("O ângulo de {}º possui cosseno: {:.2f}.".format(int(angulo),cosseno),
      "\nO ângulo de {}º possui seno: {:.2f}.".format(int(angulo),seno),
      "\nO ângulo de {}º possui tangente: {:.2f}.".format(int(angulo),tangente))