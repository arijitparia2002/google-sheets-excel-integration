import os
import pandas as pd
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def authenticate_google():
    """Authenticate and return Google Sheets service."""
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=scopes)
    creds = flow.run_local_server(port=0)
    service = build('sheets', 'v4', credentials=creds)
    return service

def update_google_sheets(service, spreadsheet_id, excel_folder):
    """Read Excel files and update Google Sheets."""
    for filename in os.listdir(excel_folder):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(excel_folder, filename)
            df = pd.read_excel(file_path)

            # Create a new sheet with the name of the Excel file
            sheet_name = filename.replace('.xlsx', '')
            body = {
                'requests': [{
                    'addSheet': {
                        'properties': {
                            'title': sheet_name
                        }
                    }
                }]
            }
            service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body=body
            ).execute()

            # Prepare range and value_input_option
            range_name = f"{sheet_name}!A1"
            value_input_option = 'RAW'
            values = [df.columns.values.tolist()] + df.values.tolist()
            body = {
                'values': values
            }
            service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body
            ).execute()

def main():
    service = authenticate_google()
    spreadsheet_id = input("Enter the Google Spreadsheet ID: ")
    excel_folder = 'excel_files'
    update_google_sheets(service, spreadsheet_id, excel_folder)

if __name__ == '__main__':
    main()
