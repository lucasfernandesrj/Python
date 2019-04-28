#desafio032
ano=int(input('Infome um ano: '))

e=('É ano bissexto!')
n=('Não é ano bissexto!')
if(ano%4==0):
    resultado =e
    if(ano%100==0):
        resultado=n
else:
    resultado=n

if (ano % 400 == 0):
    resultado =e
print(resultado)