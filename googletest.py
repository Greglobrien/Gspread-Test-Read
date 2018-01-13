import gspread
import datetime

from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("API Test Sheet").sheet1
# list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)

today = '{d.month}/{d.day}/{d.year}'.format(d=datetime.datetime.now())

cell = sheet.find(today)

today_row = sheet.row_values(cell.row)

print today
print("Found something at Row %s" % (cell.row))
print today_row