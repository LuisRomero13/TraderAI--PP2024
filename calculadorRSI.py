import pandas as pd
import numpy as np

# Función para calcular el RSI
def calcular_RSI(data, columna='Close', periodo=14):
    """
    Calcula el RSI para un DataFrame dado.
    
    :param df: DataFrame de pandas con datos de precios
    :param periodo: El período para calcular el RSI (por defecto 14)
    :param columna: El nombre de la columna con los precios (por defecto 'Close')
    :return: Una serie de pandas con los valores del RSI
    """
    
    # Calcular los cambios diarios
    delta = data[columna].diff()
    
    # Separar los cambios positivos (ganancias) y negativos (pérdidas)
    ganancia = np.where(delta > 0, delta, 0)
    perdida = np.where(delta < 0, -delta, 0)
    
    # Calcular el promedio de ganancias y pérdidas
    avg_gain = pd.Series(ganancia).rolling(window=(periodo)).mean()
    avg_loss = pd.Series(perdida).rolling(window=(periodo)).mean()
    
    # Calcular el RS (Relative Strength)
    RS = avg_gain / avg_loss

    if RS.last_valid_index():
        # Calcular el RSI
        RSI = 100 - (100 / (1 + RS))
        # Devolver sólo el valor que le corresponde al periodo descrito anteriormente
        return RSI[RSI.last_valid_index()]
    # En caso contrario 
    return pd.DataFrame()