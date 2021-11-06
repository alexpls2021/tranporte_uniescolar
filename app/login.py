
def Somar():
    n1 = int(numero1.get())
    n2 = int(numero2.get())
    mostrar['text'] = n1+n2

from tkinter import *

root = Tk()
root.geometry("400x400")
root.title('Login')

numero1 = Entry()
numero1.grid(row=0, column=0)


numero2 = Entry()
numero2.grid(row=1, column=0)


Button(text='somar', command=Somar).grid(row=2, column=0)

mostrar = Label(text="Ressultaso")
mostrar.grid(row=3, column=0)




root.mainloop()






