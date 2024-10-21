import pandas as pd
import numpy as np

# Función para calcular el RSI
def calcular_RSI(data, columna='Close'):
    """
    Calcula el RSI para un DataFrame dado.
    
    :param df: DataFrame de pandas con datos de precios
    :param periodo: El período para calcular el RSI (por defecto 14)
    :param columna: El nombre de la columna con los precios (por defecto 'Close')
    :return: Una serie de pandas con los valores del RSI
    """
    # Asegurarse de que el DataFrame está ordenado por fecha
    df = data.sort_index(ascending = False)
    
    # Calcular los cambios diarios
    delta = df[columna].diff()
    
    # Separar los cambios positivos (ganancias) y negativos (pérdidas)
    ganancia = np.where(delta > 0, delta, 0)
    perdida = np.where(delta < 0, -delta, 0)
    
    # Calcular el promedio de ganancias y pérdidas
    avg_gain = pd.Series(ganancia).rolling(window=(len(df))).mean()
    avg_loss = pd.Series(perdida).rolling(window=(len(df))).mean()
    
    # Calcular el RS (Relative Strength)
    RS = avg_gain / avg_loss
    
    # Calcular el RSI
    RSI = 100 - (100 / (1 + RS))
    
    return RSI[RSI.last_valid_index()]