import pandas as pd
import numpy as np

# Cargar el archivo CSV
file_path = r'C:\Users\oscar\Dropbox\PC\Documents\Teo_AnalizadorSintactico\utils\tablas_ll1\instrucciones.csv'

# Inspeccionar el contenido crudo para entender su estructura
with open(file_path, 'r') as file:
    raw_content = file.readlines()

# Mostrar las primeras líneas (puedes omitir este paso en producción)
# print(raw_content[:10])

# Cargar el archivo utilizando el delimitador ";", omitiendo filas vacías
processed_data = pd.read_csv(file_path, delimiter=';', skip_blank_lines=True, encoding='utf-8')

# Reemplazar encabezados defectuosos y eliminar filas completamente vacías

# print(processed_data)
# processed_data.columns = processed_data.shape[1]
processed_data.dropna(how='all', inplace=True)

# Crear la estructura deseada: tabla[A][B]
tabla_transformada = ""

# # Iterar por las filas para construir la estructura
for _, row in processed_data.iterrows():
    b_key = row[0]  # Columna B (primera columna)

    print("")   
    print("NT."+b_key, ":")   
    print("{")   
    for a_key in processed_data.columns[1:]:  # Ignorar la primera columna
        # if a_key not in tabla_transformada:
            # tabla_transformada[b_key] = {}
        if str(row[a_key]) == "nan": 
            print("'"+a_key+"'"+":", [], ",")
        else:      
            print("'"+a_key+"'"+":", str(row[a_key]).split()[::2], ",")      
    print("},")   
        # tabla_transformada[b_key][a_key] = [row[a_key]]

# Mostrar la estructura final (puedes omitir este paso en producción)
