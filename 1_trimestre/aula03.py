# Informa uma mensagem na tela
# e captura algo digitado como string
a = input("Digite o valor de A:")
# Converte o valor armazenado em a para float
a = float(a)

# Mesma coisa, porém converte pra int
b = input("Grau da raiz:")
b = int(b)

# Realiza uma operação matemática
x = a**(1/b)

# Apresenta o valor da variável
print(x)

# Mostra uma mensagem e o valor de x
print("O resultado é", x)

# Mostra uma variável
print("A raiz de grau", b, "de", a, "é", x)
