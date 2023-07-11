import customtkinter

class TelaPrincipal():
    def __init__(self,tela):
        # Configuracao de tela
        self.janela = tela
        self.janela.geometry('500x400')
        self.janela.resizable(width='false', height='false')
        self.janela.title('Login')
        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('blue')

        # componentes da tela inicial
        self.frame = customtkinter.CTkFrame(master=self.janela)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        self.titulo = customtkinter.CTkLabel(master=self.frame, text='Login', font=('Roboto', 24, 'bold'))
        self.titulo.pack(pady=12,padx=10)

        self.caixa_login = customtkinter.CTkEntry(master=self.frame, placeholder_text='Login')
        self.caixa_login.pack(pady=12, padx=10)

        self.caixa_senha = customtkinter.CTkEntry(master=self.frame, placeholder_text='Senha', show='*')
        self.caixa_senha.pack(pady=12, padx=10)

        self.botao_login = customtkinter.CTkButton(master=self.frame, text='Login', command=self.login)
        self.botao_login.pack(pady=12, padx=10)

        self.botao_cadastro = customtkinter.CTkButton(master=self.frame, text='Cadastro', command=self.cadastro)
        self.botao_cadastro.pack(pady=12, padx=10)

        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text='Lembrar-me')
        self.checkbox.pack(pady=12, padx=10)




    # Funcao LOGIN
    def login(self):
        print('Login efetuado')

    # Função cadastro
    def cadastrar(self):
        print('Cadastro efetuado')
    def cadastro(self):
        # configuração da tela cadastro
        self.janela.withdraw()
        self.janela2 = customtkinter.CTkToplevel()
        self.janela2.geometry('500x400')
        self.janela2.title('Cadastro')
        self.janela2.resizable(width='false', height='false')
        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('blue')
        # conponentes do janela2

        self.frame = customtkinter.CTkFrame(master=self.janela2)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        self.titulo = customtkinter.CTkLabel(master=self.frame, text='Cadastro', font=('Roboto', 24, 'bold'))
        self.titulo.pack(pady=5,padx=10)

        self.label_nome = customtkinter.CTkLabel(master=self.frame, text='Nome Completo',
                                                font=('roboto', 10, 'bold'))
        self.label_nome.pack(pady=0, padx=10)
        self.caixa_nome = customtkinter.CTkEntry(master=self.frame, placeholder_text='Nome Sobrenome')
        self.caixa_nome.pack(pady=0, padx=10)

        self.label_cpf = customtkinter.CTkLabel(master=self.frame, text='CPF',
                                                font=('roboto', 10, 'bold'))
        self.label_cpf.pack(pady=0, padx=10)
        self.caixa_cpf = customtkinter.CTkEntry(master=self.frame, placeholder_text='000.000.000-00')
        self.caixa_cpf.pack(pady=0, padx=10)

        self.label_data = customtkinter.CTkLabel(master=self.frame, text='Data de nascimento',
                                                font=('roboto', 10, 'bold'))
        self.label_data.pack(pady=0, padx=10)
        self.caixa_data = customtkinter.CTkEntry(master=self.frame, placeholder_text='00/00/0000')
        self.caixa_data.pack(pady=0, padx=10)

        self.label_senha = customtkinter.CTkLabel(master=self.frame, text='Senha',
                                                font=('roboto', 10, 'bold'))
        self.label_senha.pack(pady=0, padx=10)

        self.caixa_senha = customtkinter.CTkEntry(master=self.frame, placeholder_text='Senha', show='*')
        self.caixa_senha.pack(pady=0, padx=10)

        self.label_confirmarsenha = customtkinter.CTkLabel(master=self.frame, text='Confirme a senha',
                                                font=('roboto', 10, 'bold'))
        self.label_confirmarsenha.pack(pady=0, padx=10)

        self.caixa_confirmarsenha = customtkinter.CTkEntry(master=self.frame, placeholder_text='confirme a senha', show='*')
        self.caixa_confirmarsenha.pack(pady=0, padx=10)

        self.botao_cadastrar = customtkinter.CTkButton(master=self.frame, text='Cadastrar', command=self.cadastrar)
        self.botao_cadastrar.pack(pady=5, padx=10)

        self.janela2.mainloop()

tela = customtkinter.CTk()
objeto = TelaPrincipal(tela)
tela.mainloop()