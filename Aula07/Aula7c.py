n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2   #soma
m = n1 * n2   #multiplicação
d = n1 / n2   #divisão
di = n1 // n2 #divisão inteira
e = n1 ** n2  #exponenciação
print('A soma é {}, \n o produto é {} e a divisão é {:.2f}'.format(s,m,d), end=' ')
print ('a divisão inteira é {} e a potência é {}.'.format(di,e))

# \n quebra a linha
# ,end='' não permite a quebra de linha
