from listaAcciones import cargarAcciones
from listaCotizaciones import descargarCotizaciones
from calculadorRSI import calcular_RSI
from señalRSI import determinarSeñal

def cargarArchivo(pathExcel):
    df, mensaje = cargarAcciones(pathExcel)
    return df, mensaje

def señalesRSI(df):
    while df:
        print()

df, mensaje = cargarArchivo("/home/luisromero13/Documentos/acciones.xlsx")