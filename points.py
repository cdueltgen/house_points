import gspread
import requests

points = { "Gryffindor": 0,
        "Ravenclaw": 0,
        "Hufflepuff": 0,
        "Slytherin": 0,
        "Dumbledore's Army": 0 }

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
    points[row[1]] += int(row[2])

print "Gryffindor: ", points["Gryffindor"]
print "Hufflepuff: ", points["Hufflepuff"]
print "Ravenclaw: ", points["Ravenclaw"]
print "Slytherin: ", points["Slytherin"]
print "Dumbledore's Army: ", points["Dumbledore's Army"]