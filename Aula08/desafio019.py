from random import choice
nome1=input("informe o primeiro nome: ")
nome2=input("informe o segundo nome: ")
nome3=input("informe o terceiro nome: ")
nome4=input("informe o quarto nome: ")
escolhido = [nome1,nome2,nome3,nome4]
print("O aluno escolhido foi {}".format(choice(escolhido)))
