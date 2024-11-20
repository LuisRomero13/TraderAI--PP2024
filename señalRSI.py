def determinarSeñal(valorRSI):
    # Determina la recomendación final de la acción en base al valor que recibe
    if valorRSI > 70:
        señal = "VENTA"
    elif valorRSI < 30:
        señal = "COMPRA"
    else:
        señal = "NEUTRO"    
    return señal