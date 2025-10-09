import tkinter as tk
from tkinter import messagebox

# Criando a janela principal
janela = tk.Tk()
janela.title("Interatividade com Widgets")
janela.geometry("320x200+400+300") # largura, altura, posição na tela

# Adicionando um rótulo
rotuloNome = tk.Label(janela, text="Digite seu nome:")
rotuloNome.pack()

# Adicionando uma entrada de texto
entradaNome = tk.Entry(janela)
entradaNome.pack()

rotuloSobrenome = tk.Label(janela, text="Digite seu sobrenome:")
rotuloSobrenome.pack()

entradaSobrenome = tk.Entry(janela)
entradaSobrenome.pack()

# Função para exibir mensagem
def exibir_mensagem():
    nome = entradaNome.get()
    sobrenome = entradaSobrenome.get()

    if nome and sobrenome:
        messagebox.showinfo("Saudação", f"Presença confirmada, {nome} {sobrenome}!")
        entradaNome.delete(0, tk.END)
        entradaSobrenome.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira seu nome e sobrenome.")

# Adicionando um botão
botao = tk.Button(janela, text="Confirmar presença", command=exibir_mensagem)
botao.pack()

# Iniciando o loop principal da aplicação
janela.mainloop()