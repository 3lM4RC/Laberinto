import tkinter as tk
from tkinter import filedialog
import ast

# Crear una ventana principal
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Abrir el cuadro de diálogo para seleccionar un archivo TXT
file_path = filedialog.askopenfilename(filetypes=[("Archivos TXT", "*.txt")])

if file_path:
    # Leer el contenido del archivo TXT y eliminar comas y paréntesis
    with open(file_path, 'r') as file:
        text = file.read()

    # Convertir el texto en una lista anidada de Python utilizando ast.literal_eval
    try:
        matrix = ast.literal_eval(text)
        # Ahora, 'matrix' contiene la matriz bidimensional de Python
        print("Matriz cargada correctamente en la variable 'matrix'.")
        print(matrix, type(matrix))
    except Exception as e:
        print(f"Error al cargar la matriz: {str(e)}")
else:
    print("No se seleccionó ningún archivo TXT.")
