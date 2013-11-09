import gspread
import requests

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
da = 0

"""
Link for editing sheet:
https://docs.google.com/a/hackbrightacademy.com/spreadsheet/ccc?key=0Ahc_9pLanCZudHNOTi1fVVlfX1dRdFZkWHMtSzZwNmc&usp=sharing
"""
# This is for people who don't mind typing their password in clear text
# login with username and password from secret file
"""
gc = gspread.login(secret.GD_LOGIN, secret.GD_PASS)
points_results = gc.open("Fall 2013 House Points (Responses)")
results_ws = points_results.worksheet("Form Responses")
all_points = results_ws.get_all_values()
del all_points[0]
"""

#Trying again without the password
csv_request = requests.get("https://docs.google.com/spreadsheet/ccc?key=0Ahc_9pLanCZudHNOTi1fVVlfX1dRdFZkWHMtSzZwNmc&output=csv")
csv_file = csv_request.content
lines = csv_file.split('\n')
del lines[0]
for row in lines:
    row = row.split(',')

# for row in all_points:
    if row[1] == "Gryffindor":
        gryffindor += int(row[2])
    if row[1] == "Slytherin":
        slytherin += int(row[2])
    if row[1] == "Ravenclaw":
        ravenclaw += int(row[2])
    if row[1] == "Hufflepuff":
        hufflepuff += int(row[2])
    if row[1] == "Dumbledore's Army":
        da += int(row[2])

print "Gryffindor: ", gryffindor
print "Hufflepuff: ", hufflepuff
print "Ravenclaw: ", ravenclaw
print "Slytherin: ", slytherin
print "Dumbledore's Army: ", da