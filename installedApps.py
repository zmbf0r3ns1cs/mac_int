# Query Logic for Installed Applications v0.1
# Justin Boncaldo, Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

import sqlite3
import re
from variable_db import *
#from mountedDevices import *

# Specify files here for testing
file = open('/Users/zachburnham/Desktop/Capstone/Mac_apt_Output/exampleWrite.txt', 'w+')
connection = sqlite3.connect('/Users/zachburnham/Desktop/Capstone/Mac_apt_Output/mac_apt02.db')
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
endGen = "no"
counter = 0
output = None



# Username search (may be in main function, TBD)
userSearch = input("What User? (Enter for default All): ")
print("Starting Installed Application Parsing for " + str(userSearch) + "...")

# Define variables for table
while endGen != "yes":

    # Round 1 includes InstallHistory, DockItems, and NetUsage. Only require one parameter
    # 0 - 2 = InstallHistory
    # 3 - 9 = NetUsage
    # Round 2 includes RecentItems, Safari. Require two parameters (Add BashSessions and Quarantine)
    # 10 - 11 = RecentItems
    # 14 - 17 = DockItems
    # 16 - 17 = Safari
    # Round 3 includes Users and Spotlight
    # 18 - 20 Quarantine
    if counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        print("[~] Finding Updates...")
        while counter in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
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
                a = n
                b = nU
                c = T
                g = App
            elif counter == 4:
                a = fSD
                b = nU
                c = T
                g = App
            elif counter == 5:
                a = lSD
                b = nU
                c = T
                g = App
            elif counter == 6:
                a = win
                b = nU
                c = T
                g = App
            elif counter == 7:
                a = wout
                b = nU
                c = T
                g = App
            elif counter == 8:
                a = wirIn
                b = nU
                c = T
                g = App
            elif counter == 9:
                a = wirOut
                b = nU
                c = T
                g = App

            cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))
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
                    inst_appName_List.append(string1)
                    AppNameLength: int = len(inst_appName_List)
                elif counter == 4:
                    inst_fSD_List.append(string1)
                    fSDLength: int = len(inst_fSD_List)
                elif counter == 5:
                    inst_lSD_List.append(string1)
                    lSDLength: int = len(inst_lSD_List)
                elif counter == 6:
                    inst_wifiIn_List.append(string1)
                    AppNameLength: int = len(inst_wifiIn_List)
                elif counter == 7:
                    inst_wifiOut_List.append(string1)
                    wOutLength: int = len(inst_wifiOut_List)
                elif counter == 8:
                    inst_wiredIn_List.append(string1)
                    wirInLength: int = len(inst_wiredIn_List)
                elif counter == 9:
                    inst_wiredOut_List.append(string1)
                    wirOutLength: int = len(inst_wiredOut_List)
                else:
                    continue
            counter = counter + 1

    else:
        endGen = "yes"



while end != "yes":
    # These require two parameters
    if counter in (10, 11, 12, 13, 14, 15, 16, 17):
        print("[~] Finding User Downloads...")
        while counter in (10, 11, 12, 13, 14, 15, 16, 17):
            if counter == 10:
                a = n
                b = ri
                c = T
                g = u
                h = application
                i = userSearch
            if counter == 11:
                a = url
                b = ri
                c = T
                g = u
                h = application
                i = userSearch
            if counter == 12:
                a = NoT
                b = S
                c = T
                g = u
                h = dL
                i = userSearch
            if counter == 13:
                a = url
                b = S
                c = T
                g = u
                h = dL
                i = userSearch
            elif counter == 14:
                a = fL
                b = di
                c = u
                g = fT
                h = userSearch
                i = appCode
            elif counter == 15:
                a = pM
                b = di
                c = u
                g = fT
                h = userSearch
                i = appCode
            elif counter == 16:
                a = fM
                b = di
                c = u
                g = fT
                h = userSearch
                i = appCode
            elif counter == 17:
                a = fP
                b = di
                c = u
                g = fT
                h = userSearch
                i = appCode

            cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
            output = cursor.fetchall()
            d.clear()
            for row in output:
                d.append(str(row[0]))
            pos = 0
            for (row) in output:
                string1 = str(d[pos])
                pos = pos + 1
                # Volume Name List Start
                if counter == 10:
                    inst_recentIName_List.append(string1)
                    riNLength1: int = len(inst_recentIName_List)
                if counter == 11:
                    inst_recentIURL_List.append(string1)
                    riURLLength1: int = len(inst_recentIURL_List)
                if counter == 12:
                    inst_SNoT_List.append(string1)
                    sNoTLength1: int = len(inst_SNoT_List)
                if counter == 13:
                    inst_sURL_List.append(string1)
                    sURLLength1: int = len(inst_sURL_List)
                if counter == 14:
                    inst_fileLabelList.append(string1)
                    fLLength: int = len(inst_fileLabelList)
                if counter == 15:
                    inst_parentModifiedList.append(string1)
                    pMLength: int = len(inst_parentModifiedList)
                if counter == 16:
                    inst_fileModifiedList.append(string1)
                    fMLength: int = len(inst_fileModifiedList)
                if counter == 17:
                    inst_filePathList.append(string1)
                    fPLength: int = len(inst_filePathList)
                else:
                    continue
            counter = counter + 1

    # Spotlight database for individual has to reference Users first for UID
    if counter == 18:
        # Need to find user's UID first from Users table
        cursor.execute('SELECT UID FROM Users WHERE Username=?', (userSearch,))
        output = cursor.fetchall()
        d.clear()
        for row in output:
            d.append(str(row[0]))
        pos = 0
        for (row) in output:
            string1 = str(d[pos])
            pos = pos + 1
            inst_userUID_List.append(string1)  # This now holds the user's UID
        counter = counter + 1

    # Starts actual spotlight parsing now
    if counter in (19, 20, 21, 22, 23, 24):
        print("[~] Finding User's Applications...")
        while counter in (19, 20, 21, 22, 23, 24):
            if counter == 19:  # Starts checks for pue in everything. Then needs to check for com.microsoft
                a = idn
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = pue
            elif counter == 20:
                a = ifn
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = pue
            elif counter == 21:
                a = ik
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = pue
            elif counter == 22:
                a = ps
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = pue
            elif counter == 23:
                a = ida
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = pue
            elif counter == 24:
                a = iwf
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = pue
            cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
            output = cursor.fetchall()
            d.clear()
            for row in output:
                d.append(str(row[0]))
            pos = 0
            for (row) in output:
                string1 = str(d[pos])
                pos = pos + 1
                if counter == 19:
                    inst_idn_List.append(string1)  # This now holds the user's UID
                elif counter == 20:
                    inst_ifn_List.append(string1)
                elif counter == 21:
                    inst_ik_List.append(string1)
                elif counter == 22:
                    inst_ps_List.append(string1)
                elif counter == 23:
                    inst_ida_List.append(string1)
                elif counter == 24:
                    inst_iwf_List.append(string1)
                else:
                    continue
            counter = counter + 1

    # Continues spotlight parsing now
    if counter in (25, 26, 27, 28, 29, 30):
        while counter in (25, 26, 27, 28, 29, 30):
            if counter == 25:  # Starts checks for com.microsoft
                a = idn
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = cmwe
            elif counter == 26:
                a = ifn
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = cmwe
            elif counter == 27:
                a = ik
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = cmwe
            elif counter == 28:
                a = ps
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = cmwe
            elif counter == 29:
                a = ida
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = pue
            elif counter == 30:
                a = iwf
                b = sls
                c = ioUID
                g = ict
                h = str(inst_userUID_List[0])
                i = cmwe
            cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=? AND "{}"=?'.format(a, b, c, g), (h, i))
            output = cursor.fetchall()
            d.clear()
            for row in output:
                d.append(str(row[0]))
            pos = 0
            for (row) in output:
                string1 = str(d[pos])
                pos = pos + 1
                if counter == 25:
                    inst_idn2_List.append(string1)
                elif counter == 26:
                    inst_ifn2_List.append(string1)
                elif counter == 27:
                    inst_ik2_List.append(string1)
                elif counter == 28:
                    inst_ps2_List.append(string1)
                elif counter == 39:
                    inst_ida2_List.append(string1)
                elif counter == 30:
                    inst_iwf2_List.append(string1)
                else:
                    continue
            counter = counter + 1

    if counter in (31, 32, 33):
        while counter in (31, 32, 33):
            if counter == 31:
                a = date
                b = ih
                c = pN
                g = macOS
            elif counter == 32:
                a = date
                b = ih
                c = pN
                g = softwareupdated
            elif counter == 33:
                a = date
                b = ih
                c = pN
                g = installer
            cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))
            output = cursor.fetchall()
            d.clear()
            for row in output:
                d.append(str(row[0]))
            pos = 0
            for (row) in output:
                string1 = str(d[pos])
                pos = pos + 1
                # Volume Name List Start
                if counter == 31:
                    inst_date1List.append(string1)
                    pNLength1: int = len(inst_date1List)
                elif counter == 32:
                    inst_date2List.append(string1)
                    pNLength2: int = len(inst_date2List)
                elif counter == 33:
                    inst_date3List.append(string1)
                    pNLength3: int = len(inst_date3List)
                else:
                    continue
            counter = counter + 1
    else:
        end = "yes"




    # # Quarantine search requires a fuzzy name search with regex. DO NOT REMOVE FOR NOW
    # print("Counter before 18: " + str(counter))
    # if counter == 18:  # Change to if counter in 18, 19, 20
    #     y = 0
    #     while y <= sNoTLength1:
    #         print(str(counter))
    #         if counter == 18:
    #             a = tS
    #             b = q
    #             c = u
    #             g = dU
    #             h = userSearch
    #             i = inst_SNoT_List
    #         # Define Last Seen List Variables
    #         # elif counter == 3:
    #         #     a = du
    #         #     b = sls
    #         else:
    #             counter = counter + 1
    #         # SQLite Search Start
    #         cursor.execute("SELECT {} FROM {} WHERE {}=? AND {} LIKE ?".format(a, b, c, g), (h, '%' + str(i) + '%',))
    #         output = cursor.fetchall()
    #         e.clear()
    #         for (row) in output:
    #             e.append(str(row[0]))
    #         # First Seen List Start
    #         if counter == 18:
    #             print("made it to list append")
    #             inst_quarantineTimeStamp_List.append(str(e))
    #             quarantineTSLength: int = len(inst_quarantineTimeStamp_List)
    #             # if y == (volLength - 1):
    #             #     y = 0
    #             #     counter = counter + 1
    #             # else:
    #             y = y + 1

    # #     #----------------------
print("System-wide items")
print("macOS Installer Instance: " + str(inst_processName1List))
print("macOS Installer Date: " + str(inst_date1List))
print("Software Updated Instance: " + str(inst_processName2List))
print("Software Updated Date: " + str(inst_date2List))
print("Installer Instance: " + str(inst_processName3List))
print("Installer Date: " + str(inst_date3List))
print("Docker File Label: " + str(inst_fileLabelList))
print("Docker Parent Modified: " + str(inst_parentModifiedList))
print("Docker File Modified: " + str(inst_fileModifiedList))
print("Docker File Path: " + str(inst_filePathList))
print("App Name: " + str(inst_appName_List))
print("FirstSeenDate: " + str(inst_fSD_List))
print("LastSeenDate: " + str(inst_lSD_List))
print("WifiIn: " + str(inst_wifiIn_List))
print("WifiOut: " + str(inst_wifiOut_List))
print("WiredIn: " + str(inst_wiredIn_List))
print("WireOut: " + str(inst_wiredOut_List))
print("\n")
print("User Specific items")
print("Recently Used Apps: " + str(inst_recentIName_List))
print("Recently Used App URL: " + str(inst_recentIURL_List))
print("File Download from Safari: " + str(inst_SNoT_List))
print("File Download from Safari: " + str(inst_sURL_List))
print("\n")
print("User's Unix Executables:")
print("Item Display Name: " + str(inst_idn_List))
print("Item File Name: " + str(inst_ifn_List))
print("Item Kind: " + str(inst_ik_List))
print("Physical Size: " + str(inst_ps_List))
print("Item Date Added: " + str(inst_ida_List))
print("Item Where from: " + str(inst_iwf_List))
print("\n")
print("User's Microsoft Windows Executables:")
print("Item Display Name: " + str(inst_idn2_List))
print("Item File Name: " + str(inst_ifn2_List))
print("Item Kind: " + str(inst_ik2_List))
print("Physical Size: " + str(inst_ps2_List))
print("Item Date Added: " + str(inst_ida2_List))
print("Item Where from: " + str(inst_iwf2_List))



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
