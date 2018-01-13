import gspread
import datetime

from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("API Test Sheet").sheet1
#These commented out rows will print EVERYTHING in the sheet
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)
today = '{d.month}/{d.day}/{d.year}'.format(d=datetime.datetime.now())

cell = sheet.find(today)
if cell == "":
    print ("No Show today?")
    quit()
#The commented out rows indicate initial tests to find an individual row, better to test for multiple
#else:
    #today_row = sheet.row_values(cell.row)
    #print today
    #print ("Found something at Row %s" % (cell.row))
    #print today_row

cell_list = sheet.findall(today)
row_count = 0
for cell in cell_list:
    print ("Found something at Row %s" % (cell.row))
    today_row = sheet.row_values(cell.row)
    print today_row
    row_count = row_count + 1



print ("Cell List")
print cell_list
print ("The Numbers of Rows %s" % (row_count))
