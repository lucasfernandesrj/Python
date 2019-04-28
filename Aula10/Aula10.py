tempo=int(input('Informe quantos anos o seu carro tem: '))
if tempo <=3:
    print('Carro Novo!')
else:
    print('Carro Velho!')
print('---FIM---')

print('Carro novo' if tempo <=5 else 'Carro velho')