import tkinter as tk

# model
confirmacoes = 0

# controller
def confirmar_presenca():
    global confirmacoes
    confirmacoes = confirmacoes + 1
    print("Presença confirmada")

# view
janela = tk.Tk()
janela.title("Programa para Eventos")
janela.geometry("500x400+300+100")

lblNome = tk.Label(janela, text="Nome:")
lblEmail = tk.Label(janela, text="E-mail:")
btConfirmar = tk.Button(janela, text="Confirmar", command=confirmar_presenca)


lblEmail.pack()
lblNome.pack()
btConfirmar.pack()
janela.mainloop()
