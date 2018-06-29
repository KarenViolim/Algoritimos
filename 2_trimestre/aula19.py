#importa a randint da biblioteca random
from random import randint
#Criação do vetor para armazenar números
loteria = [""]*6
#Variável de controle do laço de repetição
i = 0
#Laço para preencher o vetor
while i < len(loteria):
    # Gera número
    num = randint(1,60)
    #Variável para saber se repetiu ou não
    repetiu = "n"
    # Variável de controle do laço do laço que verifica se o número já existe ou não
    k = 0
    # Laço para verificação do número
    while k < i:
        #Verifica que se o nḿ está na posição
        if num == loteria[k]:
            # Se for verdadeiro, o número já está na lista
            # Diminui o valor do "i" para fazer este processo novamente
            i -= 1
            #Muda o valor da variável repetiu
            repetiu = "S"
            # Parar laço de repetição
            break
        #Incremento da posição
        k += 1
        #Fim do While do K
    if repetiu == "n":
        # Armazena
        loteria[i] = num

        # Incremento da posição
        i+=1

        #Mostrar a lista gerada
print(loteria)


##### Porque eu gosto do Python? #####

numeros = []

while len(numeros) < 6:
    num = randint(1,60)
    if num not in numeros:
        numeros.append(num)

print(numeros)
