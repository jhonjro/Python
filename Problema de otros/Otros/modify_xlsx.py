# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:02:02 2021

@author: jhon_
"""

import os
import pandas as pd


ejemplo_dir = 'C:/Users/jhon_/Mi unidad/Scripts/Python/dynamic_light_scattering'
contenido = os.listdir(ejemplo_dir)


for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.xlsx'):
        # Cargamos los datos
        data = pd.read_excel(fichero, header=None, engine='openpyxl')
        print(data)
        data = data.to_numpy()
        x = data[:, 0]

        tabla = pd.DataFrame(x, columns=['x'])
        print(tabla)
        tabla.to_excel('Procesado/Autocorrelation ' + os.path.splitext(fichero)[0] + '.xlsx', sheet_name='Autocorrelation', index=False)
