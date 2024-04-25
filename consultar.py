import sqlite3

def consultar_tabela():
    # Conectar ao banco de dados clientesDB.sqlite
    conexao = sqlite3.connect('data/clientesDB.sqlite')
    cursor = conexao.cursor()

    # Comando SQL para selecionar todos os registros da tabela Cadastro
    comando_selecao = 'SELECT * FROM Cadastro;'

    # Executar o comando de seleção
    cursor.execute(comando_selecao)

    # Fetch (recuperar) todos os resultados
    resultados = cursor.fetchall()

    # Verificar se a consulta retornou registros
    if resultados:
        print("Consultando toda a tabela 'Cadastro':")
        for registro in resultados:
            print(registro)
    else:
        print("A tabela 'Cadastro' está vazia.")

    # Fechar a conexão com o banco de dados
    conexao.close()

if __name__ == "__main__":
    consultar_tabela()
