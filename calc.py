import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("260x300")

mostrador = tk.Entry(janela)
oper1 = None
oper2 = None
resultado = 0
mostrador.insert(0, resultado)

def somar():
    global oper1
    global oper2
    global resultado

    valor = int(mostrador.get())

    if (not oper1):
        oper1 = valor
        mostrador.delete(0, tk.END)
    else:
        oper2 = valor
        # já que agora tenho os dois operandos, posso fazer a operação
        resultado = oper1 + oper2
        mostrador.delete(0, tk.END)
        mostrador.insert(0, resultado)

        # rotação dos operandos
        oper1 = resultado
        oper2 = None


def subtrair():
    global memoria
    valor = int(mostrador.get())
    memoria = memoria - valor
    mostrador.delete(0, tk.END)
    mostrador.insert(0, memoria)

def multiplicar():
    global memoria
    valor = int(mostrador.get())
    memoria = memoria * valor
    mostrador.delete(0, tk.END)
    mostrador.insert(0, memoria)

def dividir():
    global memoria
    valor = int(mostrador.get())
    memoria = memoria / valor
    mostrador.delete(0, tk.END)
    mostrador.insert(0, memoria)

def clear():
    global oper1, oper2, resultado
    oper1 =  None
    oper2 = None
    resultado = 0
    mostrador.delete(0, tk.END)
    mostrador.insert(0, resultado)

btSomar = tk.Button(janela, text="+", command=somar)
btSubtrair = tk.Button(janela, text="-", command=subtrair)
btMultiplicar = tk.Button(janela, text="x", command=multiplicar)
btDividir = tk.Button(janela, text="÷", command=dividir)
btClear = tk.Button(janela, text="c", command=clear)

mostrador.grid(row=0, column=1)
btSomar.grid(row=1, column=1)
btClear.grid(row=1, column=2)
btSubtrair.grid(row=2, column=2)
btMultiplicar.grid(row=3, column=2)
btDividir.grid(row=4, column=2)



janela.mainloop()