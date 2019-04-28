#desafio035
a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

ok = -1
if (b - c) < a < (b + c):
    if (a - c) < b < (a + c):
        if (a - b) < c < (a + b):
            ok = 1

if ok == 1:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')
