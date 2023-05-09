# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:35:16 2021

@author: jhon_
"""

import os
import pandas as pd

ejemplo_dir = 'C:/Users/jhon_/Mi unidad/Scripts/Python/dynamic_light_scattering/Anka'
contenido = os.listdir(ejemplo_dir)


for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.xlsx'):

        fich = os.path.join(ejemplo_dir, fichero)
        print(fichero)

        xlsx = pd.ExcelFile(fich)
        sheet_names = xlsx.sheet_names

        name_new = ejemplo_dir + '/Procesado/template_format_' + \
            os.path.splitext(fichero)[0] + '.xlsx'
        fichero_new = pd.ExcelWriter(name_new, engine='openpyxl')

        for sheet_name in sheet_names:

            data = pd.read_excel(fich, header=0,  sheet_name=sheet_name)
            # print(data)
            data = data.to_numpy()
            # print(data)
            products = data[:, 0]
            print(products)
            codes = data[:, 4]
            lenght = len(products)

            for i in range(lenght):
                sheet_name = str(codes[i])
                x = [1]
                code = [codes[i]]
                y = [products[i]]
                z = ['']

                tabla = pd.DataFrame(list(zip(x, code, y, z)), columns=[
                                     'ITEM', 'CODE', 'PRODUCT', 'SERIE'])
                tabla.to_excel(fichero_new, sheet_name=sheet_name, index=False)
        fichero_new.save()
