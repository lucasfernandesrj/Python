#desafio034
salario=int(input('Informe o salário: '))
if salario>1250:
    salario = salario * 1.10
else:
    salario = salario * 1.15

print('O salário com aumento é R${:.2f}.'.format(salario))