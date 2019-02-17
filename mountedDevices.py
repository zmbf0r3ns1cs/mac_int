# Query Logic for Mounted Devices/Volumes v0.8
# Justin Boncaldo, Zachary Burnham 2019
# ----------------------------------------------------------

import sqlite3
import re

# Specify files here for testing
file = open('//Users//zachburnham//Desktop//Capstone//Mac_apt_Output//exampleWrite.txt', 'w+')
connection = sqlite3.connect('//Users//zachburnham//Desktop//Capstone//Mac_apt_Output//mac_apt02.db')
cursor = connection.cursor()

# Mounted Volume variables
global a, b, output

# Define strings
d = []
e = []
volList = []
crList = []
fsList = []
lsList = []
string1 = "None"

# Define variables
i = "Info"
ri = "RecentItems"
icd = "_kMDItemCreationDate"
sls = "'Spotlight-1-store'"
du = "Date_Updated"
sc = "Session_Commands"
bs = "BashSessions"
n = "Name"

# Define counters
y = 0
x = "first"
end = "no"
counter = 0
output = None

# Username search (may be in main function, TBD)
userSearch = input("What User? (Enter for default All): ")

while end != "yes":
    if counter < 2:
        if counter == 0:
            a = n
            b = ri
        elif counter == 1:
            a = i
            b = ri
        cursor.execute("SELECT {} FROM {} WHERE Type='VOLUME' AND User=?".format(a, b), (userSearch,))
        output = cursor.fetchall()
        d.clear()
        for row in output:
            d.append(str(row[0]))
        pos = 0
        for (row) in output:
            string1 = str(d[pos])
            pos = pos + 1
            if counter == 0:
                volList.append(string1)
                volLength: int = len(volList)
            elif counter == 1:
                crList.append(string1)
                crLength: int = len(crList)
            else:
                continue
        counter = counter + 1
    else:
        while y < volLength:
            if counter == 2:
                a = icd
                b = sls
            elif counter == 3:
                a = du
                b = sls
            else:
                end = "yes"
            cursor.execute("SELECT {} FROM {} WHERE kMDItemKind='Volume' AND kMDItemDisplayName =?".format(a, b), (str(volList[y]),))
            output = cursor.fetchall()
            e.clear()
            for (row) in output:
                e.append(str(row[0]))
            if counter == 2:
                #print(str(counter))
                fsList.append(str(e))
                fsLength: int = len(fsList)
                if y == (volLength - 1):
                    y = 0
                    counter = counter + 1
                else:
                     y = y + 1
                print("fsList " + str(fsList))
            elif counter == 3:
                #print(str(counter))
                lsList.append(str(e))
                lsLength: int = len(lsList)
                print("lsList " + str(lsList))
                if y == (volLength - 1):
                    y = 0
                    counter = counter + 1
                else:
                     y = y + 1
            else:
                print("Done")
                y = (volLength + 1)
                end = "yes"

file.write('\n')
file.close

# Global variables and function call
a = "None"
b = "None"
output = None