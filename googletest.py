#https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
import gspread
import datetime
import re

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
#https://stackoverflow.com/questions/9525944/python-datetime-formatting-without-zero-padding
cell = sheet.find(today)
if cell == "":
    print ("No Show today?")
    # https://stackoverflow.com/questions/73663/terminating-a-python-script
    quit()
#The commented out rows indicate initial tests to find an individual row
#else:
    #today_row = sheet.row_values(cell.row)
    #print today
    #print ("Found something at Row %s" % (cell.row))
    #print today_row

#https://developers.google.com/edu/python/lists
multicam_Trucks = ['killer frost', 'harley quinn', 'poison ivy', 'catwomen']
cell_list = sheet.findall(today)
row_count = 0
for cell in cell_list:
    print ("Found something at Row %s" % (cell.row))
    #today_row = sheet.row_values(cell.row)
    #print today_row
    row_count = row_count + 1
    #https://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
    home_team = sheet.cell (cell.row, 5).value.lower()
    encoder = sheet.cell(cell.row, 11).value.lower()
    #encoder_list = re.split( , encoder)
    #https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python
    print ("-You're using %s at %s today" % (encoder, home_team))
    if any(multicam in encoder for multicam in multicam_Trucks):
       print ("-- %s is a Multicam at %s" % (encoder, home_team))


print ("Cell List")
print cell_list
print ("The Numbers of Rows %s" % (row_count))
