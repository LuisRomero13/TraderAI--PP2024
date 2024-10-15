import pandas as pd
from validador import validarFormato

def cargarAcciones(path):
    es_valido, mensaje = validarFormato(path)
    if es_valido:
        df = pd.read_excel(path, sheet_name='Hoja1')
    else:
        print("Error en la validación:", mensaje)
    return df, mensaje  