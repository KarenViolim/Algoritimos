preco_bruto = 789.90

# Calculando o desconto com uma promoção de
# 10% + 10% + 10% - (desconto progressivo)
d10 = preco_bruto * (10/100)
preco_final = preco_bruto - d10

d10 = preco_final * (10/100)
preco_final = preco_final - d10

d10 = preco_final * (10/100)
preco_final = preco_final - d10

# Calculando desconto direto de 30%
d30 = preco_bruto * (30/100)
preco_final2 = preco_bruto - d30

print("Final: R$", preco_final)
print("Final com 30%: R$", preco_final2)


###############################################


'''
Operadores relacionais

Todos podem ser utilizados com números (int e float)

>   maior
<   menor
>=  maior ou igual
<=  menor ou igual
==  igual         ->      Pode ser usado com String
!=  diferente     ->      Pode ser usado com String

"if" e a outra é o "else"

Utilização:
if condição:
    código 1
    código 2
    etc

'''
# idade = input("Digite sua idade: ")
# idade = int(idade)
#
# # Verifica se a condição é verdadeira
# if idade >= 18:
#     # Se for, faz somente esse código
#     print("Você é maior!")
#     print('Entrada permitida...')
# else:
#     # Se for falsa, faz esses daqui somente
#     print("Menor detectado...")
#     print("Entrada negada!")
#
#
# # Usando Strings na comparação
# if "Rafael" == "rafael":
#     print("Letras maiúsculas não importam.")
# else:
#     print("Letras maiúsculas são diferentes de minúsculas")
#

"""
LISTA DE EXERCÍCIOS

https://wiki.python.org.br/ListaDeExercicios
"""

# Faça um Programa que peça dois números e imprima o maior deles.
num1 = input("Digite um número: ")
num1 = int(num1)

num2 = input("Digite outro número: ")
num2 = int(num2)

if num1 > num2:
    print("O primeiro número é maior.")
# Podemos adicionar novas condições com o elif
# Que funciona da mesma forma que o if 
elif num2 > num1:
    print("O segundo é maior.")
else:
    print("Os números são iguais.")


# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
sexo = input("Digite m para Masculino e f para feminino: ")
# Não precisa converter porque sempre o input devolve uma string
if sexo == "m":
    print("M - Masculino")
else:
    print("F - Feminino")

