
<h1>PPTEXE-PYAPP 📖</h1>

## Agregar archivos
> En la carpeta **"resources"** del projecto coloca el archivo de presentación y pdf.

> Asegurate de que el nombre de cada archivo sea simple, preferiblemente sin espacios y símbolos especiales.

## Configurar la aplicación
> Edita el archivo **setup.ini** para modificar las variables:
- presentation_file_name:
    - Establece el nombre del archivo de presentación, no olvides incluir la extensión, ejemplo: .pptx o .ppsm
- pdf_file_name:
    - Establece el nombre del archivo PDF que se abrirá con la aplicación.
- active_pdf_button:
    - Valor por defecto ```False```
    - Cambia el valor a ```True``` para permitir que la aplicación incluya el botón de abrir PDF.
- open_presentation_at_startup:
    - Valor por defecto ```True```
    - Cambia el valor a ```False``` para la aplicación no abra la presentación al iniciar.

## Cambiar Icono de la aplicación
> Remplaza el archivo **icon.ico** para cambiar el icono de la aplicación, recuerda que este debe tener el nombre ```icon.ico```
> La extensión debe ser **.ico**
> El icono incluido como ejemplo fue tomado de: [icon-icons](https://icon-icons.com/es/download/51077/ICO/512/)

## Crear y activar entorno virtual
> Para instalar las dependecias de este proyecto es recomendable utilizar un **Entorno Virtual** de trabajo.

> Ejecuta el siguiente comando: 
```sh
python -m venv .env
```

> Activa el entorno virtual con el siguiente comando:
```sh
# En windows:
.env\Scripts\activate.bat
# En sh:
.env\Scripts\activate
```

## Instalar dependecias
> Ejecuta el siguiente comando para instalar las dependecias del proyecto:
```sh
pip install -r requirements.txt
```

## Crear ejecutable

> Ejecuta el siguiente comando para crear el ejecutable:

```sh
pyinstaller --clean main.spec
```