import pandas as pd

def cargarAcciones(path):
    """
    docstring
    """
    pass
    df = pd.read_excel(path, sheet_name='Hoja1')
    print(df)
    