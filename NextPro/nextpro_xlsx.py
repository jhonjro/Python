# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 18:02:02 2021

@author: jhon_
"""

import os
import pandas as pd

# import numpy as np


ejemplo_dir = "C:/Users/jhon_/Downloads/NextPro"
contenido = os.listdir(ejemplo_dir)

fields = ""


for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith(".xlsx"):
        fich = os.path.join(ejemplo_dir, fichero)
        print(fichero)

        xlsx = pd.ExcelFile(fich)
        sheet_names = ["Mapeo"]  # xlsx.sheet_names
        for sheet_name in sheet_names:
            data = pd.read_excel(fich, header=0, sheet_name=sheet_name)
            data = data.to_numpy()
            x = data[25:106, 5]
            y = data[25:106, 6]

            lenght = len(x)
            # print(lenght)

            for index in range(lenght):
                # fields += f"{x[index].lower()} = fields.Char(string='{y[index]}')\n"
                fields += f"<field name='{x[index].lower()}'/>\n"

print(fields)
# print(lenght == z)
#
