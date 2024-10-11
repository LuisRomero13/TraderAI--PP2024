import yfinance as yf
# validador Yfiance
def verificar_ticker(ticker):
    try:
        # Intenta obtener información del ticker
        datos = yf.Ticker(ticker).info
        # Si no hay excepción, el ticker existe
        return True
    except ValueError:
        # Si ocurre un ValueError, significa que el ticker no existe
        return False
    except Exception as e:
        # Captura cualquier otro tipo de excepción (ej. conexión a internet)
        print(f"Ocurrió un error: {e}")
        return False