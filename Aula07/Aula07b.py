nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:=^20}!'.format(nome.title())) # centralizado
print('Prazer em te conhecer, {:)<20}!'.format(nome.title())) # alinhado a esquerda
print('Prazer em te conhecer, {:+>20}!'.format(nome.title())) # alinhado a direita