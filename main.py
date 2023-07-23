import customtkinter

class TelaPrincipal():
    def __init__(self,tela):
        # Configuracao de tela
        self.main = tela
        self.main.geometry('500x400')
        self.main.title('Login')
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')

        # componentes da tela inicial
        self.frame = customtkinter.CTkFrame(master=self.main)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        self.titulo = customtkinter.CTkLabel(master=self.frame, text='Login', font=('Roboto', 24, 'bold'))
        self.titulo.pack(pady=12,padx=10)

        self.caixa_login = customtkinter.CTkEntry(master=self.frame, placeholder_text='Login')
        self.caixa_login.pack(pady=12, padx=10)

        self.caixa_senha = customtkinter.CTkEntry(master=self.frame, placeholder_text='Senha', show='*')
        self.caixa_senha.pack(pady=12, padx=10)

        self.botao = customtkinter.CTkButton(master=self.frame, text='Login')
        self.botao.pack(pady=12, padx=10)

        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text='Lembrar-me')
        self.checkbox.pack(pady=12, padx=10)







tela = customtkinter.CTk()
objeto = TelaPrincipal(tela)
tela.mainloop()