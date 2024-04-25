from config.modulos import *

class JanelaPrincipal():
    def __init__(self) -> None:
        self.set_var()
        self.dimensao()
        self.widgets()
        self.root.mainloop()

    def set_var(self):
        self.instancia_f = funcoes()
        self.cor = cor()
        self.root = Tk()
        self.id = StringVar()
        self.nome_completo = StringVar()
        self.email = StringVar()
        self.telefone = StringVar()
        self.endereco = StringVar()
        self.tipos = ['Código', 'Nome', 'E-mail', 'Telefone', 'Endereço']
        self.tipo_selecionado = StringVar()
        self.procurar_dados = StringVar()
        self.tabela_head = ['Código', 'Nome', 'E-mail', 'Endereço', 'Telefone']
        self.lista = []
        self.id = StringVar()

    def dimensao(self):
        self.root.title('Cadastro de clientes')
        self.root.iconbitmap('images/icone_janela.ico')
        self.root.configure(background=self.cor.cor_fundo)
        self.root.resizable(False, False)
        # dimensões da janela
        self.width = 800
        self.height = 600
        # resolução do nosso sistema
        self.width_screen = self.root.winfo_screenwidth()
        self.height_screen = self.root.winfo_screenheight()
        # posição da janela
        self.posx = self.width_screen/2 - self.width/2
        self.posy = self.height_screen/2 - self.height/2
        # definir a geometry
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, self.posx, self.posy))

    def widgets(self):
        # Label
        self.lbl_id = Label(self.root, text='Código:', bg=self.cor.cor_fundo, fg=self.cor.cor_texto_label, font=('Helvetica', 10, 'bold'))
        self.lbl_nome_completo = Label(self.root, text='Nome Completo:', bg=self.cor.cor_fundo, fg=self.cor.cor_texto_label, font=('Helvetica', 10, 'bold'))
        self.lbl_email = Label(self.root, text='E-mail:', bg=self.cor.cor_fundo, fg=self.cor.cor_texto_label, font=('Helvetica', 10, 'bold'))
        self.lbl_endereco = Label(self.root, text='Endereço:', bg=self.cor.cor_fundo, fg=self.cor.cor_texto_label, font=('Helvetica', 10, 'bold'))
        self.lbl_telefone = Label(self.root, text='Telefone:', bg=self.cor.cor_fundo, fg=self.cor.cor_texto_label, font=('Helvetica', 10, 'bold'))

        # Entry
        self.ety_id = Entry(self.root, textvariable=self.id, width=10, state='readonly')
        self.ety_nome_completo = Entry(self.root, textvariable=self.nome_completo)
        self.ety_email = Entry(self.root, textvariable=self.email)
        self.ety_endereco = Entry(self.root, textvariable=self.endereco)
        self.ety_telefone = Entry(self.root, textvariable=self.telefone)
        self.ety_procurar = Entry(self.root, textvariable=self.procurar_dados, width=20)

        # ComboBox
        self.cbx_tipo = Combobox(self.root, textvariable=self.tipo_selecionado, values=self.tipos, width=20)
        self.tipo_selecionado.set('Código')

        # Button
        self.btn_procurar = Button3d(self.root, text='Procurar', bg=cor.cor_botao, command=self.procurar)
        self.btn_salvar_alterar = Button3d(self.root, text='Salvar', bg=cor.cor_botao, command=self.salvar_alterar)
        self.btn_novo = Button3d(self.root, text='Novo', bg=cor.cor_botao, command=self.novo)
        self.btn_excluir = Button3d(self.root, text='Excluir', bg=cor.cor_botao, command=self.excluir)


        # TreeView
        self.tvw = Treeview(self.root, columns=self.tabela_head, show='headings')
        for col in self.tabela_head:
            if col == 'Código':
                self.tvw.column(col, width=25, anchor='center')  
            elif col == 'Nome':
                self.tvw.column(col, width=100, anchor='center') 
            elif col == 'E-mail':
                self.tvw.column(col, width=130, anchor='center')
            elif col == 'Endereço':
                self.tvw.column(col, width=170, anchor='center')
            elif col == 'Telefone':
                self.tvw.column(col, width=50, anchor='center')
            else:
                self.tvw.column(col, width=100, anchor='center')
            self.tvw.heading(col, text=col)

        # Layout label
        self.lbl_id.place(x=10, y=10,)
        self.lbl_nome_completo.place(x=10, y=40)
        self.lbl_email.place(x=10, y=70)
        self.lbl_endereco.place(x=10, y=100,)
        self.lbl_telefone.place(x=10, y=130)

        # Layout entry
        self.ety_id.place(x=130, y=11, width=40, height=21)
        self.ety_nome_completo.place(x=130, y=41, width=650, height=21)
        self.ety_email.place(x=130, y=71, width=650, height=21)
        self.ety_endereco.place(x=130, y=101, width=650, height=21)
        self.ety_telefone.place(x=130, y=131, width=150, height=21)
        self.ety_procurar.place(x=130, y=161, width=440, height=21)

        # Layout ComboBox
        self.cbx_tipo.place(x=10, y=161, width=110)

        # Layout Button
        self.btn_procurar.place(x=580, y=152, width=200, height=40)
        self.btn_salvar_alterar.place(x=10, y=550, width=250, height=40)
        self.btn_novo.place(x=275, y=550, width=250, height=40)
        self.btn_excluir.place(x=540, y=550, width=250, height=40)

        # Layout TreeView
        self.tvw.place(x=10, y=200, width=780, height=340) 
        self.tvw.bind('<ButtonRelease-1>', self.on_one_click)

        self.limpar_campos()
        self.att_treeview()

    def entrada_nomes(self, valor):
        if (len(valor) > 30):
            return False
        return funcoes.testa_valor_entrada(funcoes, valor)
    
    def procurar(self):
        self.tvw.delete(*self.tvw.get_children())
        tipo_procura = self.tipos.index(self.tipo_selecionado.get())
        valor_procurado = self.procurar_dados.get()
        query = ''
        params = ()

        if tipo_procura == 0:  # Código
            try:
                valor_procurado = int(valor_procurado)
                query = 'SELECT * FROM Cadastro WHERE id = ?'
                params = (valor_procurado,)
            except ValueError:
                messagebox.showinfo("Aviso", "Por favor, insira um número válido para ID.")
                return
        elif tipo_procura == 1:  # Nome
            query = 'SELECT * FROM Cadastro WHERE nome_completo LIKE ?'
            params = (f'%{valor_procurado}%',)
        elif tipo_procura == 2:  # E-mail
            query = 'SELECT * FROM Cadastro WHERE email LIKE ?'
            params = (f'%{valor_procurado}%',)
        elif tipo_procura == 3:  # Telefone
            query = 'SELECT * FROM Cadastro WHERE telefone LIKE ?'
            params = (f'%{valor_procurado}%',)
        elif tipo_procura == 4:  # Endereço
            query = 'SELECT * FROM Cadastro WHERE endereco LIKE ?'
            params = (f'%{valor_procurado}%',)

        if query:
            self.lista_clientes = self.instancia_f.ler_campos(query, params)
            for cliente in self.lista_clientes:
                self.tvw.insert('', 'end', values=cliente)

    def salvar_alterar(self):
        if self.id.get() == '':
            self.instancia_f.inserir_4_campos(self.nome_completo.get().upper(), self.email.get().upper(), self.endereco.get().upper(), self.telefone.get(), 'INSERT INTO Cadastro (nome_completo, email, endereco, telefone) VALUES (?, ?, ?, ?)')
            self.lista = ['Salvando', 'Cliente salvo com sucesso!!!']
        elif self.id.get() != '':
            self.instancia_f.atualiza_4_campos(self.nome_completo.get().upper(), self.email.get().upper(), self.endereco.get().upper(), self.telefone.get(), self.id.get(), 'UPDATE Cadastro SET nome_completo=?, email=?, endereco=?, telefone=? WHERE id=?')
            self.lista = ['Atualizando', 'Cliente atualizado com sucesso!!!']
        self.limpar_campos()
        self.att_treeview()
        messagebox.showinfo(self.lista[0], self.lista[1])

    def excluir(self):
        if self.id.get() != '':
            self.instancia_f.deleta_registro(self.id.get(), "DELETE FROM Cadastro WHERE id = ?")
            self.att_treeview()
            self.limpar_campos()
            messagebox.showinfo('Deletando', 'Cliente deletado com sucesso!!!')

    def novo(self):
        self.limpar_campos()
        self.att_treeview()
        self.root.focus()

    def limpar_campos(self):
        self.id.set('')
        self.nome_completo.set('')
        self.email.set('')
        self.endereco.set('')
        self.telefone.set('')
        self.btn_salvar_alterar.configure(text='Salvar')

    def att_treeview(self):
        self.tvw.delete(*self.tvw.get_children())
        self.lista_clientes = funcoes.ler_campos(funcoes, 'SELECT * FROM Cadastro ORDER BY id')
        for i in self.lista_clientes:
            self.tvw.insert('', END, values=i)
    
    def on_one_click(self, event):
        self.limpar_campos()
        self.selecao = self.tvw.focus()
        self.valores = self.tvw.item(self.selecao, 'values')
        self.valor = funcoes.ler_campos(funcoes, f'SELECT * FROM Cadastro WHERE id = {self.valores[0]}')
        self.id.set(self.valores[0])
        self.nome_completo.set(self.valor[0][1])
        self.email.set(self.valor[0][2])
        self.endereco.set(self.valor[0][3])
        self.telefone.set(self.valor[0][4])
        self.btn_salvar_alterar.configure(text='Atualizar')


JanelaPrincipal()
