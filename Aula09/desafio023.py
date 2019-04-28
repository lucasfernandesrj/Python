#desafio023
num=str(input('Digite um número(0 a 9999): '))
dezena=0
centena=0
milhar=0

print("==MODO STR==")
unidade=num[len(num)-1]
if len(num)>1:dezena=num[len(num)-2]
if len(num)>2:centena=num[len(num)-3]
if len(num)>3:milhar=num[len(num)-4]

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

print("==MODO INT==")
num2=int(num)
print('Unidade: {}'.format(num2 % 10))
print('Dezena:{}'.format((num2 // 10) % 10))
print('Centena: {}'.format((num2 // 100) % 10))
print('Milhar: {}'.format(num2 // 1000))