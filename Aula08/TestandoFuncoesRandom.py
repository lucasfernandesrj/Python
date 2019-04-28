import random
print(random.random()) # gera Float 0.0 <= x < 1.0
print(random.randint(2,5)) # gera Float 2 <= x <=5
print(random.randrange(10)) # gera Int  0 <= x < 10
print(random.uniform(2.5,10.0)) # gera Float 2.5 <= x < 10.0
print(random.randrange(0,101,3)) # gera Int 0 <= x < 101 com intervalo de 3
print(random.choice(['sim','nao','talvez'])) # gera um elemento da sequencia
print(random.sample([45,32,42,54,1,4,43],5)) # gera uma sequencia e a quantidade 5 de retirada
print(random.choices(['do','re','mi','fa','so','la','si'],[1,0,0,5,0,0,5],k=10)) # elementos / amostragem por cada elemento / retiradas
