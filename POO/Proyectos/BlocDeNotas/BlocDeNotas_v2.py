import tkinter as tk  # Importamos tkinter para la interfaz gráfica
from tkinter import filedialog, messagebox, simpledialog  # Importamos funciones específicas de tkinter

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root  # La raíz de la ventana principal
        
        # Crear área de texto con la opción de deshacer
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        
        self.current_open_file = ''  # Variable para almacenar el archivo actualmente abierto
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_quit)  # Manejar el evento de cerrar la ventana

        # Detectar cambios en el texto
        self.text_area.bind("<<Modified>>", self.on_modified)
        self.text_modified = False  #  Chivato pa Saber si el texto ha sido modificado

    def on_modified(self, event):
        self.text_modified = True  # Cambiar el chivato si el texto es modificado
        self.text_area.edit_modified(False)  # Restablecer el estado modificado de la área de texto

    def confirm_quit(self):
        # Preguntar al usuario si quiere salir sin guardar los cambios
        if self.text_modified:
            if messagebox.askokcancel("Salir", "Tienes cambios sin guardar. ¿Deseas salir sin guardar?"):
                self.root.destroy()
        else:
            self.root.destroy()

    def open_file(self):
        # Preguntar al usuario si quiere abrir otro archivo sin guardar los cambios
        if self.text_modified:
            if not messagebox.askokcancel("Abrir", "Tienes cambios sin guardar. ¿Deseas abrir otro archivo sin guardar los cambios?"):
                return

        filename = filedialog.askopenfilename()  # Abrir cuadro de diálogo para seleccionar archivo
        if filename:
            self.text_area.delete("1.0", tk.END)  # Borrar contenido actual del área de texto
            with open(filename, "r") as file:
                self.text_area.insert("1.0", file.read())  # Insertar contenido del archivo en el área de texto
            self.current_open_file = filename
            self.text_modified = False  # Restablecer el chivato de modificación

    def new_file(self):
        # Preguntar al usuario si quiere crear un nuevo archivo sin guardar los cambios
        if self.text_modified:
            if not messagebox.askokcancel("Nuevo", "Tienes cambios sin guardar. ¿Deseas crear un nuevo archivo sin guardar los cambios?"):
                return

        self.text_area.delete("1.0", tk.END)  # Borrar contenido actual del área de texto
        self.current_open_file = ''  # Restablecer el nombre del archivo actual
        self.text_modified = False  # Restablecer el chivato de modificación

    def save_file(self):
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename()  # Cuadro de diálogo para guardar archivo
            if new_file_path:
                self.current_open_file = new_file_path
            else:
                return

        with open(self.current_open_file, 'w') as file:
            file.write(self.text_area.get('1.0', tk.END))  # Guardar contenido del área de texto en el archivo
        self.text_modified = False  # Restablecer chivato de modificación

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")  # Cortar texto seleccionado

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")  # Copiar texto seleccionado

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")  # Pegar texto del portapapeles

    def search_text(self):
        search_query = simpledialog.askstring("Buscar", "Introduzca la palabra o carácter a buscar:")  # Cuadro de diálogo para ingresar texto a buscar
        if not search_query:
            messagebox.showwarning("Buscar", "Debe introducir una palabra o carácter para buscar.")  # Mostrar advertencia si no se ingresa nada
            return

        self.text_area.tag_remove('highlight', '1.0', tk.END)  # Eliminar resaltado anterior
        start_pos = '1.0'
        while True:
            start_pos = self.text_area.search(search_query, start_pos, stopindex=tk.END)  # Buscar texto
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_query)}c"
            self.text_area.tag_add('highlight', start_pos, end_pos)  # Resaltar texto encontrado
            self.text_area.tag_config('highlight', background='yellow', foreground='black')  # Configurar color de resaltado
            start_pos = end_pos

# Crear ventana principal
root = tk.Tk()
root.geometry("700x500")  # Configurar tamaño de la ventana
root.title("Bloc de notas tkinter")  # Configurar título de la ventana

# Crear instancia del editor de texto
editor = SimpleTextEditor(root)

# Crear barra de menú
menu_bar = tk.Menu(root)

# Crear menús
menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_herramientas = tk.Menu(menu_bar, tearoff=0)

# Añadir opciones al menú "Archivo"
menu_opciones.add_command(label="Nuevo", command=editor.new_file)
menu_opciones.add_command(label="Abrir", command=editor.open_file)
menu_opciones.add_command(label="Guardar", command=editor.save_file)
menu_opciones.add_command(label="Salir", command=editor.confirm_quit)

# Añadir opciones al menú "Herramientas"
menu_herramientas.add_command(label="Cortar", command=editor.cut_text)
menu_herramientas.add_command(label="Copiar", command=editor.copy_text)
menu_herramientas.add_command(label="Pegar", command=editor.paste_text)
menu_herramientas.add_command(label="Buscar", command=editor.search_text)

# Añadir menús a la barra de menú
menu_bar.add_cascade(label="Archivo", menu=menu_opciones)
menu_bar.add_cascade(label="Herramientas", menu=menu_herramientas)

# Configurar barra de menú en la ventana principal
root.config(menu=menu_bar)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
