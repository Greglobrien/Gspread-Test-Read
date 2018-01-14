#https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
import gspread
import datetime
import re

from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#https://github.com/burnash/gspread
calendar_sheet = client.open("API Calendar Sheet").sheet1
ip_sheet = client.open("API Internet Sheet")
ip_worksheet = ip_sheet.worksheet("Additional")

#These commented out rows will print EVERYTHING in the sheet
#list_of_hashes = ip_worksheet.get_all_records()
#print(list_of_hashes)

#https://stackoverflow.com/questions/9525944/python-datetime-formatting-without-zero-padding
today = '{d.month}/{d.day}/{d.year}'.format(d=datetime.datetime.now())

cell = calendar_sheet.find(today)
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
multicam_trucks = ['killer frost', 'harley quinn', 'poison ivy', 'catwoman']
cell_list = calendar_sheet.findall(today)
row_count = 0
for cell in cell_list:
    print ("Found something at Row %s" % (cell.row))
    #today_row = sheet.row_values(cell.row)
    #print today_row
    row_count = row_count + 1
    #https://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
    home_team = calendar_sheet.cell (cell.row, 5).value.lower()
    encoder = calendar_sheet.cell(cell.row, 11).value.lower()
    #encoder_list = re.split( , encoder)
    #https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python
    print ("-You're using %s at %s today" % (encoder, home_team))
    #https://stackoverflow.com/questions/3271478/check-list-of-words-in-another-string
    #https://stackoverflow.com/questions/19211828/python-using-any-and-all-to-check-if-a-list-contains-one-set-of-values-or-an
    if any(multicam in encoder for multicam in multicam_trucks):
       print ("-- %s is a Multicam at %s" % (encoder, home_team))


ip_multicam_row = ip_worksheet.row_values(1)
print "IP ROW"
print ip_multicam_row
ip_row_count = 0

for item in ip_multicam_row:
    item.find("Harley Quinn")
    ip_row_count = ip_row_count + 1

print ip_row_count

ip_multicam_column = ip_worksheet.col_values(ip_row_count)
print "IP Column"
print ip_multicam_column

#if any("Killer Frost" in s for s in ip_multicam_row):
    #print ("this is the count %s ") % (s)
#   print "I found something"


print ("Cell List")
print cell_list
print ("The number of Rows %s" % (row_count))
