#desafio027
nome=input('Informe o nome completo: ').title().strip()
ult=nome.rfind(' ')
pri=nome.find(' ')
completo=nome
print(completo)
print('Primeiro: {}.'.format(completo[:pri]))
print('Último: {}.'.format(completo[ult+1:]))


separado=nome.split()
print('{}'.format(separado[0]))
print('{}'.format(separado[len(separado)-1]))