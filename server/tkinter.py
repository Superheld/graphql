# main.py
import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Vorlage")
        self.geometry("400x300")

        # Erstellen des Menüs
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Datei-Menü
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Öffne Tabelle", command=self.open_table)
        file_menu.add_command(label="Öffne Eingabeformular", command=self.open_input_form)

    def open_table(self):
        # Hier kannst du den Code einfügen, um die Tabelle zu öffnen
        table_window = tk.Toplevel(self)
        table_window.title("Tabelle")
        table_window.geometry("600x400")

        # Beispiel für eine Tabelle mit ttk.Treeview
        columns = ("Spalte1", "Spalte2", "Spalte3")
        tree = ttk.Treeview(table_window, columns=columns, show="headings")
        tree.pack(expand=True, fill=tk.BOTH)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER)

        # Beispiel-Daten einfügen
        data = [
            ("Daten1", "Daten2", "Daten3"),
            ("Daten4", "Daten5", "Daten6"),
            ("Daten7", "Daten8", "Daten9")
        ]

        for item in data:
            tree.insert("", tk.END, values=item)

    def open_input_form(self):
        # Hier kannst du den Code einfügen, um das Eingabeformular zu öffnen
        input_window = tk.Toplevel(self)
        input_window.title("Eingabeformular")
        input_window.geometry("400x200")

        # Beispiel für ein Eingabeformular
        label = ttk.Label(input_window, text="Name:")
        label.pack(pady=10)

        entry = ttk.Entry(input_window)
        entry.pack(pady=10)

        button = ttk.Button(input_window, text="Speichern", command=lambda: self.save_input(entry.get()))
        button.pack(pady=10)

    def save_input(self, input_text):
        # Hier kannst du den Code einfügen, um die Eingabe zu speichern
        print(f"Eingabe gespeichert: {input_text}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()