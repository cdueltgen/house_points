import gdata
import gspread
import secret

# login with username and password from secret file
gc = gspread.login(secret.GD_LOGIN, secret.GD_PASS)
points_results = gc.open("Fall 2013 House Points (Responses)")

results_ws = points_results.worksheet("Form Responses")

all_points = results_ws.get_all_values()

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
da = 0

del all_points[0]
for row in all_points:
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