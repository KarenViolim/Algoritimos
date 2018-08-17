"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita mas começa um arquivo em branco e apaga o existente
"""
print("Abrindo arquivo...")
# a função open retorna um endereço para o arquivo
arq = open("arquivos/nomes.txt", "a")

# print("Escrevendo no arquivo...")
#Pela variável anterior, escolha o arquivo para escrever alguma coisa
# arq.write("Santiago Molina\n")
nome = input("Informe seu nome completo: ")
#Armazena o nome digitado
arq.write(nome)
#Quebra a linha
arq.write("\n")

print("Fechando o arquivo...")
# Salva as modificações e fecha o arquivo
arq.close()
