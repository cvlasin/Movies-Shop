import tkinter as tk
import BenutzerFunktionen as f
import FilmeFunktionen as g
import BestellungFunktionen as c
import Bestellung as com

def ord_func():
    u = c.Bestellung(1, 1, 'a')
    f = g.film("a", 1, 1, "a", 1)

    r1 = tk.Tk()
    r1.title("Bestellungen Filme")
    r1.geometry("350x350")
    def back():
        r1.destroy()
        meniu()
    def addtolist():
        Lista1 = []
        for item in varList1:
            if item.get() != "":
                Lista1.append(item.get())
        u.preluare_comanda(entry1.get(),Lista1)
        back()

    label1 = tk.Label(r1, text='ID')
    label1.config(font=('Helvetica', 12), pady=0)
    label1.place(x=130, y=0)
    entry1 = tk.Entry(r1)
    entry1.place(x=0, y=0)

    l1 = []
    l1 = f.extragere_filme(l1)  # lista cu filmele existente
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

    b1 = tk.Button(r1, text="Bestellung beenden", command=addtolist)
    b1.place(x=100, y = 30)
    r1.mainloop()

def meniu():
    root = tk.Tk()
    root.title("Hauptmenu")
    root.geometry("1024x720")

    def menu_user_action():
        root.destroy()
        def back():
            window.destroy()
            meniu()

        def adaugare_func():
            def validate():
                u = f.Benutzer("a", "a", 1)
                u.add(entry1.get(),entry2.get(),entry3.get())
                u.adaugare_in_fisier()
                r.destroy()

            r = tk.Tk()
            r.geometry("350x350")
            validare = tk.Button(r, text="Enter", command=validate)
            validare.place(x=0, y= 90)

            label1 = tk.Label(r, text='Name')
            label1.config(font=('Helvetica', 12), pady=0)
            label1.place(x=130, y=0)
            entry1 = tk.Entry(r)
            entry1.place(x=0,y=0)

            label2 = tk.Label(r, text='Vorname')
            label2.config(font=('Helvetica', 12), pady=0)
            label2.place(x=130, y=30)
            entry2 = tk.Entry(r)
            entry2.place(x=0, y=30)

            label3 = tk.Label(r, text='ID')
            label3.config(font=('Helvetica', 12), pady=0)
            label3.place(x=130, y=60)
            entry3 = tk.Entry(r)
            entry3.place(x=0, y=60)
            r.mainloop()

        def modificare_func():
            def validate():
                u = f.Benutzer("a", "a", 1)
                u.modificare_prenume(entry2.get(),entry1.get())
                r.destroy()

            r = tk.Tk()
            r.geometry("350x350")
            validare = tk.Button(r, text="Enter", command=validate)
            validare.place(x=0, y= 60)

            label1 = tk.Label(r, text='Neues Vorname')
            label1.config(font=('Helvetica', 12), pady=0)
            label1.place(x=130, y=0)
            entry1 = tk.Entry(r)
            entry1.place(x=0,y=0)

            label2 = tk.Label(r, text='ID')
            label2.config(font=('Helvetica', 12), pady=0)
            label2.place(x=130, y=30)
            entry2 = tk.Entry(r)
            entry2.place(x=0, y=30)
            r.mainloop()

        def stergere_func():
            def validate():
                u = f.Benutzer("a", "a", 1)
                u.delete_benutzer(entry1.get())
                r.destroy()

            r = tk.Tk()
            r.geometry("350x350")
            validare = tk.Button(r, text="Enter", command=validate)
            validare.place(x=0, y=30)

            label1 = tk.Label(r, text='ID')
            label1.config(font=('Helvetica', 12), pady=0)
            label1.place(x=130, y=0)
            entry1 = tk.Entry(r)
            entry1.place(x=0, y=0)
            r.mainloop()

        def afisare_func():
            u = f.Benutzer("a", "a", 1)
            l = []
            l = u.afisare_useri(l)
            root = tk.Tk()
            t = tk.Text(root)
            for x in l:
                t.insert(tk.END, x + '\n')
            t.pack()
            root.mainloop()


        window = tk.Tk()
        window.title("Menu Benutzer")
        window.geometry("1024x720")
        label = tk.Label(window, text='Menu Benutzer')
        label.config(font=('Helvetica', 40, 'bold'), pady=50)
        label.place(x=0, y=20)

        adaugare = tk.Button(window, text = "Fugen ein Benutzer hin", command = adaugare_func, bg='blue', height=2)
        adaugare.place(x=0, y=150)

        modificare = tk.Button(window, text="Vorname verandern", command=modificare_func, bg='blue', height=2)
        modificare.place(x=0, y=200)

        stergere = tk.Button(window, text="Loschung von einer Benutzer", command=stergere_func, bg='blue', height=2)
        stergere.place(x=0, y=250)

        afisare = tk.Button(window, text="Anzeige Liste von Benutzer", command=afisare_func,  bg='blue', height=2)
        afisare.place(x=0, y=300)

        back_button = tk.Button(window, text='Back', command = back)
        back_button.place(x=0, y=400)

    def menu_film_action():
        root.destroy()
        def back():
            window.destroy()
            meniu()

        def adaugare_func():
            def validate():
                u = g.film("a", 1, 1, "a",1)
                u.add_film(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get())
                u.adaugare_in_fisier()
                r.destroy()

            r = tk.Tk()
            r.geometry("350x350")
            validare = tk.Button(r, text="Enter", command=validate)
            validare.place(x=0, y= 150)

            label1 = tk.Label(r, text='Titel')
            label1.config(font=('Helvetica', 12), pady=0)
            label1.place(x=130, y=0)
            entry1 = tk.Entry(r)
            entry1.place(x=0,y=0)

            label2 = tk.Label(r, text='Jahr')
            label2.config(font=('Helvetica', 12), pady=0)
            label2.place(x=130, y=30)
            entry2 = tk.Entry(r)
            entry2.place(x=0, y=30)

            label3 = tk.Label(r, text='Rating')
            label3.config(font=('Helvetica', 12), pady=0)
            label3.place(x=130, y=60)
            entry3 = tk.Entry(r)
            entry3.place(x=0, y=60)

            label4 = tk.Label(r, text='Schauspielern')
            label4.config(font=('Helvetica', 12), pady=0)
            label4.place(x=130, y=90)
            entry4 = tk.Entry(r)
            entry4.place(x=0, y=90)

            label5 = tk.Label(r, text='Preis')
            label5.config(font=('Helvetica', 12), pady=0)
            label5.place(x=130, y=120)
            entry5 = tk.Entry(r)
            entry5.place(x=0, y=120)

            r.mainloop()
        
        def modificare_func():
            def validate():
                u = g.film("a", 1, 1, "a",1)
                u.modificare_pret(entry1.get(),entry2.get())
                r.destroy()

            r = tk.Tk()
            r.geometry("350x350")
            validare = tk.Button(r, text="Enter", command=validate)
            validare.place(x=0, y= 60)

            label1 = tk.Label(r, text='Titel')
            label1.config(font=('Helvetica', 12), pady=0)
            label1.place(x=130, y=0)
            entry1 = tk.Entry(r)
            entry1.place(x=0,y=0)

            label2 = tk.Label(r, text='Neuer Preis')
            label2.config(font=('Helvetica', 12), pady=0)
            label2.place(x=130, y=30)
            entry2 = tk.Entry(r)
            entry2.place(x=0, y=30)
            r.mainloop()

        def afisare_func():
            u = g.film("a", 1, 1, "a",1)
            l = []
            l = u.afisare_filme(l)
            root = tk.Tk()
            t = tk.Text(root)
            for x in l:
                t.insert(tk.END, x + '\n')
            t.pack()
            root.mainloop()

        window = tk.Tk()
        window.title("Menu Filme")
        window.geometry("1024x720")
        label = tk.Label(window, text='Menu Filme')
        label.config(font=('Helvetica', 35, 'bold'), pady=50)
        label.place(x=0, y=20)

        adaugare = tk.Button(window, text="Fugen ein Film hin", command=adaugare_func, bg='red', height='2')
        adaugare.place(x=0, y=150)

        modificare = tk.Button(window, text="Preis verandern", command=modificare_func, bg='red', height='2')
        modificare.place(x=0, y=200)

        afisare = tk.Button(window, text="Anzeige Liste von Filme", command=afisare_func, bg='red', height='2')
        afisare.place(x=0, y=250)

        back_button = tk.Button(window, text='Back', command=back)
        back_button.place(x=0, y=400)

    def menu_gem_action():
        root.destroy()
        def comanda_functie():
            window.destroy()
            ord_func()

        def back():
            window.destroy()
            meniu()

        def afisare_func():
            u = c.Bestellung(1, 1, 'a')
            l = []
            l = u.output_bestellung(l)
            root4 = tk.Tk()
            t = tk.Text(root4)
            for x in l:
                t.insert(tk.END, x + '\n')
            t.pack()
            root4.mainloop()

        def rating_func():
            def validate():
                u = c.Bestellung(1, 1, 'a')
                l = []
                l = u.cautare_nota(l,entry1.get())
                r.destroy()
                root2 = tk.Tk()
                t = tk.Text(root2)
                for x in l:
                    t.insert(tk.END, x + '\n')
                t.pack()
                root2.mainloop()

            r = tk.Tk()
            r.geometry("350x350")
            validare = tk.Button(r, text="Search", command=validate)
            validare.place(x=0, y=30)

            label1 = tk.Label(r, text='Rating grosser als')
            label1.config(font=('Helvetica', 12), pady=0)
            label1.place(x=130, y=0)
            entry1 = tk.Entry(r)
            entry1.place(x=0, y=0)

        def actor_func():
            def validate():
                u = c.Bestellung(1, 1, 'a')
                l = []
                l = u.search_actors(l, entry1.get())
                r.destroy()
                root3 = tk.Tk()
                t = tk.Text(root3)
                for x in l:
                    t.insert(tk.END, x + '\n')
                t.pack()
                root3.mainloop()

            r = tk.Tk()
            r.geometry("350x350")
            validare = tk.Button(r, text="Search", command=validate)
            validare.place(x=0, y=30)

            label1 = tk.Label(r, text='Schauspieler')
            label1.config(font=('Helvetica', 12), pady=0)
            label1.place(x=130, y=0)
            entry1 = tk.Entry(r)
            entry1.place(x=0, y=0)

        window = tk.Tk()
        window.title("Menu Gemeinsam")
        window.geometry("1024x720")
        label = tk.Label(window, text='Menu Gemeinsam')
        label.config(font=('Helvetica', 35, 'bold'), pady=50)
        label.place(x=0, y=20)

        comanda = tk.Button(window, text="Bestellung von Filme", command = comanda_functie, bg='yellow', height='2')
        comanda.place(x=0, y=150)

        afisare = tk.Button(window, text="Liste von Benutzer mit aktuelle Bestellungen", command=afisare_func, bg='yellow', height='2')
        afisare.place(x=0, y=200)

        rating = tk.Button(window, text="Suche nach Rating", command=rating_func, bg='yellow', height='2')
        rating.place(x=0, y=250)

        actor = tk.Button(window, text="Suche nach Schauspieler", command=actor_func, bg='yellow', height='2')
        actor.place(x=0, y=300)

        back_button = tk.Button(window, text='Back', command=back)
        back_button.place(x=0, y=400)
        window.mainloop()

    label = tk.Label(root, text = 'Hauptmenu')
    label.config(font = ('Helvetica', 35, 'bold'), pady = 50)
    label.place(x=0 , y = 20)

    menu_user = tk.Button(root, text='Menu Benutzer', command=menu_user_action, bg='blue', height='2' )
    menu_user.place(x=0, y=150)

    menu_film = tk.Button(root, text='Menu Film', command=menu_film_action,  bg='red', height='2')
    menu_film.place(x=0, y=200)

    menu_gem = tk.Button(root, text='Menu Gemeinsam', command=menu_gem_action, bg='yellow', height='2')
    menu_gem.place(x=0, y=250)

    exit_button = tk.Button (root, text = 'Exit', command = quit)
    exit_button.place(x=0, y=400)
    root.mainloop()

meniu()