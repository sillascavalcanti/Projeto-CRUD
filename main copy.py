import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

main = customtkinter.CTk()
main.geometry('500x400')

def login():
    print('Login efetuado')

frame = customtkinter.CTkFrame(master=main)
frame.pack(pady=20, padx=60, fill='both', expand=True)

titulo = customtkinter.CTkLabel(master=frame, text='Login', font=('Roboto', 24, 'bold'))
titulo.pack(pady=12,padx=10)

caixa_login = customtkinter.CTkEntry(master=frame, placeholder_text='Login')
caixa_login.pack(pady=12, padx=10)

caixa_senha = customtkinter.CTkEntry(master=frame, placeholder_text='Senha', show='*')
caixa_senha.pack(pady=12, padx=10)

botao = customtkinter.CTkButton(master=frame, text='Login', command=login)
botao.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='Lembrar-me')
checkbox.pack(pady=12, padx=10)

main.mainloop()

