try:
    ## Seu código
    a = int( input("Digite um número: ") )
    b = int( input("Digite um número: ") )
    if a > 3:
        input('a maior que 3')
except:
    ## O que fazer se der erro
    print("Digite apenas números...")
    a = 0
    b = 0
# Continua seu programa normalmente
print("A é", a, "e B é", b)

##########################################

## Condições compostas com usando AND
a = 5
if a >= 0 and a <= 10:
    print("A está entre 0 e 10")
elif a > 10:
    print("A maior que 10")
else:
    print("A menor que 0")

##########################################

## Condições compostas com usando OR
sexo = input("Digite seu sexo: M ou F? ")

if sexo == 'M' or sexo == 'm':
    print("Masculino")
else:
    print("Feminino")

##########################################

## Operador que pega o resto da divisão

a = 10 % 2 # a é zero
b = 15 % 2 # a é um

# Serve para saber se um número é múltiplo/divisível de outro
if a % 2 == 0:
    print("A é par")
else:
    print("A é ímpar")
