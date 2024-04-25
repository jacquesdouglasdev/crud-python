from sqlite3 import connect, Error
from tkinter import messagebox

class funcoes():
    def __init__(self) -> None:
        
        pass

    # Funções de validação de Entry
    def testa_valor_entrada(self, valor, regra='regra4'):
        # REGRAS DE VALIDAÇÃO
        #
        # regra1 = somente números
        # regra2 = ponto + números
        # regra3 = somente letras
        # regra4 = espaço + letras
        self.resultado = True
        if (regra == 'regra1'):
            self.lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        elif (regra == 'regra2'):
            self.lista = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        elif (regra == 'regra3'):
            self.lista = ["'", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'ä', 'ã', 'á', 'â', 'é', 'ê', 'í', 'ö', 'õ', 'ó', 'ô', 'ü', 'ú']
        elif (regra == 'regra4'):
            self.lista = ['.', ' ', "'", '-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'ä', 'ã', 'á', 'â', 'é', 'ê', 'í', 'ö', 'õ', 'ó', 'ô', 'ü', 'ú']      
        for i in valor:
            if i.lower() in self.lista:
                self.resultado = True
            else:
                self.resultado = False
                break
        return self.resultado

    def inserir_4_campos(self, campo1, campo2, campo3, campo4, query):
        self.conexao = connect('data/clientesDB.sqlite')
        try:
            with self.conexao:
                self.cursor = self.conexao.cursor()
                self.cursor.execute(query, (campo1, campo2, campo3, campo4))
                self.conexao.commit()
        except Error as ex:
            messagebox.showerror('Erro', str(ex))

    def atualiza_4_campos(self, campo1, campo2, campo3, campo4, id, query):
        self.conexao = connect('data/clientesDB.sqlite')
        try:
            with self.conexao:
                self.cursor = self.conexao.cursor()
                self.cursor.execute(
                    query, (campo1, campo2, campo3, campo4, id))
                self.conexao.commit()
        except Error as ex:
            messagebox.showerror('Erro', str(ex))

    def ler_campos(self, query, params=()):
        self.conexao = connect('data/clientesDB.sqlite')
        try:
            with self.conexao:
                self.cursor = self.conexao.cursor()
                self.cursor.execute(query, params)
                return self.cursor.fetchall()
        except Error as ex:
            messagebox.showerror('Erro', str(ex))
        finally:
            if self.conexao:
                self.conexao.close()


    def deleta_registro(self, id, query):
        self.conexao = connect('data/ClientesDB.sqlite')
        try:
            with self.conexao:
                self.cursor = self.conexao.cursor()
                self.cursor.execute(query, (id,))
                self.conexao.commit()
        except Error as ex:
            messagebox.showerror('Erro', str(ex))