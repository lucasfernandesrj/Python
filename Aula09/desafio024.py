#desafio024
cidade=input("Infome o nome da cidade: ")
validador=cidade.strip().title().split()
print('A cidade começa com o nome Santo? Resultado: {}.'.format('Santo' in validador[0]))
print(cidade.strip().title())