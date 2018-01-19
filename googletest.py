# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
import gspread
import datetime

from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import CellNotFound


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# https://github.com/burnash/gspread
calendar_sheet = client.open("API Calendar Sheet").sheet1
ip_sheet = client.open("API Internet Sheet")
ip_worksheet = ip_sheet.worksheet("Additional")

# These commented out rows will print EVERYTHING in the sheet
# list_of_hashes = ip_worksheet.get_all_records()
# print(list_of_hashes)

# https://stackoverflow.com/questions/9525944/python-datetime-formatting-without-zero-padding
# Turn off for testing
# today = '{d.month}/{d.day}/{d.year}'.format(d=datetime.datetime.now())
today = "1/14/2018"

# https://github.com/burnash/gspread/issues/216
try:
    cell = calendar_sheet.find(today)
except CellNotFound:
    print ("It seems there are no shows today")
    # https://stackoverflow.com/questions/73663/terminating-a-python-script
    quit()

# The commented out rows indicate initial tests to find an individual row
# else:
# today_row = sheet.row_values(cell.row)
# print today
# print ("Found something at Row %s" % (cell.row))
# print today_row

# https://developers.google.com/edu/python/lists
multicam_trucks = ['killer frost', 'harley quinn', 'poison ivy', 'catwoman']
Todays_Multicam_list = []
Todays_Hometeam_list = []
cell_list = calendar_sheet.findall(today)
row_count = 0
for cell in cell_list:
    print ("Found something at Row %s" % (cell.row))
    # today_row = sheet.row_values(cell.row)
    # print today_row
    # row_count = row_count + 1
    # https://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
    home_team = calendar_sheet.cell(cell.row, 5).value.lower()
    raw_encoder = calendar_sheet.cell(cell.row, 11).value.lower()
    # encoder_list = re.split( , encoder)
    # https://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python
    print ("-You're using %s at %s today" % (raw_encoder, home_team))

    # https://stackoverflow.com/questions/3271478/check-list-of-words-in-another-string
    # https://stackoverflow.com/questions/19211828/python-using-any-and-all-to-check-if-a-list-contains-one-set-of-values-or-an
    # if any(multicam in raw_encoder for multicam in multicam_trucks):
    #  print ("-- %s is a Multicam at %s" % (raw_encoder, home_team))

    # ^^^ Used any to come up with splitting task to get multicam variable out
    for multicam in multicam_trucks:
        # print "in the loop"
        if multicam in raw_encoder:
            print "(For Multicam) found %s at %s" % (multicam, home_team)
            Todays_Multicam_list.append(multicam)
            Todays_Hometeam_list.append(home_team)
            # Current_Multicam = multicam
            # current_Home_Team = home_team



# For Testing Purposes
# print ("Cell List")
# print cell_list
# print ("The number of Rows %s" % (row_count))

ip_multicam_name_row = ip_worksheet.row_values(1)
ip_schools_column = ip_worksheet.col_values(1)

# https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
for index, Current_Multicam in enumerate(Todays_Multicam_list):

    print "---- the Current Multicam is: %s" % Current_Multicam
    ip_column_count = 0
    # print "IP Column %s" % ip_schools_column
    for cell in ip_schools_column:
        # print ("Currently %s at %s" % (current_Home_Team, cell))
        ip_column_count = ip_column_count + 1
        if Todays_Hometeam_list[index] in cell.lower():
            print ("----- Home Team FOUND %s at %s and Cell %s -----" % (Todays_Hometeam_list[index], ip_column_count, cell))
            current_School_number = ip_column_count


    # ip_multicam_current_address = ip.worksheet.row_values()
    # print "IP ROW"
    # print ip_multicam_name_row
    ip_row_count = 0
    # current_multicam_ip_count = 0
    # https://stackoverflow.com/questions/2972212/creating-an-empty-list-in-python
    ip_List = []

    for cell in ip_multicam_name_row:
        ip_row_count = ip_row_count + 1
        # print ("Currently %s at %s" % (Current_Multicam, cell))
        if Current_Multicam in cell.lower():
            # print ("FOUND Current Multicam %s at %s" % (Current_Multicam, ip_row_count))
            # ip_multicam_count = ip_multicam_count + 1
            current_cell = ip_worksheet.cell(current_School_number, ip_row_count)
            # print ("The Current Cell Value is: %s " % (current_cell))
            # https://stackoverflow.com/questions/12894795/appending-list-but-error-nonetype-object-has-no-attribute-append
            ip_List.append(current_cell.value)
            # current_multicam_ip_count = current_multicam_ip_count + 1
    print "Current Multicam IP Addresses"
    print (ip_List)


    # print ip_row_count
    # ip_multicam_column = ip_worksheet.col_values(ip_row_count)

    # print "IP Column"
    # print ip_multicam_column

    # if any("Killer Frost" in s for s in ip_multicam_row):
    # print ("this is the count %s ") % (s)
    #   print "I found something"
