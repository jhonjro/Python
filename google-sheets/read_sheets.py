from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import json

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
key = "Google\ordinal-rig-386013-f4be285ee861.json"
spreadsheet_id = "1vB9JB_vxYKKuRlRQr1CckKdx7MhlVcFDgBPigEF50oY"
creds = None
creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)
service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()
deudores = (
    sheet.values()
    .get(spreadsheetId=spreadsheet_id, range="Deudores (Personas)!B:B")  # A1:A8
    .execute()
)
values = deudores.get("values", [])
print(values)