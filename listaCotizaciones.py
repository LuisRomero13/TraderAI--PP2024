import yfinance as yf

# validador Yfinance
def verificar_ticker(ticker):
    try:
        # Intenta obtener información del ticker
        datos = yf.Ticker(ticker).info
        # Si no hay excepción, el ticker existe
        return True
    except ValueError:
        # Si ocurre un ValueError, significa que el ticker no existe
        print(f"La acción no existe: {e}")
        return False
    except Exception as e:
        # Captura cualquier otro tipo de excepción (ej. conexión a internet)
        print(f"Ocurrió un error: {e}")
        return False

def descargarCotizaciones(simbolo):
    # Crea una instancia del objeto Ticker
    accion = yf.Ticker(simbolo)
    #valida el ticker a trabajar
    verificar_ticker(accion)
    # Obtén datos históricos de precios
    datos_historicos = accion.history(period="1mo") # "1d"=1 dia,"1mo"=1 mes, "1y"=1 año
    print("Datos históricos de precios:", datos_historicos)