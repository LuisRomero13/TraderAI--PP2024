import tkinter as tk
from tkinter import filedialog, messagebox
from analizadorRSI import cargarArchivo
from analizadorRSI import señalesRSI

acciones = None
# Función para cargar el archivo Excel
def cargar_archivo():
    global acciones
    archivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    acciones, msj = cargarArchivo(archivo)
    if msj == "El archivo cumple con todas las validaciones.":
        messagebox.showinfo("Archivo cargado", f"Has seleccionado: {archivo}")
    else:
       messagebox.showinfo("Error en la validación", msj)

# Función para consultar la señal
def consultar_senal():
    global acciones
    if acciones is not None:
        messagebox.showinfo("Consulta de señal", "Aguarde unos segundos...")
        df_acciones = señalesRSI(acciones)
        messagebox.showinfo("Consulta de señal", "Consulta de señal realizada. \n Ahora seleccione donde desee guardar los resultados")
        archivo_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        # Guardar el DataFrame en un archivo Excel
        df_acciones.to_excel(archivo_guardar, index=False)
        messagebox.showinfo("Consulta de señal", f"El archivo se guardó satisfactoriamente en {archivo_guardar}")
    else:
        messagebox.showwarning("Advertencia", "Primero debes cargar un archivo Excel.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Trader AI: Análisis y Recomendación de Inversiones en Bolsa")

# Botón para cargar archivo Excel
btn_cargar = tk.Button(ventana, text="Cargar archivo Excel", command=cargar_archivo)
btn_cargar.pack(pady=10)

# Botón para consultar señal
btn_consultar = tk.Button(ventana, text="Consultar señal", command=consultar_senal)
btn_consultar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

__name__ = "__main__"
