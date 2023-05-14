from googleapiclient.discovery import build
from google.oauth2 import service_account
import gspread
import pandas as pd
from datetime import datetime, timedelta
from pytz import timezone
import requests
from icecream import ic
import os
from pathlib import Path


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
path = "key/service_account.json"
spreadsheet_id = "1vB9JB_vxYKKuRlRQr1CckKdx7MhlVcFDgBPigEF50oY"

key = Path(os.path.realpath(__file__)).parent / path
ic(key)


creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)
service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()
LIM = timezone("America/Lima")
url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

today = datetime.now().astimezone(LIM)
execute_hour = 6
ic(today)
params = {"fecha": today.strftime("%Y-%m-%d")}

r = requests.get(url, params)
tc_compra = r.json().get("compra")
tc_venta = r.json().get("venta")
ic(tc_compra, tc_venta)

sa = gspread.service_account(key)
sh = sa.open("Contabilidad personal")
wks = sh.worksheet("Response")


def formatFloat(obj):
    if isinstance(obj, float):
        return "{:,.2f}".format(obj)
    return repr(obj)


ic.configureOutput(argToStringFunction=formatFloat)


def get_values_sheet(range):
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range).execute()
    values = data.get("values", [])
    return values


def get_final_date_index():
    range = "Response!A:A"
    arr_date = get_values_sheet(range)

    if arr_date:
        date = arr_date[-1]
        final_date = (
            date[0]
            if isinstance(date, list)
            and date
            and isinstance(date[0], str)
            and date[0] != "Fecha"
            else None
        )
        columns_numbers = len(arr_date)
        ic(final_date, columns_numbers)
        return final_date, columns_numbers
    return None, None


final_date, index = get_final_date_index()


def lambda_handler(event=None, context=None, correction_exchange_rate=False):
    ranges = [
        "Deudores (Personas)!A:B",
        "Debo (Personas)!A:B",
        "Empresas (soles)!A:B",
        "Empresas (dólares)!A:B",
        "Cuentas bancarias (soles)!A:B",
        "Cuentas bancarias (dólares)!A:B",
        "Consumo TC (soles)!A:B",
        "Consumo TC (dólares)!A:B",
        "Metas (soles)!A:B",
        "Metas (dólares)!A:B",
    ]
    (
        deudores,
        debo,
        empresas_soles,
        empresas_dolares,
        cuentas_bancaria_soles,
        cuentas_bancaria_dolares,
        consumo_tc_soles,
        consumo_tc_dolares,
        meta_soles,
        meta_dolares,
    ) = [get_values_sheet(x) for x in ranges]
    montos = [
        deudores,
        debo,
        empresas_soles,
        empresas_dolares,
        cuentas_bancaria_soles,
        cuentas_bancaria_dolares,
        consumo_tc_soles,
        consumo_tc_dolares,
        meta_soles,
        meta_dolares,
    ]

    (
        monto_deudores_soles,
        monto_debo,
        monto_empresas_soles,
        monto_empresas_dolares,
        monto_cuentas_bancaria_soles,
        monto_cuentas_bancaria_dolares,
        monto_consumo_tc_soles,
        monto_consumo_tc_dolares,
        monto_metas_soles,
        monto_meta_dolares,
    ) = [get_total(x) for x in montos]

    process_data(
        correction_exchange_rate,
        monto_deudores_soles,
        monto_debo,
        monto_empresas_soles,
        monto_empresas_dolares,
        monto_cuentas_bancaria_soles,
        monto_cuentas_bancaria_dolares,
        monto_consumo_tc_soles,
        monto_consumo_tc_dolares,
        monto_metas_soles,
        monto_meta_dolares,
    )

    return True


def process_data(
    correction_exchange_rate,
    monto_deudores_soles,
    monto_debo,
    monto_empresas_soles,
    monto_empresas_dolares,
    monto_cuentas_bancaria_soles,
    monto_cuentas_bancaria_dolares,
    monto_consumo_tc_soles,
    monto_consumo_tc_dolares,
    monto_metas_soles,
    monto_meta_dolares,
):
    arr = [
        monto_deudores_soles + monto_empresas_soles,
        monto_empresas_dolares,
        monto_cuentas_bancaria_soles,
        monto_cuentas_bancaria_dolares,
        monto_deudores_soles + monto_empresas_soles + monto_cuentas_bancaria_soles,
        monto_empresas_dolares + monto_cuentas_bancaria_dolares,
        monto_consumo_tc_soles + monto_debo,
        monto_consumo_tc_dolares,
        monto_deudores_soles
        + monto_empresas_soles
        + monto_cuentas_bancaria_soles
        - (monto_consumo_tc_soles + monto_debo),
        monto_empresas_dolares
        + monto_cuentas_bancaria_dolares
        - monto_consumo_tc_dolares,
    ]
    # * Soles
    me_deben = (
        monto_deudores_soles + monto_empresas_soles + tc_compra * monto_empresas_dolares
    )

    en_cuenta = (
        monto_cuentas_bancaria_dolares * tc_compra + monto_cuentas_bancaria_soles
    )
    total_positivo = en_cuenta + me_deben
    total_negativo = (
        monto_consumo_tc_soles + monto_consumo_tc_dolares * tc_compra + monto_debo
    )
    patrimonio = total_positivo - total_negativo
    monto_metas = monto_metas_soles + tc_compra * monto_meta_dolares
    falta_meta = monto_metas - patrimonio if monto_metas else 0

    data_soles = [
        me_deben,
        en_cuenta,
        total_positivo,
        total_negativo,
        patrimonio,
        monto_metas,
        falta_meta,
    ]
    ic(
        me_deben,
        en_cuenta,
        total_positivo,
        total_negativo,
        patrimonio,
        monto_metas,
        falta_meta,
    )

    # * Dólares
    me_deben = (
        monto_deudores_soles + monto_empresas_soles
    ) / tc_venta + monto_empresas_dolares

    en_cuenta = monto_cuentas_bancaria_dolares + monto_cuentas_bancaria_soles / tc_venta
    total_positivo = en_cuenta + me_deben
    total_negativo = (
        monto_consumo_tc_soles + monto_debo
    ) / tc_venta + monto_consumo_tc_dolares
    patrimonio = total_positivo - total_negativo
    monto_metas = monto_metas_soles / tc_venta + monto_meta_dolares
    falta_meta = monto_metas - patrimonio if monto_metas else 0

    data_dolares = [
        me_deben,
        en_cuenta,
        total_positivo,
        total_negativo,
        patrimonio,
        monto_metas,
        falta_meta,
    ]
    ic(
        me_deben,
        en_cuenta,
        total_positivo,
        total_negativo,
        patrimonio,
        monto_metas,
        falta_meta,
    )
    global today
    ic(today)
    ic(today.hour, today.minute)
    if not correction_exchange_rate:
        days = 1 if (today.hour * 60 + today.minute > execute_hour * 60 + 5) else 0
    else:
        days = 0
    today = (today + timedelta(days=days)).strftime("%d/%m/%Y")
    ic(today)
    data_format = (
        [today]
        + [x for x in data_soles]
        + [tc_compra, tc_venta]
        + [(x) for x in data_dolares]
        + arr
    )

    if (
        today == final_date and index and index > 2
    ):  # * 2 unidades para omitir en caso se trate de la cabecera
        ic(index)
        wks.delete_rows(index)
    update_values_sheets("Response!A:AA", [data_format])


def update_values_sheets(range, values):
    sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="USER_ENTERED",
        body={"values": values},
    ).execute()


def get_total(array_of_arrays):
    df = pd.DataFrame(array_of_arrays, columns=["Nombre", "Monto"])
    total = df["Monto"].apply(convert_currency).sum()
    return total


def convert_currency(val):
    new_val = val.replace(",", "").replace("$", "")
    return float(new_val)


if __name__ == "__main__":
    lambda_handler()
