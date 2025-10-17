import tkinter as tk
from tkinter import messagebox

# Criando janela principal da aplicação
janelaPrincipal = tk.Tk()
janelaPrincipal.title("Calculadora primitiva moderna")

# Criando os widgets
lblValorA = tk.Label(janelaPrincipal, text="Valor A:")
lblValorB = tk.Label(janelaPrincipal, text="Valor B:")

entValorA = tk.Entry(janelaPrincipal)
entValorB = tk.Entry(janelaPrincipal)

def somar():
    valorA = int(entValorA.get())
    valorB = int(entValorB.get())

    soma = valorA + valorB
    messagebox.showinfo("Resposta", f"{soma}")

btSomar = tk.Button(janelaPrincipal, text="+", command=somar)

lblValorA.grid(row=0, column=0)
entValorA.grid(row=0, column=1)
lblValorB.grid(row=1, column=0)
entValorB.grid(row=1, column=1)
btSomar.grid(row=2, column=1)



# Rodando o loop principal da aplicação
janelaPrincipal.mainloop()