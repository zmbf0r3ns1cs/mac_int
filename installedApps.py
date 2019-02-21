# Query Logic for Installed Applications v0.1
# Justin Boncaldo, Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re

# Specify files here for testing
file = open('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\exampleWrite.txt', 'w+')
connection = sqlite3.connect('E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\mac_apt02.db')
cursor = connection.cursor()

# Mounted Volume variables
global a, b, c, g, output

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
fileLabel = []
parentModified = []
fileModified = []
filePath = []
appName_List = []
fSD_List = []
lSD_List = []
wifiIn_List = []
wifiOut_List = []
wiredIn_List = []
wiredOut_List = []



string1 = "None"

# Define variables
# Tables
di = '"Dock Items"'
ih = '"InstallHistory"'
nU = 'NetUsage'

# Columns
fL = '"File Label"'
fT = '"File Type"'
pM = '"Parent Modified"'
fM = '"File Modified"'
fP = '"File Path"'
date = '"Date"'
dN = '"DisplayName"'
pN = '"ProcessName"'
u = '"User"'
n = '"Name"'
fSD = '"FirstSeenDate"'
lSD = '"LastSeenDate"'
win = '"WifiIn"'
wout = '"wifiOut"'
wirIn = '"WiredIn"'
wirOut = '"WiredOut"'
App = "App"


# Values
macOS = "macOS Installer"
softwareupdated = "softwareupdated"
installer = "installer"
T = '"Type"'
# Define counters
L = 0
end = "no"
counter = 0
output = None

# Username search (may be in main function, TBD)
userSearch = input("What User? (Enter for default All): ")
print("Starting Installed Application Parsing for " + str(userSearch) + "...")

# Define variables for table
while end != "yes":

    # Round 1 includes InstallHistory, DockItems, and NetUsage
    # 0 - 2 = InstallHistory
    # 3 - 6 = DockItems
    if counter < 14:
        while counter < 14:
            if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
                if counter == 0:
                    a = dN
                    b = ih
                    c = pN
                    g = macOS
                elif counter == 1:
                    a = dN
                    b = ih
                    c = pN
                    g = softwareupdated
                elif counter == 2:
                    a = dN
                    b = ih
                    c = pN
                    g = installer
                elif counter == 3:
                    a = fL
                    b = di
                    c = u
                    g = userSearch
                elif counter == 4:
                    a = fL
                    b = di
                    c = u
                    g = userSearch
                elif counter == 5:
                    a = fM
                    b = di
                    c = u
                    g = userSearch
                elif counter == 6:
                    a = fP
                    b = di
                    c = u
                    g = userSearch
                elif counter == 7:
                    a = n
                    b = nU
                    c = T
                    g = App
                elif counter == 8:
                    a = fSD
                    b = nU
                    c = T
                    g = App
                elif counter == 9:
                    a = lSD
                    b = nU
                    c = T
                    g = App
                elif counter == 10:
                    a = win
                    b = nU
                    c = T
                    g = App
                elif counter == 11:
                    a = wout
                    b = nU
                    c = T
                    g = App
                elif counter == 12:
                    a = wirIn
                    b = nU
                    c = T
                    g = App
                elif counter == 13:
                    a = wirOut
                    b = nU
                    c = T
                    g = App
                else:
                    continue

                cursor.execute("SELECT {} FROM {} WHERE {}=?".format(a, b, c), (g,))
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
                        pNLength3: int = len(processName3)
                    elif counter == 3:
                        fileLabel.append(string1)
                        fLLength: int = len(fileLabel)
                    elif counter == 4:
                        parentModified.append(string1)
                        pMLength: int = len(parentModified)
                    elif counter == 5:
                        fileModified.append(string1)
                        fMLength: int = len(fileModified)
                    elif counter == 6:
                        filePath.append(string1)
                        fPLength: int = len(filePath)
                    elif counter == 7:
                        appName_List.append(string1)
                        AppNameLength: int = len(appName_List)
                    elif counter == 8:
                        fSD_List.append(string1)
                        fSDLength: int = len(fSD_List)
                    elif counter == 9:
                        lSD_List.append(string1)
                        lSDLength: int = len(lSD_List)
                    elif counter == 10:
                        wifiIn_List.append(string1)
                        AppNameLength: int = len(wifiIn_List)
                    elif counter == 11:
                        wifiOut_List.append(string1)
                        wOutLength: int = len(wifiOut_List)
                    elif counter == 12:
                        wiredIn_List.append(string1)
                        wirInLength: int = len(wiredIn_List)
                    elif counter == 13:
                        wiredOut_List.append(string1)
                        wirOutLength: int = len(wiredOut_List)
                    else:
                        continue
            counter = counter + 1




    # elif counter in (3, 4, 5, 6):
    #     if counter == 3:
    #         a = dN
    #         b = di
    #         process = "macOS Installer"
    #     elif counter == 4:
    #         a = dN
    #         b = di
    #         process = "softwareupdated"
    #     elif counter == 5:
    #         a = dN
    #         b = di
    #         process = "installer"
    #     elif counter == 6:
    #         a = dN
    #         b = di
    #         process = "installer"
    #     else:
    #         continue
    #
    #     cursor.execute("SELECT {} FROM {} WHERE ProcessName=?".format(a, b), (process,))
    #     output = cursor.fetchall()
    #     d.clear()
    #     for row in output:
    #         d.append(str(row[0]))
    #     pos = 0
    #     for (row) in output:
    #         string1 = str(d[pos])
    #         pos = pos + 1
    #         # Volume Name List Start
    #         if counter == 0:
    #             processName1.append(string1)
    #             pNLength1: int = len(processName1)
    #         elif counter == 1:
    #             processName2.append(string1)
    #             pNLength2: int = len(processName2)
    #         elif counter == 2:
    #             processName3.append(string1)
    #             pNLength3: int = len(string1)
    #         else:
    #             continue
    # counter = counter + 1











#----------------------
    else:
        continue
    print(str(counter))
    # print("macOS Installer Instance: " + str(processName1))
    # print("Software Updated Instance: " + str(processName2))
    # print("Installer Instance: " + str(processName3))
    # print("File Label: " + str(fileLabel))
    # print("Parent Modified: " + str(parentModified))
    # print("File Modified: " + str(fileModified))
    # print("File Path: " + str(filePath))
    #print("App Name: " + str(appName_List))
    #print("FirstSeenDate: " + str(fSD_List))
    #print("LastSeenDate: " + str(lSD_List))
    #print("WifiIn: " + str(wifiIn_List))
    #print("WifiOut: " + str(wifiOut_List))
    #print("WiredIn: " + str(wiredIn_List))
    #print("WireOut: " + str(wiredOut_List))

    end = "yes"







# Global Variables
a = "None"
b = "None"
c = "None"
g = "None"
output = None

# End Parsing
print("Installed Application Parsing Completed!")
