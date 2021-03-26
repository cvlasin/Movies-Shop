import tkinter as tk
import FilmeFunktionen as g
import BestellungFunktionen as c
import GUI as m
def order():
    u = c.Bestellung(1, 1, 'a')
    f = g.film("a", 1, 1, "a", 1)

    r1 = tk.Tk()
    r1.title("Bestellungen Filme")
    r1.geometry("350x350")
    def back():
        m.meniu()
    def addtolist():
        Lista1 = []
        for item in varList1:
            if item.get() != "":
                Lista1.append(item.get())
        u.preluare_comanda(entry1.get(),Lista1)
        r1.destroy()
        back()

    label1 = tk.Label(r1, text='ID')
    label1.config(font=('times', 10, 'bold'), pady=0)
    label1.place(x=130, y=0)
    entry1 = tk.Entry(r1)
    entry1.place(x=0, y=0)

    l1 = []
    l1 = f.extragere_filme(l1)
    varList1 = []

    class Check:
        x = 30

        def __init__(self, lbl):
            self.var = tk.StringVar()
            self.cb = tk.Checkbutton(r1, text=lbl, variable=self.var, onvalue=lbl, offvalue="")
            self.cb.place(x = 0, y = Check.x)
            Check.x += 30
            varList1.append(self.var)

    for el in l1:
        Check(el)

    b1 = tk.Button(r1, text="Submit order", command=addtolist)
    b1.place(x=100, y = 30)
    r1.mainloop()

