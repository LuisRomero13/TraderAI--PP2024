def determinarSeñal(valorRSI):
    if valorRSI > 70:
        señal = "VENTA"
    elif valorRSI < 30:
        señal = "COMPRA"
    else:
        señal = "NEUTRO"    
    return señal