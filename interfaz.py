import tkinter as tk
from tkinter import filedialog, messagebox
from analizadorRSI import cargarArchivo
from analizadorRSI import señalesRSI
# Variable global para el DataFrame resultante
acciones = None
# Función para cargar el archivo Excel
def cargar_archivo():
    global acciones
    # Preguntar por el archivo a abrir
    archivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    # llamar a la funcion donde se realiza la lógica de carga en un dataFrame con sus validaciones
    acciones, msj = cargarArchivo(archivo)
    if msj == "El archivo cumple con todas las validaciones.":
        messagebox.showinfo("Archivo cargado", f"Has seleccionado: {archivo}")
    else:
       messagebox.showwarning("Error en la validación", msj)

# Función para consultar la señal
def consultar_senal():
    # llama a la variable global
    global acciones
    if acciones is not None:
        messagebox.showinfo("Consulta de señal", "Pulse 'aceptar' para realizar la consulta de señal RSI")
        # Llamar a la funcion que realiza toda la lógica del cálculo RSI
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
# Titulo de la ventana
ventana.title("Trader AI: Análisis y Recomendación de Inversiones en Bolsa")
# La ventana no se puede redimensionar
ventana.resizable(0,0)
# Características del frame
frame = tk.Frame(ventana, borderwidth=2, relief="solid", padx=10, pady=10, width=640, height=280)
# Enlazar el frame con la ventana
frame.pack()
# Texto introductorio
tk.Label(frame, text= "Bienvenidos a TRADER AI. Un software encargado de recomendarte qué acción debes comprar, vender o esperar en base a análisis técnico de inversiones. Actualmente utiliza el método RSI", width=77, height=5, borderwidth=1, justify="left", wraplength=600).place(x=0, y= 0)
# Texto explicando el uso del primer boton
tk.Label(frame, text= "Como primer paso, debe cargar una lista de no mas de 15 acciones en formato excel pulsando aqui:", width=30, borderwidth=1, wraplength=250).place(x=40, y= 100)
# Texto explicando el uso del segundo boton
tk.Label(frame, text= "Una vez cargado, pulse aqui para analizar las acciones", width=30, height=5, borderwidth=1, justify="left", wraplength=200).place(x=40, y= 150)
# Botón para cargar archivo Excel
btn_cargar = tk.Button(frame, text="Cargar archivo Excel", command=cargar_archivo).place(x=300,y=100)
# Botón para consultar señal
btn_consultar = tk.Button(frame, text="Consultar señal", command=consultar_senal).place(x=300, y=180)

# Ejecutar la aplicación
ventana.mainloop()

__name__ = "__main__"
