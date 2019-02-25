# Query Logic for Installed Applications v0.1
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
global a, b, c, g, h, i, output

# Define strings
d = []
e = []
f = []

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
    # 7 - 13 = NetUsage
    # Round 2 includes RecentItems, Safari, BashSessions, and Quarantine
    # 14 - 15 = RecentItems
    # 16 - 17 = Safari
    # 18 - 20 = Quarantine
    if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
        while counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
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
                    inst_processName1List.append(string1)
                    pNLength1: int = len(inst_processName1List)
                elif counter == 1:
                    inst_processName2List.append(string1)
                    pNLength2: int = len(inst_processName2List)
                elif counter == 2:
                    inst_processName3List.append(string1)
                    pNLength3: int = len(inst_processName3List)
                elif counter == 3:
                    inst_fileLabelList.append(string1)
                    fLLength: int = len(inst_fileLabelList)
                elif counter == 4:
                    inst_parentModifiedList.append(string1)
                    pMLength: int = len(inst_parentModifiedList)
                elif counter == 5:
                    inst_fileModifiedList.append(string1)
                    fMLength: int = len(inst_fileModifiedList)
                elif counter == 6:
                    inst_filePathList.append(string1)
                    fPLength: int = len(inst_filePathList)
                elif counter == 7:
                    inst_appName_List.append(string1)
                    AppNameLength: int = len(inst_appName_List)
                elif counter == 8:
                    inst_fSD_List.append(string1)
                    fSDLength: int = len(inst_fSD_List)
                elif counter == 9:
                    inst_lSD_List.append(string1)
                    lSDLength: int = len(inst_lSD_List)
                elif counter == 10:
                    inst_wifiIn_List.append(string1)
                    AppNameLength: int = len(inst_wifiIn_List)
                elif counter == 11:
                    inst_wifiOut_List.append(string1)
                    wOutLength: int = len(inst_wifiOut_List)
                elif counter == 12:
                    inst_wiredIn_List.append(string1)
                    wirInLength: int = len(inst_wiredIn_List)
                elif counter == 13:
                    inst_wiredOut_List.append(string1)
                    wirOutLength: int = len(inst_wiredOut_List)
                else:
                    continue
            counter = counter + 1

    if counter in (14, 15, 16, 17):
        while counter in (14, 15, 16, 17):
            if counter == 14:
                a = n
                b = ri
                c = T
                g = u
                h = application
                i = userSearch
            if counter == 15:
                a = url
                b = ri
                c = T
                g = u
                h = application
                i = userSearch
            if counter == 16:
                a = NoT
                b = S
                c = T
                g = u
                h = dL
                i = userSearch
            if counter == 17:
                a = url
                b = S
                c = T
                g = u
                h = dL
                i = userSearch

            cursor.execute("SELECT {} FROM {} WHERE {}=? AND {}=?".format(a, b, c, g), (h, i))
            output = cursor.fetchall()
            d.clear()
            for row in output:
                d.append(str(row[0]))
            pos = 0
            for (row) in output:
                string1 = str(d[pos])
                pos = pos + 1
                # Volume Name List Start
                if counter == 14:
                    inst_recentIName_List.append(string1)
                    riNLength1: int = len(inst_recentIName_List)
                if counter == 15:
                    inst_recentIURL_List.append(string1)
                    riURLLength1: int = len(inst_recentIURL_List)
                if counter == 16:
                    inst_SNoT_List.append(string1)
                    sNoTLength1: int = len(inst_SNoT_List)
                if counter == 17:
                    inst_sURL_List.append(string1)
                    sURLLength1: int = len(inst_sURL_List)
                else:
                    continue
            counter = counter + 1

    if counter == 18: # Chnage to if counter in 18, 19, 20
        if counter == 18:
            a =
            b =
            c =
            g =
            h = userSearch
            i =

            while y < volLength:
                # Define First Seen List Variables
                if counter == 2:
                    print("[~] Finding First Seen Date for Volume " + str(y) + "...")
                    a = icd
                    b = sls
                # Define Last Seen List Variables
                elif counter == 3:
                    print("[~] Finding Last Seen Date for Volume " + str(y) + "...")
                    a = du
                    b = sls
                else:
                    counter = counter + 1
                # SQLite Search Start
                cursor.execute("SELECT {} FROM {} WHERE kMDItemKind='Volume' AND kMDItemDisplayName =?".format(a, b),
                               (str(
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
        #----------------------
    print(str(counter))
    # print("macOS Installer Instance: " + str(inst_processName1List))
    # print("Software Updated Instance: " + str(inst_processName2List))
    # print("Installer Instance: " + str(inst_processName3List))
    # print("File Label: " + str(inst_fileLabelList))
    # print("Parent Modified: " + str(inst_parentModifiedList))
    # print("File Modified: " + str(inst_fileModifiedList))
    # print("File Path: " + str(inst_filePathList))
    #print("App Name: " + str(inst_appName_List))
    #print("FirstSeenDate: " + str(inst_fSD_List))
    #print("LastSeenDate: " + str(inst_lSD_List))
    # print("WifiIn: " + str(inst_wifiIn_List))
    # print("WifiOut: " + str(inst_wifiOut_List))
    # print("WiredIn: " + str(inst_wiredIn_List))
    #print("WireOut: " + str(inst_wiredOut_List))
    #print("Recently Used Apps: " + str(inst_recentIName_List))
    #print("Recently Used App URL: " + str(inst_recentIURL_List))
    print("File Download from Safari: " + str(inst_SNoT_List))
    print("File Download from Safari: " + str(inst_sURL_List))

    end = "yes"

# Global Variables
a = "None"
b = "None"
c = "None"
g = "None"
h = "None"
i = "None"
output = None

# End Parsing
print("Installed Application Parsing Completed!")
