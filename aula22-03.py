# 1 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# n1 = input('Digite o numero:')
# n1 = int (n1)
#
# if n1 < 0:
#     print ('O numero é negativo')
# else:
#     print ('O numero é positivo')
#
# 2 Faça um Programa que peça dois números e imprima o maior deles.
# a = input ('Digite um número:')
# a = int (a)
# b = input ('Digite outro número:')
# b = int (b)
#
# if a > b:
#     print("O primeiro número é maior.")
# elif b > a:
#     print("O segundo número é maior.")
# else:
#     print("Os números são iguais.")
#
# 3 Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
# a = int ( input ("Digite o valor de A: "))
# b = int ( input ("Digite o valor de B: "))
# c = int ( input ("Digite o valor de C: "))
#
# if a+b < c:
#     print("A + B é menor que C.")
# else:
#     print("A + B é maior que C.")
#
# 4 Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever “Feminino” ou
# “Masculino”, conforme a letra digitada.
# sexo = input('Digite seu sexo (M)Masculino e (F)Feminino:')
#
# if sexo == "M":
#     print ('Masculino')
# elif sexo == "F":
#     print ('Feminino')
# else:
#     print ('Sexo invalido!')

# 5 Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).
# num = int(input("Insira um número inteiro: "))
# if num % 2 == 0:
#     print ("É par")
# else:
#     print ("É ímpar")
#
# 6 Faça um algoritmo que leia um número e some 5 caso seja par ou some 8 caso seja ímpar. Por fim, imprima o resultado desta soma.
# num = int ( input("Digite um número: "))
# if num %2 == 0:
#     print(num + 5)
# else:
#     print (num + 8)
#
# 7 Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou
# igual a 60, escreva “Aprovado”, se não, “Reprovado”.
n1 = int ( input ("Informe a nota 1: "))
n2 = int ( input ("Informe a nota 2: "))
nota = (n1 + n2) / 2
if nota >= 60:
    print ("Aprovado")
else:
    print ("Reprovado")
