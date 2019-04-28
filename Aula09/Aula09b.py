frase = '    Curso em Video Python    '
print(frase.count('o'))  #conta quantos vezes esse caractere expecificado aparece na String
print(frase.count('o',5)) #conta caractere expecificado a partir da posição 5
print(frase.count('o',5,15)) #conta caractere a partir da posição 5 e antes da posição 15
print(frase.count('video')) #conta string (difere letras Minúsculas e Maiúsculas.
print(frase.count('Video')) #conta string
print(frase.upper()) #altera frase para maiúscula
print(frase.lower()) #altera frase para minúscula
print(frase.upper().count('O')) #altera frase para maiúscula e conta caractere expecificado
print(len(frase)) # mostra o tamanho da String
print(frase.strip()) # teria espaço no início e no final
print(len(frase.strip())) # mostra o tamanho da string frase sem expaço no inicio e no final
print(frase.replace('Python','Android')) # rescreve Python como Android
frase = frase.replace('Python','Android') # modifica frase rescrevendo Python como Android
print(frase) # mostra frase já editada
print('Curso' in frase) # Validada como True ou False a existencia de Curso na String frase
print(frase.find('Curso')) # procura a existencia de Curso e retorna a primeira posição em que ela aparece
print(frase.find('curso')) # procura a existencia de curso (Letra Maiúscula ou minúscula interferem)
print(frase.strip().find('Curso'))
print(frase.lower().find('curso')) #torna string minuscula e faz busca
print(frase.upper().find('curso')) #torna string maiuscula e faz busca
print(frase.split()) #divide
dividido = frase.split() #divide e envia para dividido
print(dividido[2]) #mostra segunda posicao pos divisão
print(dividido[2][2]) #mostra segunda posicao da segunda posicao pos divisão