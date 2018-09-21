# Importa uma biblioteca para poder usar seu conteúdo
import sqlite3

########### F U N Ç Õ E S #########

def criar_tabela_usuario(conexao):

    # Cria o cursor para operar o banco
    cursor = conexao.cursor()

    # Monta o SQL a ser executado
    sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            nome text,
            login text,
            senha text
        );
    """

    # Executa um SQL
    cursor.execute(sql)

# Inserir novo usuário
def inserir_usuario(conexao, nome, login, senha):

    # Cria o cursos para operar o banco
    cursor = conexao.cursor()

    # Monta o select com o format e os dados
    sql = """
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
    """.format(nome, login, senha)

    # Executa o sql
    cursor.execute(sql)

    # Salvar as modificações.
    # O commit sempre deve ser feito depois do INSERT, UPDATE ou DELETE
    conexao.commit()
def buscar_usuario(conexao, nome):
    cursor = conexao.cursor()

    sql = """
    SELECT rowid, * FROM usuario
    WHERE nome LIKE '%{}%';
    """.format(nome)

    cursor.execute(sql)

    usuarios = cursor.fetchall()

    for usr in usuarios:
        print( "{}: {} ({})".format(usr[0], usr[1], usr[2]) )

# Listar os registros de usuário
def listar_usuarios(conexao):

    # Cria o cursor para operar o banco
    cursor = conexao.cursor()

    # Monta o SQL
    sql = "SELECT rowid, * FROM usuario ORDER BY nome;"

    # Executa o SQL
    cursor.execute(sql)

    # Armazena os dados (registros) do select
    # Toda vez que executa o select, precisa usar o fetch para buscar os registros
    usuarios = cursor.fetchall() # buscar todos

#cria um vetor para armazenar cada linha do select em uma posição
#cria um vetor para armazenar cada coluna de cada registro encontrado
#               0
#         0     1      2      0      1      2
# V = [ ['1','Rafa','123'], ['2','Fulano','312'], []... ]
#
# V[0][1] #pega o vetor na posição zero, que armazena outro vetor na posição 2 escrito Rafa.

    # Percorrer a lista com os registros
    # Estou chamando de "usr" cada item dessa lista
    for usr in usuarios:
        print( "{}: {} ({})".format(usr[0], usr[1], usr[2]) )
        # 1: Rafael Henrique (rafael.zottesso)

def alterar_usuario(conexao, id, nome, login, senha):
    cursor = conexao.cursor()

    sql = """UPDATE usuario
    SET nome = '{}', login = '{}', senha = '{}'
    WHERE rowid = {}""". format(nome, login, senha, id)

    cursor.execute(sql)

    conexao.commit()

def excluir_usuario(conexao, id):
    #Criar cursor para operar o banco
    cursor = conexao.cursor()

    #Monta o sql
    sql = "DELETE FROM usuario WHERE rowid = {}".format(id)

    #Executa o sql
    cursor.execute(sql)

    #Faz o commit para salvar as alterações
    conexao.commit()

############ P R I N C I P A L #############

# 1º - Iniciar a conexão (ligação) com nosso banco
o = 1
while o != 0:
    print("Conectando no banco...\n\n")
    conexao = sqlite3.connect("aula28.sqlite")

    # Início do programa
    #Pedir para o usuário as opções, dados, etc...
    print("""
    Em relação aos usuários do sistema, você deseja...

    1 - Inserir
    2 - Buscar
    3 - Listar
    4 - Alterar
    5 - Excluir
    9 - Voltar
    """)

    opcao = int(input("Opção desejada: "))

    if opcao == 1:
        print("\n--- Digite os dados do usário ---\n")
        n = input("Nome: ")
        l = input("Login: ")
        s = input("Senha: ")

        #Validar campos obrigatórios
        # if n, l, s == {}:
        #     print("Digite os campos obrigatórios.")
        inserir_usuario(conexao, n, l, s)
    elif opcao == 2:
        print("\n--- Busca de registros ---\n")
        #Exemplo de sql para consultar tudo
        #"SELECT ..... WHERE nome LIKE '%{}%'.".format(nome)
        n = input("\nDigite um nome para buscar: ")
        buscar_usuario(conexao, n)
    elif opcao == 3:
        print("\n--- Listando registros ---\n")
        listar_usuarios(conexao)
    elif opcao == 4:
        print("\n--- Alteração de registros ---\n")
        i = input("Digite o ID que deseja alterar: ")
        newn = input("Novo nome: ")
        newl = input("Novo login: ")
        news = input("Nova senha: ")
        alterar_usuario(conexao, i, newn, newl, news)
    elif opcao == 5:
        print("\n--- Exclusão de registros ---\n")
        e = input("\nDigite o ID para realizar a exclusão: ")
        excluir_usuario(conexao, e)
        print("\nOk. Usuário excluido com sucesso!")
    elif opcao == 9:
        print("\n--- Voltando ---\n")
    else:
        print("\n--- Opção inválida! ---\n")
        # Fim do seu programa

        # Fechando a conexão (ligação) com o banco
        print("\n\nFechando conexão com o banco...")
        conexao.close()
