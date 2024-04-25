import sqlite3

# Conectar ao banco de dados clientesDB.sqlite
conexao = sqlite3.connect('data/clientesDB.sqlite')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Comando SQL para deletar a tabela Cadastro
comando_deletar_tabela = 'DROP TABLE IF EXISTS Cadastro;'

# Executar o comando de deleção da tabela
cursor.execute(comando_deletar_tabela)

# Salvar as alterações
conexao.commit()

# Fechar a conexão com o banco de dados
conexao.close()

print("Tabela 'Cadastro' deletada com sucesso.")
