# Pede o tamanho da lista
t = int(input("Tamanho da lista:"))
# Cria a lista com tamanho "t"
lista = [""]*t

# Preenchendo o vetor com valores do usuário
p = 0
while p < len(lista):
    lista[p] = int(input("Número: "))
    p+=1

###############################################

#
# Fazendo a soma dos valores do vetor
#
soma = 0
p = 0
while p < len(lista):
    # Acrescenta o valor da lista na posição p à soma
    soma = soma + lista[p]
    p+=1

print("A soma da lista é",soma)
print("A média da lista é", soma/len(lista) )

#
# Fazendo a média ponderada
#
soma = 0
pesos = 0
p = 0
while p < len(lista):
    # faz a multiplicação do valor * a posição dele
    soma = soma + (lista[p] * p)
    # soma += lista[p] * p

    # Faz a soma dos pesos
    pesos = pesos + p
    # pesos += p

    p+=1

# Calcula a média
medpon = soma / pesos
print("Média ponderada:", medpon)

#
# Conta a quantidade de números pares e ímpares
#
par = 0
impar = 0
p = 0
while p < len(lista):


    p += 1

print("A quantidade de pares é", par)
print("A quantidade de ímpares é", impar)
