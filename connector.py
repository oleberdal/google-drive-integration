import gspread
from oauth2client.service_account import ServiceAccountCredentials


def connect(scope, credentials):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)

    return gspread.authorize(credentials)
