# Query Logic for Mounted Devices/Volumes v0.9
# Justin Boncaldo, Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re

# Specify files here for testing
file = open('C:\\Users\\burnh\\Desktop\\Capstone\\Mac_apt_Output\\exampleWrite.txt', 'w+')
connection = sqlite3.connect('C:\\Users\\burnh\\Desktop\\Capstone\\Mac_apt_Output\\mac_apt02.db')
cursor = connection.cursor()

# Mounted Volume variables
global a, b, output

# Define strings
d = []
e = []
f = []
mount_volList = []
mount_crList = []
mount_fsList = []
mount_lsList = []
mount_bashList = []
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
L = 0
x = "first"
end = "no"
counter = 0
output = None

# Username search (may be in main function, TBD)
userSearch = input("What User? (Enter for default All): ")
print("Starting Mounted Volume Parsing for " + str(userSearch) + "...")

while end != "yes":
    if (counter == 0) or (counter == 1):
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
                mount_volList.append(string1)
                volLength: int = len(mount_volList)
            elif counter == 1:
                mount_crList.append(string1)
                crLength: int = len(mount_crList)
            else:
                continue
        counter = counter + 1
    elif (counter == 2) or (counter == 3):
        while y < volLength:
            if counter == 2:
                a = icd
                b = sls
            elif counter == 3:
                a = du
                b = sls
            else:
                counter = counter + 1

            cursor.execute("SELECT {} FROM {} WHERE kMDItemKind='Volume' AND kMDItemDisplayName =?".format(a, b), (str(
                mount_volList[y]),))
            output = cursor.fetchall()
            e.clear()
            for (row) in output:
                e.append(str(row[0]))
            if counter == 2:
                mount_fsList.append(str(e))
                fsLength: int = len(mount_fsList)
                if y == (volLength - 1):
                    y = 0
                    counter = counter + 1
                else:
                     y = y + 1
            elif counter == 3:
                mount_lsList.append(str(e))
                lsLength: int = len(mount_lsList)
                if y == (volLength - 1):
                    y = 0
                    counter = counter + 1
                else:
                     y = y + 1
            else:
                y = (volLength + 1)
                #counter = counter +1
                #end = "yes"
    else:
        while L < volLength:
            a = sc
            b = bs
            cursor.execute("SELECT {} FROM {} WHERE User = ? AND All_Commands LIKE ?".format(a, b),
                           (userSearch, '%' + str(mount_volList[L]) + '%',))
            bashOutput = cursor.fetchall()
            f.clear()
            for row in bashOutput:
                f.append(str(row[0]))
            mount_bashList.append(str(f))
            L = L + 1
        end = "yes"

m = 0
z = 0

while m < (volLength):

    file.write("\t-Volume Name: " + str(mount_volList[z]) + "\n" + "\t\tVolume created on: " + str(
        mount_crList[z]) + "\n" + "\t\tVolume first seen on: " + str(
        mount_fsList[z]) + "\n" + "\t\tVolume last seen on: " + str(
        mount_lsList[z]) + "\n" + "\t\tBash Command: " + str(
        mount_bashList[z]) + "\n")
    m = m + 1
    z = z + 1


a = "None"
b = "None"
output = None
print("Mounted Volume Parsing Completed!")