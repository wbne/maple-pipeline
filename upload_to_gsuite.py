import os.path
import os
import csv
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def upload_csv(sheet):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    ######### GETTING CREDENTIALS ########

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        ######## GETTING SPREADSHEET ID ########

        time = datetime.now().strftime("%H:%M")
        today = datetime.today()
        date = today.strftime('%b-%d-%Y')
        sheet_name = date + " " + time

        if os.path.exists("spreadsheet_id.txt"):
            with open("spreadsheet_id.txt", 'r') as file:
                spreadsheet_id = file.readline()
            if(sheet == None):
                body = {
                    "requests":{
                        "addSheet":{
                            "properties":{
                                "title": sheet_name
                            }
                        }
                    }
                }
                service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        else:
            sheet = service.spreadsheets()
            spreadsheet = {
                "properties": {"title": "Maple Pipeline Data"},
                "sheets": [
                    {"properties":{"title": sheet_name}}
                ]
            }
            result = (
                sheet
                .create(body=spreadsheet, fields="spreadsheetId")
                .execute()
            )
            spreadsheet_id = result.get('spreadsheetId')
            with open("spreadsheet_id.txt", "w") as file:
                file.write(spreadsheet_id)

        ######## UPLOADING TO GOOGLE SHEETS ########
        with open('data.csv', newline='') as f:
            reader = csv.reader(f)
            values = list(reader)
        if(sheet != None):
            sheet_name = sheet
        response = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, valueInputOption='USER_ENTERED', range=sheet_name, body={"values": values}).execute()
        print(response)

        print("-------- UPLOADED CSV TO GOOGLE SHEETS --------")
    except HttpError as err:
        print(err)