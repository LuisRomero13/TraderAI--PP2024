import pandas as pd
import numpy as np
# Función para calcular el RSI
def calcular_RSI(data, period=14):
    delta = data.diff(1)  # Diferencia de precios día a día
    ganancia = np.where(delta > 0, delta, 0)
    perdida = np.where(delta < 0, -delta, 0)
    
    avg_gain = pd.Series(ganancia).rolling(window=period).mean()
    avg_loss = pd.Series(perdida).rolling(window=period).mean()
    
    RS = avg_gain / avg_loss
    RSI = 100 - (100 / (1 + RS))
    
    return RSI