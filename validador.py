import os
import pandas as pd
# validador de archivo
def validarFormato(ruta_archivo):
    # Verificar que el archivo existe
    if not os.path.exists(ruta_archivo):
        return False, "El archivo no existe."

    # Verificar que el archivo es un .xlsx
    if not ruta_archivo.lower().endswith('.xlsx'):
        return False, "El archivo no es un archivo Excel .xlsx válido."
    
    try:
        # Leer el archivo Excel
        df = pd.read_excel(ruta_archivo, sheet_name='Hoja1')
        
        # Eliminar filas completamente vacías
        df = df.dropna(how='all')
        
        # Contar el número de filas con datos
        num_filas = len(df)
        
        # Verificar que no tenga más de 20 filas
        if num_filas > 20:
            return False, f"El archivo tiene {num_filas} filas, lo cual excede el límite de 20 filas."
        
        return True, "El archivo cumple con todas las validaciones."
    
    except Exception as e:
        return False, f"Error al procesar el archivo: {str(e)}"
    
# validador Yfinance
def verificar_ticker(ticker):
    try:
        # Intenta obtener información del ticker
        datos = ticker.info
        # Busca un atributo clave en comun con las acciones
        if 'shortName' in datos and datos['shortName'] is not None:
            return True, "La acción es válida"
        else:
            return False, f"La acción no existe: {e}"
    except ValueError:
        # Si ocurre un ValueError, significa que el ticker no existe
        return False, f"La acción no existe: {e}"
    except Exception as e:
        # Captura cualquier otro tipo de excepción (ej. conexión a internet)
        return False, f"Ocurrió un error: {e}"