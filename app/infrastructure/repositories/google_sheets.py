import os
import json

import gspread
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from app.config import BASE_DIR

SPREADSHEET_ID = "1H2s2gCVdGSeuLiZ-_FLbNg9UdqeuOpJTG2pZ6Tqh62c"
GID = 143167261

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]

print(BASE_DIR)
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.json"

def get_google_credentials():
    credentials = None

    # Якщо вже авторизувалися раніше
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )

    # Якщо token відсутній або протермінований
    if not credentials or not credentials.valid:

        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES
            )

            credentials = flow.run_local_server(port=0)

        # Зберігаємо токен для наступних запусків
        with open(TOKEN_FILE, "w") as token:
            token.write(credentials.to_json())

    return credentials


def get_products():
    credentials = get_google_credentials()

    client = gspread.authorize(credentials)

    spreadsheet = client.open_by_key(SPREADSHEET_ID)

    worksheet = spreadsheet.get_worksheet_by_id(GID)

    products = worksheet.get_all_records()

    print(f"Знайдено товарів: {len(products)}")
    json_data = json.dumps(products, ensure_ascii=False, indent=2)

    print(json_data)
    return products
