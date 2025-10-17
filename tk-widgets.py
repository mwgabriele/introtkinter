import tkinter as tk
from tkinter import messagebox

# Criando a janela principal
janela = tk.Tk()
janela.title("Interagindo com um widget")
janela.geometry("320x200+400+300")

# Adicionando um rótulo
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack()

# Adicionando uma entrada de texto
entrada = tk.Entry(janela)
entrada.pack()

# Função para exibir mensagem
def exibir_mensagem():
    nome = entrada.get()
    if nome:
        messagebox.showinfo("Saudação", f"Olá, {nome}!")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira seu nome.")

# Adicionando um botão
botao = tk.Button(janela, text="Enviar", command=exibir_mensagem)
botao.pack()

# Iniciando o loop principal da aplicação
janela.mainloop()