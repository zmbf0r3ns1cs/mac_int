# Query Logic for Mounted Devices/Volumes v0.9
# Justin Boncaldo, Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re

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
inst_fLList = []
inst_pMList = []
inst_fMList = []
inst_fPList = []
inst_fTList = []
inst_dateList = []
inst_dNList = []
inst_pNList = []
processName1 = []
processName2 = []
processName3 = []
string1 = "None"

# Define variables
# Tables
di = '"Dock Items"'
ih = '"InstallHistory"'

# Columns
fL = '"File Label"'
fT = '"File Type"'
pM = '"Parent Modified"'
fM = '"File Modified"'
fP = '"File Path"'
date = '"Date"'
dN = '"DisplayName"'
pN = '"ProcessName"'

# Define counters
c = 0
L = 0

x = "first"
end = "no"
counter = 0
output = None

# Username search (may be in main function, TBD)
userSearch = input("What User? (Enter for default All): ")
print("Starting Installed Application Parsing for " + str(userSearch) + "...")

# Define variables for table
while end != "yes":

    if counter in (0, 1, 2):
        while counter < 3:
            if counter in (0, 1, 2):
                if counter == 0:
                    a = dN
                    b = ih
                    process = "macOS Installer"
                elif counter == 1:
                    a = dN
                    b = ih
                    process = "softwareupdated"
                elif counter == 2:
                    a = dN
                    b = ih
                    process = "installer"
                else:
                    continue

                cursor.execute("SELECT {} FROM {} WHERE ProcessName=?".format(a, b), (process,))
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
                        processName1.append(string1)
                        pNLength1: int = len(processName1)
                    elif counter == 1:
                        processName2.append(string1)
                        pNLength2: int = len(processName2)
                    elif counter == 2:
                        processName3.append(string1)
                        pNLength3: int = len(string1)
                    else:
                        continue
            counter = counter + 1
    elif counter == 3:
        #print("Test for 3")
        continue
    print(str(counter))
    print("macOS Installer Instance: " + str(processName1))
    print("Software Updated Instance: " + str(processName2))
    print("Installer Instance: " + str(processName3))
    end = "yes"







# Global Variables
a = "None"
b = "None"
output = None

# End Parsing
print("Installed Application Parsing Completed!")