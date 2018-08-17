menu = 0

while menu != 3:

    print("""
    1 - Adicionar palavra
    2 - Listar palavras
    3 - Sair
    """)

    menu = int(input("Escolha uma opção: "))
    if menu == 1:
        arq = open ("arquivos/palavras.txt", "a")
        palavra = input("Digite a palavra para adicionar: ")
        arq.write(palavra)
        arq.write("\n")
        arq.close()
    if menu == 2:
        arq = open ("arquivos/palavras.txt", "r")
        forca = arq.readlines()
        arq.close
        for p in forca:
            print(p)
    if menu == 3:
        print("Fechando o programa...")
