import sqlite3

# Conectar ao banco de dados clientesDB.sqlite; será criado se não existir
conexao = sqlite3.connect('data/clientesDB.sqlite')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Comando SQL para criar a tabela Cadastro, se ainda não existir
comando_criacao_tabela = '''
CREATE TABLE IF NOT EXISTS Cadastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    endereco TEXT,
    telefone TEXT
);
'''

# Executar o comando de criação da tabela
cursor.execute(comando_criacao_tabela)

# Salvar as alterações
conexao.commit()

# Fechar a conexão com o banco de dados
conexao.close()

print("Banco de dados 'clientesDB' e tabela 'Cadastro' criados com sucesso.")
