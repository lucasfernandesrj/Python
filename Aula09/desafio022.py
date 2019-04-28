#desafio022
nome=str(input('Informe o nome completo: ')) #recebe a informação em forma de string
dividido=nome.title().split() # modifica como titulo e separa
print('Nome em Maiúsculo: {}'.format(' '.join(dividido).upper())) #junta com espaços simples e modifica para maiusulo
print('Nome em Minúsculo: {}'.format(' '.join(dividido).lower())) #junta com espaços simples e modifica para minusculo
print('Letras ao todo: {}'.format(len(''.join(dividido)))) #junta SEM espaços e conta
print('Letras do primeiro nome: {}'.format(len(dividido[0]))) #conta apenas a string na primeira posição
