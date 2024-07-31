import tkinter as tk
from tkinter import Label, messagebox
import comtypes.client
import os
import shutil

from src import UI, Setup

# Cambia el siguiente valor a True para incluir el botón de abrir PDF
include_pdf_button = True
# Cambia el siguiente valor a True para abrir la presentación al iniciar la aplicación
open_presentation_at_startup = True

# Coloca aquí el nombre del archivo de presentación
ppt_file_name = ""
# Nombre del archivo PDF
pdf_file_name = ""
# Nombre del archivo copiado
ppdata_file_name = "ppdata"

# Directorio de archivos de la aplicación en la carpeta personal del usuario
app_files_dir = os.path.join(os.path.expanduser("~"), ".pptexe_py_data")
# Ruta completa del archivo copiado
ppdata_file_path = os.path.join(app_files_dir, ppdata_file_name)

# Variable para guardar el estado de la presentación
presentation = None

def get_app_path():
    """Obtiene la ruta del directorio de la aplicación."""
    return os.path.dirname(__file__)

def load_setup():
    """Carga el archivo setup.ini."""
    global include_pdf_button, ppt_file_name, pdf_file_name, open_presentation_at_startup

    setup = Setup.get_setup()

    include_pdf_button = setup.getboolean('actions', 'active_pdf_button')
    open_presentation_at_startup = setup.getboolean('actions', 'open_presentation_at_startup')
    ppt_file_name = setup.get('files', 'presentation_file_name')
    pdf_file_name = setup.get('files', 'pdf_file_name')


def initialize_app():
    """Inicializa la aplicación creando el archivo necesario en el directorio del usuario."""
    if not os.path.exists(app_files_dir):
        os.makedirs(app_files_dir)
        
    if not os.path.exists(ppdata_file_path):
        resource_path = os.path.join(get_app_path(), "resources", ppt_file_name)
        if os.path.exists(resource_path):
            shutil.copyfile(resource_path, ppdata_file_path)
        else:
            messagebox.showerror("Error", f"No se encuentra el archivo de recursos: {resource_path}")
            return
        # copy all extra files from resources to app_files_dir
        for file in os.listdir(os.path.join(get_app_path(), "resources")):
            if file != ppt_file_name and file != 'put_files_here':
                shutil.copyfile(os.path.join(os.path.join(get_app_path(), "resources"), file), os.path.join(app_files_dir, file))


def open_presentation():
    """Crea una instancia de Powerpoint y abre la presentación en modo de vista protegida y solo lectura."""
    global presentation

    try:
        # Crear una instancia de Powerpoint
        powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
        powerpoint.Visible = True

        # Abrir la presentación en modo de vista protegida
        presentation = powerpoint.Presentations.Open(ppdata_file_path, ReadOnly=False, WithWindow=False)

        # Iniciar la presentación en modo de presentación de diapositivas
        presentation.SlideShowSettings.Run()

    except Exception as e:
        messagebox.showerror("Error", f"Error al abrir la presentación: {e}")

def save_presentation_state():
    """Guarda el estado de la presentación."""
    global presentation

    try:
        if presentation:
            presentation.Save()
            messagebox.showinfo("Genial", "El estado de la presentación se ha guardado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "No hay ninguna presentación abierta para guardar.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar la presentación: {e}")

def open_pdf():
    """Abre el archivo PDF con la aplicación por defecto del sistema."""
    global pdf_file_name

    file_path = os.path.join(get_app_path(), "resources", pdf_file_name)
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"No se encuentra el archivo: {file_path}")
        return

    try:
        os.startfile(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Error al abrir el PDF: {e}")

# Ejecutar la aplicación
if __name__ == "__main__":
    load_setup()
    initialize_app()

    # Abrir la presentación al iniciar
    if open_presentation_at_startup:
        open_presentation()

    # Generar UI
    root = UI().root

    # Crear un botón para abrir la presentación
    open_button = tk.Button(root, text="Abrir Presentación", command=open_presentation)
    open_button.pack(pady=10)

    # Crear un botón para guardar el estado de la presentación
    save_button = tk.Button(root, text="Guardar Presentación", command=save_presentation_state)
    save_button.pack(pady=10)

    # Verificar si se incluye el botón de abrir PDF
    if include_pdf_button:
        pdf_button = tk.Button(root, text="Abrir PDF", command=open_pdf)
        pdf_button.pack(pady=10)

    # Ejecutar la aplicación
    root.mainloop()
