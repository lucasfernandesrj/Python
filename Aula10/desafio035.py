#desafio035
a=int(input('Informe o primeiro valor: '))
b=int(input('Informe o segundo valor: '))
c=int(input('Informe o terceiro valor: '))

if (b-c)<a:
    if a<(b+c):
        ok1=1
    else:
        ok1=-1
else:
    ok1=-1

if (a-c)<b:
    if b<(a+c):
        ok2=1
    else:
        ok2=-1
else:
    ok2=-1

if(a-b)<c:
    if c<(a+b):
        ok3=1
    else:
        ok3=-1
else:
    ok3=-1

if ok1==1:
    if ok2==1:
        if ok3==1:
            super=1
        else:
            super=-1
    else:
        super=-1
else:
    super=-1

if super==1:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')



if (b-c)<a<(b+c):
    ok1=1
else:
    ok1=-1