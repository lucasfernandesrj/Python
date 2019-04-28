from math import floor,trunc
num=float(input("Informe um valor: "))
print("O valor {} foi arredondado para {}".format(num, floor(num)))
print("O valor {} foi arredondado para {}".format(num, trunc(num)))
print("O valor {} foi arredondado para {}".format(num, int(num)))