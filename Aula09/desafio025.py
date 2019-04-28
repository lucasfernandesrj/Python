#desafio025
nome=input('Digite o nome: ')
teste=nome.strip().title().find('Silva')
if teste!=-1:print('Sim, possui Silva no nome!')
else: print('Não possui!')
#.format('Silva' in nome)o