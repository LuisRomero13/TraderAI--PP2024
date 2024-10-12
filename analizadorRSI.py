from listaAcciones import cargarAcciones


def cargarArchivo(pathExcel = "/home/luisromero13/Documentos/acciones.xlsx"):
    df = cargarAcciones(pathExcel)