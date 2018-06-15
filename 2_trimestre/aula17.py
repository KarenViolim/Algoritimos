# Pede o tamanho da lista
t = int(input("Tamanho da lista:"))
# Cria a lista com tamanho "t"
lista = [""]*t

# Preenchendo o vetor com valores do usuário
p = 0
while p < len(lista):
    lista[p] = int(input("Número: "))
    p+=1
# Fim do preenchimento

# "Desenha" o vetor na tela
print(lista)

# Usando um laço de repetição for
# for nomeDaVariavel in nomeDaLista:
# A variável escolhida vai assumir os valores da lista.
# A cada rodada ele assume o valor conforme a ordem que o vetor foi criado
for valor in lista:
    dobro = valor * 2
    print("Valor armazenado: {} e o seu dobro: {}".format(valor, dobro) )

# Mostrando que a lista não é alterada
print(lista)
