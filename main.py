import tkinter as tk
from tkinter import Label, messagebox
import comtypes.client
import os

# cambia este valor a True para incluir el botón de abrir PDF
include_pdf_button = False
# coloca aquí el nombre del archivo de presentación
ppt_file_name = "presentation.ppsm"
# coloca aquí el nombre del archivo PDF, este debe ser el mismo nombre que utiliza la presentación para abrir el archivo
pdf_file_name = "TFG-L1023.pdf"

def open_presentation():
    """open_presentation:
    Crea una instancia de Powerpoint y abre la presentación en modo de vista protegida y solo lectura.
    """
    global ppt_file_name

    # cargar el archivo de presentación
    file_path = os.path.join(os.path.dirname(__file__), "resources", ppt_file_name)
    # verificar si el archivo existe
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"No se encuentra el archivo: {file_path}")
        return
    
    # abrir la presentación
    try:
        # Crear una instancia de Powerpoint
        powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
        powerpoint.Visible = True
        
        # Abrir la presentación en modo de vista protegida
        presentation = powerpoint.Presentations.Open(file_path, ReadOnly=False, WithWindow=False)
        
        # Iniciar la presentación en modo de presentación de diapositivas
        presentation.SlideShowSettings.Run()
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al abrir la presentación: {e}")

def open_pdf():
    """
    Abre el archivo PDF con la aplicación por defecto del sistema.
    """
    global pdf_file_name

    file_path = os.path.join(os.path.dirname(__file__), "resources", pdf_file_name)
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"No se encuentra el archivo: {file_path}")
        return
    
    try:
        os.startfile(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Error al abrir el PDF: {e}")

# Ejecutar la aplicación
if __name__ == "__main__":

    # Crear la ventana principal
    root = tk.Tk()
    root.title("pptexe-pyapp")
    root.geometry("300x120")

    # Crear un botón para abrir la presentación
    open_button = tk.Button(root, text="Abrir Presentación", command=open_presentation)
    open_button.pack(pady=10)
    
    # verificar si se incluye el botón de abrir PDF
    if (include_pdf_button):
        # create button to open pdf file
        open_button = tk.Button(root, text="Abrir PDF", command=open_pdf)
        open_button.pack(pady=10)

    # dev contact
    label = Label(root, text="Desarrollado por: andresangulodev@gmail.com")
    label.pack()

    # Ejecutar la aplicación
    root.mainloop()
