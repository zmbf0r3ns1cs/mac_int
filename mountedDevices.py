# Query Logic for Mounted Devices/Volumes v0.9
# Justin Boncaldo, Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re
from variable_db import *

# Specify files here for testing
file = open('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\exampleWrite.txt', 'w+')
connection = sqlite3.connect('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\mac_apt02.db')
cursor = connection.cursor()

# Mounted Volume variables
global a, b, output

# Define strings
d = []
e = []
f = []


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

# Define variables for table
while end != "yes":
    if (counter == 0) or (counter == 1):
        # Define Volume Name List Variables
        if counter == 0:
            a = n
            b = ri
        # Define Created Date List Variables
        elif counter == 1:
            a = i
            b = ri
        # SQLite Search Start
        cursor.execute("SELECT {} FROM {} WHERE Type='VOLUME' AND User=?".format(a, b), (userSearch,))
        output = cursor.fetchall()
        d.clear()
        for row in output:
            d.append(str(row[0]))
        pos = 0
        for (row) in output:
            string1 = str(d[pos])
            pos = pos + 1
            # Volume Name List Start
            if counter == 0:
                mount_volList.append(string1)
                volLength: int = len(mount_volList)
            # Created Date List Start
            elif counter == 1:
                mount_crList.append(string1)
                crLength: int = len(mount_crList)
            else:
                continue
        counter = counter + 1
    # Define variables for table
    elif (counter == 2) or (counter == 3):
        while y < volLength:
            # Define First Seen List Variables
            if counter == 2:
                a = icd
                b = sls
            # Define Last Seen List Variables
            elif counter == 3:
                a = du
                b = sls
            else:
                counter = counter + 1
            # SQLite Search Start
            cursor.execute("SELECT {} FROM {} WHERE kMDItemKind='Volume' AND kMDItemDisplayName =?".format(a, b), (str(
                mount_volList[y]),))
            output = cursor.fetchall()
            e.clear()
            for (row) in output:
                e.append(str(row[0]))
            # First Seen List Start
            if counter == 2:
                mount_fsList.append(str(e))
                fsLength: int = len(mount_fsList)
                if y == (volLength - 1):
                    y = 0
                    counter = counter + 1
                else:
                     y = y + 1
            # Last Seen List Start
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
    else:
        # Define variables for Bash Commands
        while L < volLength:
            a = sc
            b = bs
            # SQLite Search Start
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

# Begin writing output
while m < (volLength):
    file.write("\t-Volume Name: " + str(mount_volList[z]) + "\n" + "\t\tVolume created on: " + str(
        mount_crList[z]) + "\n" + "\t\tVolume first seen on: " + str(
        mount_fsList[z]) + "\n" + "\t\tVolume last seen on: " + str(
        mount_lsList[z]) + "\n" + "\t\tBash Command: " + str(
        mount_bashList[z]) + "\n")
    m = m + 1
    z = z + 1

# Global Variables
a = "None"
b = "None"
output = None

# End Parsing
print("Mounted Volume Parsing Completed!")
