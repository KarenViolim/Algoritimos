# 1)Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar
# uma posição do vetor (lista).
# a - Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
# lista = [""]*100
#
# p = 0
# while p < len(lista):
#     lista[p] = p+1
#     p += 1
#
# p = 0
# while p < len(lista):
#     print("A posição",p,"tem o valor",lista[p])
#     p+=1

# b - Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
# p = len(lista) - 1
# while p >= 0:
#     print('A posição {} tem o valor {}'.format(p,lista[p]))
#     p -= 1

# c - Mostre na tela o dobro de todos os números.
# p = 0
# while p < len(lista):
#     dobro = lista[p] * 2
#     print("A posição {} tem o valor {}".format(p,dobro))
#     p += 1

# d - Apresente na tela a soma de todos os números.
# soma = 0
# p = 0
# while p < len(lista):
#     soma += lista[p]
#     p+=1
# print("A soma de todos os números é igual a {}".format(soma))

# e - Apresente na tela a média geral dos valores contidos na lista.
# soma = 0
# p = 0
# while p < len(lista):
#     soma += lista[p]
#     div = soma/len(lista)
#     p += 1
# print("A Média Geral dos valores é igual a {}".format(div))

# f - Mostre na tela a quantidade de números pares.
# par = 0
# p = 0
# while p <len(lista):
#     if lista[p] %2==0:
#         par +=1
#     p +=1
# print("Existem {} números pares".format(par))

# 2 - Faça um programa para armazenar 6 números inteiros para uma loteria,
# permitindo que o usuário informe os números sorteados. Depois de preencher,
# informe uma mensagem e os números sorteados.
# lista = [""]*6
#
# p = 0
# while p < len(lista):
#     lista[p] = input("Digite os números sorteados: ")
#     p += 1
#
# p = 0
# while p < len(lista):
#     p+=1
# print("Os Numeros sorteados foram {}".format(lista))

# 3 - Um professor precisa armazenar em uma lista os nomes dos alunos presentes em
# um minicurso. Faça um programa para armazenar 5 nomes e permitir que o professor
# digite o nome da cada um. Em seguida, apresente na tela todos os nomes informados.
# lista = [""]*5
#
# p = 0
# while p < len(lista):
#     lista[p] = input("Digite os nomes dos alunos: ")
#     p += 1
# for nome in lista:(input("Tamanho da lista: "))
# lista = [""]*t
#
#     p+=1
# print("O Nome dos alunos são: {}".format(lista))

# 4 - Faça um programa que peça para o usuário informar o tamanho de um vetor.
# Em seguida, crie este vetor e preencha ele com números digitados pelo usuário.
# Por fim, apresente na tela os números digitados.
# t = int(input("Tamanho da lista: "))
# lista = [""]*t
#
# p = 0
# while p < len(lista):
#     lista[p] = input("Digite os números desejados: ")
#     p += 1
#
# for numero in lista:
#     p+=1
# print("Os Numeros digitados foram {}".format(lista))

# 5 - Para os exercícios abaixo, utilize o vetor criado no exercício anterior.
t = int(input("Tamanho da lista: "))
lista = [""]*t

# a - Apresente os números do vetor em ordem inversa.
# p = 0
# while p < len(lista):
#     lista[p] = input("Digite os valores: ")
#     p += 1
#
# print(lista)
#
# p = len(lista) - 1
# while p >= 0:
#     print('A ordem inversa é {}'.format(lista[p]))
#     p -= 1

# b - Apresente a soma de todos os elementos.
# p = 0
# while p < len(lista):
#     lista[p] = int(input("Digite os valores: "))
#     p += 1
#
# soma = 0
# p = 0
# while p < len(lista):
#     soma += lista
#     p+=1
# print("A soma de todos os números é igual a {}".format(soma))

# c - Calcule a média aritmética dos valores.
p = 0
while p < len(lista):
    lista[p] = int(input("Digite os valores: "))
    p += 1

soma = 0
p = 0
while p < len(lista):
    soma += lista[p]
    div = soma/len(lista)
    p += 1
print("A média aritimética é igual a {}".format(div))
