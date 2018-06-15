# Criando uma lista com 5 posições
lista = [""]*5

# # Preenchendo uma lista manualmente
# lista[0] = 15
# lista[1] = 20
# lista[2] = 150
# lista[3] = 0
# lista[4] = 159
# # Mostrando os valores da lista no print
# print("A primeira posição:", lista[0])
# print("A segunda posição:", lista[1])
# pripnt("A terceira posição:", lista[2])
# print("A quarta posição:", lista[3])
# print("A quinta posição:", lista[4])
# # Pode alterar o valor da lista
# lista[3] = 29
# print("A quarta posição:", lista[3])


# Criando uma lista vazia
# listaVazia = []

# Pedir para o usuário informar o tamanho da lista
# t = int(input("Tamanho da lista: "))

# Criação de uma variável para representar as posições
p = 0
# Condição para parar antes do tamanho porque começa em zero
# len(lista) verifica o tamanho atual da lista
while p < len(lista):
    # Armazena algo digitado na posição p
    lista[p] = input("Número:")
    # Converte o valor da posição p para int
    lista[p] = int(lista[p])
    # Muda a posição da lista
    p = p + 1 # p+=1

# Percorrendo a lista com outro while
p = 0
while p < len(lista):
    print("Posição",p," - valor:",lista[p])
    p+=1

print("De traz para frente...")
# Verifica o tamanho da lista e diminui 1
p = len(lista) - 1
while p >= 0:
    print("Posição",p,"- valor:",lista[p])
    p = p - 1 # p-=1
