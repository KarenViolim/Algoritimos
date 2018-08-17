"""
Modos de leitura de arquivos:
- "r" é de leitura
- "w" é de escrita
- "a" é de escrita mas começa um arquivo em branco e apaga o existente
"""
arquivo = open("arquivos/nomes.txt", "r")

conteudo = arquivo.readlines()

arquivo.close()

l = 0
while (l <len(conteudo)):
    print(conteudo[l])
    l += 1

# for linha in conteudo:
#     print(linha)
