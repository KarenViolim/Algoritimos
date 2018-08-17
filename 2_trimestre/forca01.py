from random import randint

def erro0():

    print("""
__________
|       |
|
|
|
|
|
|
|    """)

def erro1():

    print("""
__________
|       |
|       O
|
|
|
|
|
|    """)

def erro2():
    print("""
__________
|       |
|       O
|       |
|
|
|
|
|    """)

def erro3():
    print("""
__________
|       |
|       O
|      /|
|
|
|
|
|  """)

def erro4():
    print("""
__________
|       |
|       O
|      /|\\
|
|
|
|
|    """)

def erro5():
    print("""
__________
|        |
|        O
|       /|\\
|       /
|
|
|
|    """)

def erro6():
    print("""
__________
|        |
|        O
|       /|\\
|       / \\
|
|
|
|
""")

def gameover():
    print("""
╔═════════════════════════════╗
║ Game Over!! Tente Novamente ║
╚═════════════════════════════╝
    """)

def venceu():
    print("""
╔═════════════════════════╗
║ Parabéns!! Você ganhou  ║
╚═════════════════════════╝
""")

def sorteio():
    aleatorio = randint(0,len(palavras)-1) #sorteador
    return(aleatorio)

palavras = ["vassoura", "ifpr", "onca", "camiseta", "inverno"]
dica = ['acessório de limpeza', 'instituição de ensino', 'animal feroz', 'vestimos todo dia', 'estação do ano']
novamente = 's'
while novamente == 's':
    num = sorteio()
    palavra = palavras[num]

    letrasdigitadas = []
    letrascorretas = ['_']*len(palavra)
    letraserradas = []

    erro = 0
    certas = 0
    tentativas = 6

    while erro < 7:
        if erro == 0:
            erro0()

        if erro == 1:
            erro1()

        if erro == 2:
            erro2()

        if erro == 3:
            erro3()

        if erro == 4:
            erro4()

        if erro == 5:
            erro5()

        if erro == 6:
            erro6()
            gameover()
        print('     ',' '.join(letrascorretas))
        print('Dica', ''.join(dica[num]))
        print('As letras erradas são', ', '.join(letraserradas))
        print('Tentativas restante {}'.format(tentativas))
        letra = input('Digite uma letra: ')
        repetiu = 'n'
        if letra not in letrasdigitadas:
            letrasdigitadas.append(letra)
        else:
            print('Você já digitou está palavra')
            repetiu = 's'

        if repetiu == 'n':
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letrascorretas[i] = letra
                    certas += 1
            if certas == len(palavra):
                #print('     ',' '.join(letrascorretas))
                erro = 7
            if letra not in palavra:
                letraserradas.append(letra)
                erro += 1
                tentativas -= 1


        if erro == 6:
            erro6()
            gameover()
            print("A palavra era: {}".format(palavra))
            novamente = input('Deseja jogar novamente? Digite "s": ')
        if erro == 7:
             venceu()
             print("A palavra era: {}".format(palavra))
             novamente = input('Deseja jogar novamente? Digite "s": ')
