#desafio026
frase=input('Escreva a frase: ').strip()
print('Quantidade de letras A(minúscula e maiúscula): {}.'.format(frase.upper().count('A')))
print('Posição em que a letra A(minúscula e maiúscula) aparece pela PRIMEIRA vez: {}'.format(frase.upper().find('A')+1))
print('Posição em que a letra A(minúscula e maiúscula) aparece pela ÚLTIMA vez: {}'.format(frase.upper().rfind('A')+1))
