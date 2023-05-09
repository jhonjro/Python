# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:02:02 2021

@author: jhon_
"""

import os
import pandas as pd
import numpy as np


ejemplo_dir = 'C:/Users/jhon_/Mi unidad/Scripts/Python/dynamic_light_scattering/Anka'
contenido = os.listdir(ejemplo_dir)


for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.xlsx'):

        fich = os.path.join(ejemplo_dir, fichero)
        print(fichero)

        xlsx = pd.ExcelFile(fich)
        sheet_names = xlsx.sheet_names

        name_new = ejemplo_dir + '/Procesado/template_format_' + os.path.splitext(fichero)[0] + '.xlsx'
        fichero_new = pd.ExcelWriter(name_new, engine='openpyxl')

        for sheet_name in sheet_names:

            data = pd.read_excel(fich, header=0,  sheet_name=sheet_name)
            z = data['SERIE'].fillna('')
            data = data.to_numpy()
            x = data[:, 0]
            length = len(x)
            k = sheet_name
            code = np.full(length, k)
            y = data[:, 1]
            # z = data[:, 2]
            print(z)
            z = np.array([str(i) for i in z if i != ''])
            z = list(z)
            if not z:
                z = np.full(length, '')

            sheet_name = str(k)  # x[0].split(': ')[1]  # + '-' + sheet_name

            # length = len(x) - 2
            # item = np.arange(length) + 1
            # code = np.full(length, sheet_name)
            # product = np.full(length, x[1])
            # serie = x[2:]

            # if serie[0] == 'SIN SERIE':
            #     serie = np.full(length, '')

            # tabla = pd.DataFrame(list(zip(item, code, product, serie)), columns=['ITEM', 'CODE', 'PRODUCT', 'SERIE'])
            tabla = pd.DataFrame(list(zip(x, code, y, z)), columns=['ITEM', 'CODE', 'PRODUCT', 'SERIE'])

            tabla.to_excel(fichero_new, sheet_name=sheet_name, index=False)
        print('FINISH')
        fichero_new.save()
