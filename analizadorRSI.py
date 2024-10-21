from listaCotizaciones import descargarCotizaciones
from calculadorRSI import calcular_RSI
from señalRSI import determinarSeñal
from validador import validarFormato
import pandas as pd

def cargarArchivo(pathExcel):
    es_valido, mensaje = validarFormato(pathExcel)
    if es_valido:
        df = pd.read_excel(pathExcel, sheet_name='Hoja1')
    else:
        df = pd.DataFrame()
    return df, mensaje

def señalesRSI(df):
    df['señal'] = None
    for index, row in df.iterrows():
        simbolo = row["acciones"]
        cotizaciones, msj = descargarCotizaciones(simbolo)
        if msj == "La acción es válida":
            valorRSI = calcular_RSI(cotizaciones)
            señal = determinarSeñal(valorRSI)
            df.at[index, 'señal'] = señal
    return df