from tkinter import *

janela = Tk()
janela.title('minha primeira tela')
janela['bg'] = 'lightblue'
janela.geometry('400x300+540+150')

#-------------------- Funções ----------------------------
def mostrar():
    try:
        nome = str(ent_nome.get())
        if nome.isalpha():
            idade = int(ent_idade.get())
            if str(idade).isnumeric():
                mensagem['text'] = f'seu nome é {nome}, e idade é {idade}'
        else:
           mensagem['text'] = 'diga seu nome em letras!'
    except ValueError:
        mensagem['text'] = 'Idade é apenas números!'
def outraJanela():
    #janela.withdraw()  # Esconder janela anterior
    janela1 = Toplevel()
    janela1.title('Janela 2')
    janela1['bg'] = 'lightpink'
    janela1.geometry('400x300+540+150')

    janela1.mainloop()
#---------------------------------------------------------

nome= Label(janela, text='digite seu nome: ', font=('arial', 12), bg='lightblue')
nome.pack()
ent_nome= Entry(janela, font=('arial', 12))
ent_nome.pack()
idade= Label(janela, text='digite sua idade: ', font=('arial', 12), bg='lightblue')
idade.pack()
ent_idade= Entry(janela, font=('arial', 12))
ent_idade.pack()

botao= Button(janela, text="salvar", font=('arial', 12), command=mostrar)
botao.pack()

mensagem= Label(janela, font=('arial', 12), bg='lightblue')
mensagem.pack()

botao= Button(janela, text="Criar outra janela", font=('arial', 12), command=outraJanela)
botao.pack()
janela.mainloop()

