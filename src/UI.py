import tkinter as tk
from tkinter import messagebox

from src import Setup


class UI:
    width = "300"
    heigth = "160"

    windwow_title = "pptexe-pyapp"

    root = None

    menu_options = [
        ['Acerca de', 'about'],
        # ['Cambiar arranque', 'set_startup'],
    ]

    def __init__(self):
        self.generate_window()
        self.create_menu()
        self.set_icon()

    def set_icon(self, icon_path = None):
        if icon_path is None:
            icon_path = Setup.get_path() + "/icon.ico"
            
        self.root.iconbitmap(icon_path)
    
    def generate_window(self):
        self.root = tk.Tk()
        self.root.title(self.windwow_title)
        self.root.geometry(f"{self.width}x{self.heigth}")

    def create_menu(self):
        menu_bar = tk.Menu()
        option_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Opciones", menu=option_menu)
        for option in self.menu_options:
            option_menu.add_command(label=option[0], command=getattr(self, option[1]))

            #menu_option.add_command(label=option[0], command=getattr(self, option[1]))
        self.root.config(menu=menu_bar)


    @staticmethod
    def about():
        messagebox.showinfo("Acerca de la aplicación", "Aplicación desarrollada por Andrés Angulo\n\n Contacto: andresangulodev@gmail.com")

    @staticmethod
    def set_startup():
        # create dialog to set startup option from ini file

        return None
