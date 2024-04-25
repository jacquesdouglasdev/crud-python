import sqlite3
from sqlite3 import Error

def inserir_clientes_teste():
    # Lista de clientes de teste para inserir
    clientes = [
    ("Ana Silva", "ana.silva@email.com", "Rua das Flores, 10", "11999999999"),
    ("Bruno Souza", "bruno.souza@email.com", "Avenida Central, 500", "11999999998"),
    ("Carlos Oliveira", "carlos.oliveira@email.com", "Rua da Paz, 250", "11999999997"),
    ("Daniela Martins", "daniela.martins@email.com", "Rua do Sol, 100", "11999999996"),
    ("Eduardo Rocha", "eduardo.rocha@email.com", "Avenida dos Estados, 1200", "11999999995"),
    ("Fernanda Lima", "fernanda.lima@email.com", "Rua das Laranjeiras, 300", "11999999994"),
    ("Gabriel Alves", "gabriel.alves@email.com", "Praça da Sé, 15", "11999999993"),
    ("Helena Gomes", "helena.gomes@email.com", "Alameda Barão de Limeira, 200", "11999999992"),
    ("Igor Santos", "igor.santos@email.com", "Rua Augusta, 450", "11999999991"),
    ("Júlia Pereira", "julia.pereira@email.com", "Rua Haddock Lobo, 330", "11999999990"),
    ("Kauê Ribeiro", "kaue.ribeiro@email.com", "Rua da Consolação, 1230", "11999999989"),
    ("Larissa Costa", "larissa.costa@email.com", "Avenida Paulista, 1578", "11999999988"),
    ("Márcio Neves", "marcio.neves@email.com", "Rua Oscar Freire, 1100", "11999999987"),
    ("Nadia Silva", "nadia.silva@email.com", "Rua dos Pinheiros, 980", "11999999986"),
    ("Otávio Mendes", "otavio.mendes@email.com", "Avenida Rebouças, 2200", "11999999985"),
    ("Patrícia Souza", "patricia.souza@email.com", "Rua Veneza, 35", "11999999984"),
    ("Quintino Aires", "quintino.aires@email.com", "Rua Bela Cintra, 120", "11999999983"),
    ("Roberta Figueiredo", "roberta.figueiredo@email.com", "Rua dos Ingleses, 325", "11999999982"),
    ("Sérgio Lopes", "sergio.lopes@email.com", "Praça Roosevelt, 134", "11999999981"),
    ("Tânia Mara", "tania.mara@email.com", "Avenida Ipiranga, 200", "11999999980"),
    ("Umberto Ferreira", "umberto.ferreira@email.com", "Rua da Consolação, 2934", "11999999979"),
    ("Vânia Almeida", "vania.almeida@email.com", "Rua Vergueiro, 1000", "11999999978"),
    ("William Barros", "william.barros@email.com", "Rua Frei Caneca, 569", "11999999977"),
    ("Xuxa Meneghel", "xuxa.meneghel@email.com", "Avenida Brasil, 177", "11999999976"),
    ("Yasmin Faria", "yasmin.faria@email.com", "Rua Teodoro Sampaio, 200", "11999999975"),
    ("Zilda Martins", "zilda.martins@email.com", "Rua Amaral Gurgel, 333", "11999999974"),
    ("Aline Castro", "aline.castro@email.com", "Rua Matias Aires, 78", "11999999973"),
    ("Bruno César", "bruno.cesar@email.com", "Avenida Pompeia, 1458", "11999999972"),
    ("Cecília Souza", "cecilia.souza@email.com", "Rua Clélia, 2207", "11999999971"),
    ("Diego Almeida", "diego.almeida@email.com", "Rua Faustolo, 1123", "11999999970")
]


    # Ajuste o caminho do banco de dados conforme necessário
    conexao = sqlite3.connect('data/clientesDB.sqlite')
    
    try:
        cursor = conexao.cursor()
        
        # SQL para inserir clientes
        query = '''
        INSERT INTO Cadastro (nome_completo, email, endereco, telefone) 
        VALUES (?, ?, ?, ?)
        '''
        
        for cliente in clientes:
            cursor.execute(query, cliente)
            
        conexao.commit()
        print(f"{len(clientes)} clientes inseridos com sucesso.")
        
    except Error as e:
        print(f"Erro ao inserir clientes: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    inserir_clientes_teste()
