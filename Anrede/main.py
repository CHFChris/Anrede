import tkinter as tk
from funktionen import verbinde_datenbank, anrede_hinzufuegen

def speichern():
    anrede = eingabe.get()
    anrede_hinzufuegen(conn, anrede)
    listebox.insert(tk.END, anrede)
    eingabe.delete(0, tk.END)

conn = verbinde_datenbank()

root = tk.Tk()
root.title("Anrede Verwaltung")

tk.Label(root, text="Neue Anrede eingeben:").pack(padx=10, pady=5)

eingabe = tk.Entry(root, width=40)
eingabe.pack(padx=10, pady=5)

speicher_button = tk.Button(root, text="Anrede speichern", command=speichern)
speicher_button.pack(padx=10, pady=5)

tk.Label(root, text="Gespeicherte Anreden:").pack(padx=10, pady=(10, 0))

listebox = tk.Listbox(root, width=40)
listebox.pack(padx=10, pady=5)

root.mainloop()
