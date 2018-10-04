# Importação da biblioteca
import sqlite3

# Função para criar a tabela
def criar_tabela_contato(conexao):

    # Cria o cursor para operar o BD
    cursor = conexao.cursor()

    # Monta o sql
    sql = """
        CREATE TABLE IF NOT EXISTS contato (
            nome text,
            fone text,
            email text,
            usuario integer
        );
    """

    # Executa o SQL
    cursor.execute(sql)
def inserir_contato(conexao, nome, fone, email, usuario):

    cursor = conexao.cursor()

    sql = """
        INSERT INTO contato VALUES(
            '{}',
            '{}',
            '{}',
            {}
        );
    """.format(nome, fone, email, usuario)

    sql = """
        INSERT INTO usuario VALUES(
             'Rafael Zottesso',
             'rafael',
             '123'
         );
"""

    cursor.execute(sql)

    conexao.commit()

def buscar_contato(conexao, nome):
    cursor = conexao.cursor()

    sql = """
    SELECT rowid, * FROM contato
    WHERE nome LIKE '%{}%';
    """.format(nome)

    cursor.execute(sql)

    contato = cursor.fetchall()

    for c in contato:
        print( "{}: {} ({})".format(c[0], c[1], c[2]) )

def listar_contato(conexao):

    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM contato ORDER BY nome;"

    cursor.execute(sql)

    contato = cursor.fetchall()

    for c in contato:
        print( "{}: {} ({})".format(c[0], c[1], c[2]) )

def alterar_contato(conexao, id, nome, fone, email):
    cursor = conexao.cursor()

    sql = """UPDATE contato
    SET nome = '{}', telefone = '{}', email = '{}'
    WHERE rowid = {}""". format(nome, fone, email, id)

    cursor.execute(sql)

    conexao.commit()

def excluir_contato(conexao, id):
    cursor = conexao.cursor()

    sql = "DELETE FROM contato WHERE rowid = {}".format(id)

    cursor.execute(sql)

    conexao.commit()


##############################################################
def menu_contato():
    o = 1
    while o != 0:
        print("Conectando ao banco... ")
        conexao = sqlite3.connect("usuario.sqlite")

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
            print("\n--- Digite os dados do contato ---\n")
            n = input("Nome: ")
            t = input("Telefone: ")
            e = input("Email: ")

            inserir_contato(conexao, n, t, e, usuario)

        elif opcao == 2:
            print("\n--- Busca de registros ---\n")
            n = input("\nDigite um nome para buscar: ")
            buscar_contato(conexao, n)

        elif opcao == 3:
            print("\n--- Listando registros ---\n")
            listar_contato(conexao)

        elif opcao == 4:
            print("\n--- Alteração de registros ---\n")
            i = input("Digite o ID que deseja alterar: ")
            newn = input("Novo nome: ")
            newt = input("Novo telefone: ")
            newe = input("Novo email: ")
            alterar_contato(conexao, i, newn, newt, newe)
            print("\nContato alterado com sucesso!\n")

        elif opcao == 5:
            print("\n--- Exclusão de registros ---\n")
            e = input("\nDigite o ID para realizar a exclusão: ")
            excluir_contato(conexao, e)
            print("\nOk. Contato excluido com sucesso!\n")

        elif opcao == 9:
            print("\n--- Voltando ---\n")

        else:
            print("\n--- Opção inválida! ---\n")

            print("\nFechando conexão com o banco...")
            conexao.close()
menu_contato()
