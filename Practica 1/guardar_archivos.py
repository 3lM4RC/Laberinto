#Programa para abrir archivos y guardar el laberinto
import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Crear una ventana principal
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Abrir el cuadro de diálogo para seleccionar un archivo CSV
file_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

if file_path:
    # Leer el contenido del archivo CSV en un DataFrame de Pandas
    try:
        df = pd.read_csv(file_path)
        # Ahora, 'df' contiene los datos del archivo CSV en forma de DataFrame de Pandas
        print("Archivo CSV cargado correctamente en la variable 'df'.")
        print(df)
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {str(e)}")
else:
    print("No se seleccionó ningún archivo CSV.")

# Puedes usar el DataFrame 'df' para trabajar con los datos cargados desde el archivo CSV.
