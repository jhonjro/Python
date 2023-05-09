from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
from datetime import date
import json

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
key = "data/google-sheets\data\ordinal-rig-386013-f4be285ee861.json"
spreadsheet_id = "1vB9JB_vxYKKuRlRQr1CckKdx7MhlVcFDgBPigEF50oY"
creds = None
creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)
service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()
tc = 3.76


def lambda_handler(event=None, context=None):
    ranges = [
        "Deudores (Personas)!A:B",
        "Debo (Personas)!A:B",
        "Empresas (soles)!A:B",
        "Empresas (dólares)!A:B",
        "Cuentas bancarias (soles)!A:B",
        "Cuentas bancarias (dólares)!A:B",
        "Consumo TC!A:B",
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
        consumo_tc,
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
        consumo_tc,
        meta_soles,
        meta_dolares,
    ]

    (
        monto_deudores,
        monto_debo,
        monto_empresas_soles,
        monto_empresas_dolares,
        monto_cuentas_bancaria_soles,
        monto_cuentas_bancaria_dolares,
        monto_consumo_tc,
        monto_metas_soles,
        monto_meta_dolares,
    ) = [get_total(x) for x in montos]
    process_data(
        monto_deudores,
        monto_debo,
        monto_empresas_soles,
        monto_empresas_dolares,
        monto_cuentas_bancaria_soles,
        monto_cuentas_bancaria_dolares,
        monto_consumo_tc,
        monto_metas_soles,
        monto_meta_dolares,
    )
    return {"statusCode": 200, "body": json.dumps("Success!")}


def process_data(
    monto_deudores,
    monto_debo,
    monto_empresas_soles,
    monto_empresas_dolares,
    monto_cuentas_bancaria_soles,
    monto_cuentas_bancaria_dolares,
    monto_consumo_tc,
    monto_metas_soles,
    monto_meta_dolares,
):
    today = date.today().strftime("%d/%m/%Y")
    me_deben = monto_deudores + monto_empresas_soles + tc * monto_empresas_dolares
    en_cuenta = monto_cuentas_bancaria_dolares * tc + monto_cuentas_bancaria_soles
    total_positivo = en_cuenta + me_deben
    total_negativo = monto_consumo_tc + monto_debo
    patrimonio = total_positivo - total_negativo
    monto_metas = monto_metas_soles + tc * monto_meta_dolares
    falta_meta = monto_metas - patrimonio if monto_metas else 0
    data = [
        me_deben,
        en_cuenta,
        total_positivo,
        total_negativo,
        patrimonio,
        monto_metas,
        falta_meta,
    ]
    print(data)
    data_format = (
        [today]
        + [x for x in data]
        + [(x / tc) for x in data]
        # + [" S/ " + "{:,.2f}".format(x) for x in data]
        # + ["$ " + "{:,.2f}".format(x / tc) for x in data]
    )
    update_values_sheets("Response!A:Q", [data_format])


def get_values_sheet(range):
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=range).execute()
    values = data.get("values", [])
    return values


def update_values_sheets(range, values):
    sheet.values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="USER_ENTERED",
        body={"values": values},
    ).execute()


def get_total(array_of_arrays):
    df = pd.DataFrame(array_of_arrays, columns=["Nombre", "Monto"])
    total = df["Monto"].astype("float64").sum()
    return total


lambda_handler()
