import sqlite3

########### F U N Ç Õ E S #########

def criar_tabela_usuario(conexao):

    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            nome text,
            login text,
            senha text
        );
    """

    cursor.execute(sql)

def inserir_usuario(conexao, nome, login, senha):

    cursor = conexao.cursor()

    sql = """
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
    """.format(nome, login, senha)

    cursor.execute(sql)

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

def listar_usuarios(conexao):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM usuario ORDER BY nome;"

    cursor.execute(sql)

    usuarios = cursor.fetchall()

    for usr in usuarios:
        print( "{}: {} ({})".format(usr[0], usr[1], usr[2]) )

def alterar_usuario(conexao, id, nome, login, senha):
    cursor = conexao.cursor()

    sql = """UPDATE usuario
    SET nome = '{}', login = '{}', senha = '{}'
    WHERE rowid = {}""". format(nome, login, senha, id)

    cursor.execute(sql)

    conexao.commit()

def excluir_usuario(conexao, id):
    cursor = conexao.cursor()

    sql = "DELETE FROM usuario WHERE rowid = {}".format(id)

    cursor.execute(sql)

    conexao.commit()

############ P R I N C I P A L #############

# 1º - Iniciar a conexão (ligação) com nosso banco
o = 1
while o != 0:
    print("Conectando no banco...\n\n")
    conexao = sqlite3.connect("aula28.sqlite")

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

        inserir_usuario(conexao, n, l, s)

    elif opcao == 2:
        print("\n--- Busca de registros ---\n")
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
        print("\nUsuário alterado com sucesso!\n")

    elif opcao == 5:
        print("\n--- Exclusão de registros ---\n")
        e = input("\nDigite o ID para realizar a exclusão: ")
        excluir_usuario(conexao, e)
        print("\nOk. Usuário excluido com sucesso!\n")

    elif opcao == 9:
        print("\n--- Voltando ---\n")
        
    else:
        print("\n--- Opção inválida! ---\n")

        print("\n\nFechando conexão com o banco...")
        conexao.close()
