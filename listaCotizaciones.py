import yfinance as yf
import pandas as pd
from validador import verificar_ticker
from datetime import datetime, timedelta

def descargarCotizaciones(simbolo):
    # Crea una instancia del objeto Ticker
    accion = yf.Ticker(simbolo)
    
    #valida el ticker a trabajar
    es_valido, mensaje = verificar_ticker(accion)
    
    if es_valido:
        # Calcula la fecha actual y la fecha de 2 semanas atrás   
        fecha_fin = datetime.now().strftime("%Y-%m-%d")
        fecha_inicio = (datetime.now() - timedelta(days=15)).strftime("%Y-%m-%d")
        
        # Obtiene datos históricos de precios
        datos_historicos = accion.history(start=fecha_inicio, end=fecha_fin)
        
        return datos_historicos, mensaje
    else:
        # En caso de no verificar la acción se devuelve un DataFrame vacio con su mensaje de error
        df = pd.DataFrame()
        
        return df, mensaje