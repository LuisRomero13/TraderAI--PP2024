import yfinance as yf
import pandas as pd
from validador import verificar_ticker

def descargarCotizaciones(simbolo):
    # Crea una instancia del objeto Ticker
    accion = yf.Ticker(simbolo)
    
    #valida el ticker a trabajar
    es_valido, mensaje = verificar_ticker(accion)
    
    if es_valido:
        # Obtiene datos históricos de precios y ordene por fecha actual
        datos_historicos = accion.history(period="1mo")
        return datos_historicos, mensaje
    else:
        # En caso de no verificar la acción se devuelve un DataFrame vacio con su mensaje de error
        df = pd.DataFrame()

        return df, mensaje