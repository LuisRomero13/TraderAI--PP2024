from listaCotizaciones import descargarCotizaciones
from calculadorRSI import calcular_RSI
from señalRSI import determinarSeñal
from validador import validarFormato
import pandas as pd

def cargarArchivo(pathExcel):
    # funcion para todas las validaciones del archivo recibido
    es_valido, mensaje = validarFormato(pathExcel)
    if es_valido:
        # funcion para leer el excel si pasa la validacion
        df = pd.read_excel(pathExcel, sheet_name='Hoja1')
    else:
        # Crea y devuelve un dataFrame vacio en caso contrario
        df = pd.DataFrame()
    return df, mensaje

def señalesRSI(df):
    # Se agrega una columna para el resultado de la señal consultada
    # Ya lo inicializamos con texto de "no resuelto"
    # En caso de que si se resuelva solo se reemplaza el valor
    df['señal'] = "No se ha podido resolver"
    # Se crea una lista de mensajes de error de cotizaciones
    msj_cotiz = list()
    # Se recorre el Dataframe por filas
    for index, row in df.iterrows():
        # Se guarda el simbolo bursatil de cada accion
        simbolo = row["acciones"]
        # Se descargan las cotizaciones historicas de la accion
        cotizaciones, msj = descargarCotizaciones(simbolo)
        # Si es valido, se calcula su señal y se guarda en el Dataframe cargado
        if msj == "La acción es válida":
            valorRSI = calcular_RSI(cotizaciones)
            señal = determinarSeñal(valorRSI)
            df.at[index, 'señal'] = señal
        else:
            # Se van agregando las acciones por error
            msj_cotiz.append(f"para la accion '{simbolo}': {msj}")
    return df, msj_cotiz