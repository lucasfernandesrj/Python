from random import shuffle
n1=input("Informe um nome: ")
n2=input("Informe um nome: ")
n3=input("Informe um nome: ")
n4=input('Informe um nome: ')
lista=[n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)