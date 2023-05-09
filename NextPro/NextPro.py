import requests
from datetime import datetime
import pandas as pd
import json
import time as t


"""
PROBLEMA 1
"""

print('Aquí inicia el problema 1.')

# * Se pide el enlace al cual se le le hará la petición (GET)

# url = input('Ingrese el enlace de la cuál se hará la petición GET\n')

url = 'https://desarrollonextpro-nextconnector-demo07.odoo.com/list_orders'


# * Se corroborará que link sea válido para aplicar la función get de la librería request

headers = {
    'accessToken': 'PXT0PFt45',
    'Content-Type': 'application/json'
}

try:
    get_info = requests.get(url, auth=('user', 'pass'))
except:
    print('Link inválido.')  # ! Devolver este mensaje, si ocurre algún error al aplicar la función GET.
else:
    if get_info.status_code == 200 and get_info:
        # print(get_info.text)  # * Se devuelve la info, si el status code es 200, es decir, obtención de datos exitosa.

        print('Aquí inicia el problema 2.')

        info = get_info.json()

        info = sorted(info, key=lambda g: float(g.get('total', 0)), reverse=True)

        top = []

        for i in info[:10]:
            top.append(i)  # se añade en top los 10 primeros elementos con mayor valor de 'total'.

        orden_venta = list(map(lambda r: r.get('id_orden_venta', 0), top))
        num = list(map(lambda r: r.get('num', ''), top))
        date = list(map(lambda r: r.get('date'), top))
        customer = list(map(lambda r: r.get('customer', ''), top))
        total = list(map(lambda r: r.get('total', 0), top))

        for a, b, c, d, e in zip(orden_venta, num, date, customer, total):
            print(f'{a} ; {b} ; {c} ; {d} ; {e}')

        tabla = pd.DataFrame(list(zip(orden_venta, num, date, customer, total)), columns=['id', 'num', 'date', 'customer', 'total'])

        now = datetime.now()
        date = now.date()
        time = now.time()
        title = 'JHONJAIRO_ROJASORTIZ_' + str(date) + '_' + str(time)
        title = title.replace(':', '-') + '.csv'

        tabla.to_csv(title, sep=';')

        print('Aquí inicia el problema 3.')

        url = 'https://desarrollonextpro-nextconnector-demo07.odoo.com/set_order'

        headers = {
            'accessToken': 'PXT0PFt45',
            'Content-Type': 'application/json'
        }

        # * Por cada elemento del top se hace un POST con la información requerida

        # top = top[:1] + top[2:]

        for index, p in enumerate(top):

            t.sleep(1)

            # print(f"ID: {p.get('id_orden_venta', 0)}")

            body = {
                "id_orden_venta": p.get('id_orden_venta', 0),
                # "num": p.get('num', ''),
                # "date": p.get('date'),
                # "customer": p.get('customer', ''),
                # "total": p.get('total', '0'),
                "candidate_name": "REGISTOR ACTUALIZADO POR JHON JAIRO ROJAS ORTIZ",
                "candidate_sequence": index + 1
            }

            # print(body)

            ok = {
                "jsonrpc": "2.0",
                "id": p.get('id_orden_venta', 0),
                "result": {
                    "state": "ok",
                    "message": ""
                }
            }

            bad = {
                "jsonrpc": "2.0",
                "id": p.get('id_orden_venta', 0),
                "result": {
                    "state": "error",
                    "message": "Jhon Jairo Rojas Ortiz"
                }
            }

            r = requests.post(url, data=json.dumps(body), headers=headers)

            # print('post')

            # * Respuesta de actualización con éxito y respuesta con estado de error

            print(r.text)

            if r.status_code == 200:
                print(json.dumps(ok))
            else:
                print(json.dumps(bad))

    else:
        print(f'STATUS CODE: {get_info.status_code}')
